#!/usr/bin/env python3
"""Inventory local protected 3D sources and statically inspect ZIP/3MF files."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import posixpath
import stat
import sys
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any
from xml.etree import ElementTree as ET


FORMATS = {".stl": "STL", ".3mf": "3MF", ".step": "STEP", ".stp": "STEP",
           ".sldasm": "SLDASM", ".sldprt": "SLDPRT", ".iges": "IGES",
           ".igs": "IGES", ".obj": "OBJ", ".amf": "AMF", ".zip": "ZIP"}
MAX_ARCHIVE_MEMBERS = 10_000
MAX_MEMBER_BYTES = 256 * 1024 * 1024
MAX_UNCOMPRESSED_BYTES = 512 * 1024 * 1024
MAX_XML_MODEL_BYTES = 128 * 1024 * 1024
MAX_GRAPH_DEPTH = 512
CORE_NS = "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
PROD_NS = "http://schemas.microsoft.com/3dmanufacturing/production/2015/06"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
UNIT_TO_MM = {"micron": 0.001, "millimeter": 1.0, "centimeter": 10.0,
              "inch": 25.4, "foot": 304.8, "meter": 1000.0}


class VerificationError(ValueError):
    """Unsafe, malformed, or over-budget input."""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def safe_member_path(name: str) -> PurePosixPath:
    """Return a safe normalized ZIP path; allow only the final directory slash."""
    if not name or "\\" in name or "\x00" in name:
        raise VerificationError(f"unsafe archive path: {name!r}")
    raw_parts = name.split("/")
    if raw_parts[-1] == "":
        raw_parts.pop()
    if not raw_parts or any(part in ("", ".", "..") for part in raw_parts):
        raise VerificationError(f"unsafe archive path: {name!r}")
    path = PurePosixPath(*raw_parts)
    if path.is_absolute() or raw_parts[0].endswith(":"):
        raise VerificationError(f"unsafe archive path: {name!r}")
    return path


def validate_zip_metadata(zf: zipfile.ZipFile) -> list[zipfile.ZipInfo]:
    infos = zf.infolist()
    if len(infos) > MAX_ARCHIVE_MEMBERS:
        raise VerificationError(f"archive has more than {MAX_ARCHIVE_MEMBERS} members")
    total = 0
    seen: set[str] = set()
    for info in infos:
        safe_member_path(info.filename)
        if info.filename in seen:
            raise VerificationError(f"duplicate archive path: {info.filename}")
        seen.add(info.filename)
        mode = info.external_attr >> 16
        if stat.S_ISLNK(mode):
            raise VerificationError(f"symlink archive member not allowed: {info.filename}")
        if info.file_size > MAX_MEMBER_BYTES:
            raise VerificationError(f"archive member exceeds {MAX_MEMBER_BYTES} bytes: {info.filename}")
        total += info.file_size
        if total > MAX_UNCOMPRESSED_BYTES:
            raise VerificationError(f"archive exceeds {MAX_UNCOMPRESSED_BYTES} uncompressed bytes")
    bad = zf.testzip()
    if bad is not None:
        raise VerificationError(f"archive CRC test failed at {bad}")
    return infos


def read_checked(zf: zipfile.ZipFile, info: zipfile.ZipInfo) -> bytes:
    safe_member_path(info.filename)
    if info.file_size > MAX_MEMBER_BYTES:
        raise VerificationError(f"archive member exceeds {MAX_MEMBER_BYTES} bytes: {info.filename}")
    try:
        data = zf.read(info)
    except (zipfile.BadZipFile, RuntimeError, OSError, EOFError) as exc:
        raise VerificationError(f"cannot read {info.filename}: {exc}") from exc
    if len(data) != info.file_size:
        raise VerificationError(f"size mismatch for {info.filename}")
    return data


def local_name(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


def children(element: ET.Element, name: str) -> list[ET.Element]:
    return [child for child in element if local_name(child) == name]


def matrix_from(value: str | None) -> list[list[float]]:
    if value is None or not value.strip():
        return [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]
    parts = [float(item) for item in value.split()]
    if len(parts) != 12 or any(not math.isfinite(item) for item in parts):
        raise VerificationError(f"invalid 3MF transform: {value!r}")
    # 3MF serializes the first three columns of a row-major matrix; convert to
    # the conventional column-vector affine matrix used by the calculations.
    return [[parts[0], parts[3], parts[6], parts[9]],
            [parts[1], parts[4], parts[7], parts[10]],
            [parts[2], parts[5], parts[8], parts[11]],
            [0.0, 0.0, 0.0, 1.0]]


def multiply(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    return [[sum(left[r][k] * right[k][c] for k in range(4)) for c in range(4)] for r in range(4)]


def uniform_scale(value: float) -> list[list[float]]:
    return [[value, 0.0, 0.0, 0.0], [0.0, value, 0.0, 0.0],
            [0.0, 0.0, value, 0.0], [0.0, 0.0, 0.0, 1.0]]


def clean_float(value: float) -> float:
    rounded = round(value, 9)
    return 0.0 if abs(rounded) < 0.000000001 else rounded


def transform_bounds(bounds: list[list[float]], transform: list[list[float]]) -> list[list[float]]:
    points = []
    for x in bounds[0]:
        for y in bounds[1]:
            for z in bounds[2]:
                point = [x, y, z, 1.0]
                points.append([sum(transform[r][c] * point[c] for c in range(4)) for r in range(3)])
    return [[clean_float(min(point[axis] for point in points)),
             clean_float(max(point[axis] for point in points))] for axis in range(3)]


def manifest_matrix(matrix: list[list[float]]) -> list[list[float]]:
    return [[clean_float(value) for value in row] for row in matrix]


def mesh_stats(mesh: ET.Element, unit: str | None = None) -> dict[str, Any]:
    vertices_node = next(iter(children(mesh, "vertices")), None)
    triangles_node = next(iter(children(mesh, "triangles")), None)
    if vertices_node is None or triangles_node is None:
        raise VerificationError("mesh is missing vertices or triangles")
    vertices = []
    for vertex in children(vertices_node, "vertex"):
        try:
            point = tuple(float(vertex.attrib[key]) for key in ("x", "y", "z"))
        except (KeyError, ValueError) as exc:
            raise VerificationError(f"invalid mesh vertex: {exc}") from exc
        if any(not math.isfinite(axis) for axis in point):
            raise VerificationError("mesh has non-finite vertex coordinates")
        vertices.append(point)
    triangles = []
    for triangle in children(triangles_node, "triangle"):
        try:
            indices = tuple(int(triangle.attrib[key]) for key in ("v1", "v2", "v3"))
        except (KeyError, ValueError) as exc:
            raise VerificationError(f"invalid mesh triangle: {exc}") from exc
        if any(index < 0 or index >= len(vertices) for index in indices):
            raise VerificationError("mesh triangle references an invalid vertex")
        triangles.append(indices)
    if not vertices or not triangles:
        raise VerificationError("mesh contains no vertices or triangles")
    edges: Counter[tuple[int, int]] = Counter()
    degenerate = 0
    for a, b, c in triangles:
        if len({a, b, c}) < 3:
            degenerate += 1
        else:
            p, q, r = vertices[a], vertices[b], vertices[c]
            u = tuple(q[i] - p[i] for i in range(3))
            v = tuple(r[i] - p[i] for i in range(3))
            cross = (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
            if sum(axis * axis for axis in cross) <= 1e-24:
                degenerate += 1
        for first, second in ((a, b), (b, c), (c, a)):
            edges[tuple(sorted((first, second)))] += 1
    duplicate_count = len(triangles) - len({tuple(sorted(tri)) for tri in triangles})
    bounds = [[min(point[axis] for point in vertices), max(point[axis] for point in vertices)] for axis in range(3)]
    incidence = Counter(edges.values())
    status = "FAIL" if degenerate or duplicate_count else "PASS"
    return {"unit_declared": unit, "vertex_count": len(vertices), "triangle_count": len(triangles),
            "bounds": bounds, "degenerate_triangle_count": degenerate,
            "duplicate_triangle_count": duplicate_count,
            "edge_incidence": {str(count): incidence[count] for count in sorted(incidence)},
            "watertight_by_edge_count": bool(edges) and all(count == 2 for count in edges.values()),
            "manifold_by_edge_count": bool(edges) and all(count <= 2 for count in edges.values()),
            "mesh_status": status}


def package_path(source_part: str, target: str) -> str:
    if not target or "\\" in target or "\x00" in target:
        raise VerificationError(f"invalid relationship target: {target!r}")
    joined = target.lstrip("/") if target.startswith("/") else posixpath.join(posixpath.dirname(source_part), target)
    normalized = posixpath.normpath(joined)
    safe_member_path(normalized)
    return normalized


def rels_part(source_part: str) -> str:
    directory, filename = posixpath.split(source_part)
    return posixpath.join(directory, "_rels", filename + ".rels")


def relationships(data: bytes, source: str) -> dict[str, str]:
    if not data:
        return {}
    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        raise VerificationError(f"malformed relationships for {source}: {exc}") from exc
    result: dict[str, str] = {}
    for relation in children(root, "Relationship"):
        if not relation.attrib.get("Type", "").endswith("/3dmodel"):
            continue
        relation_id = relation.attrib.get("Id")
        target = relation.attrib.get("Target")
        if not relation_id or not target:
            raise VerificationError(f"incomplete 3D model relationship in {source}")
        if relation_id in result:
            raise VerificationError(f"duplicate relationship id {relation_id!r} in {source}")
        result[relation_id] = package_path(source, target)
    return result


def validate_content_types(data: bytes, model_paths: list[str]) -> None:
    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        raise VerificationError(f"malformed 3MF content types: {exc}") from exc
    if root.tag != f"{{{CT_NS}}}Types":
        raise VerificationError("invalid 3MF content types root")
    defaults: dict[str, str] = {}
    overrides: dict[str, str] = {}
    for entry in root:
        if entry.tag == f"{{{CT_NS}}}Default":
            extension, content_type = entry.attrib.get("Extension"), entry.attrib.get("ContentType")
            if not extension or not content_type or extension.lower() in defaults:
                raise VerificationError("invalid or duplicate default content type")
            defaults[extension.lower()] = content_type
        elif entry.tag == f"{{{CT_NS}}}Override":
            part_name, content_type = entry.attrib.get("PartName"), entry.attrib.get("ContentType")
            if not part_name or not content_type:
                raise VerificationError("incomplete content type override")
            normalized = safe_member_path(part_name.lstrip("/")).as_posix()
            if normalized in overrides:
                raise VerificationError(f"duplicate content type override: {normalized}")
            overrides[normalized] = content_type
    expected = "application/vnd.ms-package.3dmanufacturing-3dmodel+xml"
    for path in model_paths:
        content_type = overrides.get(path, defaults.get(Path(path).suffix.lstrip(".").lower()))
        if content_type != expected:
            raise VerificationError(f"missing or invalid 3D model content type: {path}")


def inspect_3mf(data: bytes) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    from io import BytesIO

    try:
        with zipfile.ZipFile(BytesIO(data)) as zf:
            infos = validate_zip_metadata(zf)
            names = {info.filename for info in infos if not info.is_dir()}
            if "[Content_Types].xml" not in names or "_rels/.rels" not in names:
                raise VerificationError("3MF package is missing required package metadata")
            model_paths = sorted(name for name in names if name.startswith("3D/") and name.endswith(".model"))
            if "3D/3dmodel.model" not in model_paths:
                raise VerificationError("3MF is missing 3D/3dmodel.model")
            validate_content_types(member_bytes_data := read_checked(
                zf, next(info for info in infos if info.filename == "[Content_Types].xml")), model_paths)
            members = []
            member_bytes: dict[str, bytes] = {}
            for info in sorted(infos, key=lambda item: item.filename):
                if info.is_dir():
                    continue
                content = read_checked(zf, info)
                if (info.filename.endswith(".model") or info.filename.endswith(".rels")
                        or info.filename in {"[Content_Types].xml", "Metadata/model_settings.config",
                                             "Metadata/project_settings.config"}):
                    if len(content) > MAX_XML_MODEL_BYTES:
                        raise VerificationError(f"3MF model XML exceeds {MAX_XML_MODEL_BYTES} bytes: {info.filename}")
                    member_bytes[info.filename] = content
                members.append({"path": info.filename, "size_bytes": info.file_size, "sha256": sha256(content)})
    except (zipfile.BadZipFile, OSError, EOFError) as exc:
        raise VerificationError(f"invalid 3MF ZIP package: {exc}") from exc

    try:
        root_rels = relationships(member_bytes.get("_rels/.rels", b""), "")
        primary_parts = list(root_rels.values())
        if primary_parts.count("3D/3dmodel.model") != 1:
            raise VerificationError("3MF package must have exactly one root 3D model relationship")
        docs: dict[str, dict[str, Any]] = {}
        issues: list[str] = []
        mesh_records: list[dict[str, Any]] = []
        all_relationships: dict[str, dict[str, str]] = {}
        model_metadata: dict[str, dict[str, str]] = {}
        for path in model_paths:
            try:
                xml_root = ET.fromstring(member_bytes[path])
            except ET.ParseError as exc:
                raise VerificationError(f"malformed 3MF model XML {path}: {exc}") from exc
            if local_name(xml_root) != "model":
                raise VerificationError(f"3MF model part does not have a model root: {path}")
            model_metadata[path] = {el.attrib["name"]: (el.text or "").strip()
                                    for el in children(xml_root, "metadata") if "name" in el.attrib}
            declared_unit = xml_root.attrib.get("unit")
            effective_unit = declared_unit or "millimeter"
            if effective_unit not in UNIT_TO_MM:
                issues.append(f"invalid 3MF unit {effective_unit!r} in {path}")
                effective_unit = "millimeter"
            objects = {}
            for resource in children(next((el for el in xml_root.iter() if local_name(el) == "resources"), ET.Element("resources")), "object"):
                object_id = resource.attrib.get("id")
                if object_id is None or object_id in objects:
                    issues.append(f"duplicate or missing object id in {path}: {object_id}")
                    continue
                mesh = next(iter(children(resource, "mesh")), None)
                components_node = next(iter(children(resource, "components")), None)
                components = children(components_node, "component") if components_node is not None else []
                stats = None
                if mesh is not None:
                    try:
                        stats = mesh_stats(mesh, declared_unit)
                        stats["unit_effective"] = effective_unit
                        stats["unit_source"] = "declared" if declared_unit else "3MF default"
                        stats["bounds_mm"] = [[clean_float(axis * UNIT_TO_MM[effective_unit])
                                                for axis in pair] for pair in stats["bounds"]]
                    except VerificationError as exc:
                        stats = {"mesh_status": "FAIL", "error": str(exc)}
                        issues.append(f"invalid mesh {path} object {object_id}: {exc}")
                    mesh_records.append({"path": path, "object_id": object_id, "mesh": stats})
                if mesh is not None and components:
                    issues.append(f"object mixes a mesh and components: {path} object {object_id}")
                objects[object_id] = {"element": resource, "mesh": stats,
                                      "components": components, "unit": declared_unit,
                                      "effective_unit": effective_unit,
                                      "unit_to_mm": UNIT_TO_MM[effective_unit]}
            docs[path] = {"root": xml_root, "objects": objects, "unit": declared_unit,
                          "effective_unit": effective_unit,
                          "unit_to_mm": UNIT_TO_MM[effective_unit]}
        for source in model_paths:
            part = rels_part(source)
            all_relationships[source] = relationships(member_bytes.get(part, b""), source)

        graph: dict[tuple[str, str], list[tuple[tuple[str, str], list[list[float]]]]] = {}
        component_references = []
        for source, document in docs.items():
            for object_id, obj in document["objects"].items():
                node = (source, object_id)
                links = []
                for component in obj["components"]:
                    target_id = component.attrib.get("objectid")
                    if target_id is None:
                        issues.append(f"component has no objectid at {source} object {object_id}")
                        continue
                    path_attr = component.attrib.get(f"{{{PROD_NS}}}path")
                    target_part = source
                    relationship_found = path_attr is None
                    if path_attr is not None:
                        try:
                            target_part = package_path(source, path_attr)
                        except VerificationError as exc:
                            issues.append(str(exc))
                            continue
                        relationship_found = target_part in all_relationships.get(source, {}).values()
                        if not relationship_found:
                            issues.append(f"component reference has no relationship: {source} -> {target_part}")
                        if target_part not in docs:
                            issues.append(f"component references missing model part: {target_part}")
                            component_references.append({"source_part": source, "source_object_id": object_id,
                                "target_part": target_part, "target_object_id": target_id,
                                "external_path": path_attr, "relationship_found": relationship_found,
                                "target_found": False})
                            continue
                    target_exists = target_id in docs[target_part]["objects"]
                    try:
                        transform = matrix_from(component.attrib.get("transform"))
                    except (ValueError, VerificationError) as exc:
                        issues.append(f"invalid component transform at {source} object {object_id}: {exc}")
                        component_references.append({"source_part": source, "source_object_id": object_id,
                            "target_part": target_part, "target_object_id": target_id,
                            "external_path": path_attr, "relationship_found": relationship_found,
                            "target_found": target_exists, "transform_valid": False})
                        continue
                    ref_record = {"source_part": source, "source_object_id": object_id,
                        "target_part": target_part, "target_object_id": target_id,
                        "external_path": path_attr, "relationship_found": relationship_found,
                        "target_found": target_exists, "transform": manifest_matrix(transform),
                        "source_unit_effective": document["effective_unit"],
                        "target_unit_effective": docs[target_part]["effective_unit"],
                        "target_to_source_unit_scale": clean_float(
                            docs[target_part]["unit_to_mm"] / document["unit_to_mm"])}
                    component_references.append(ref_record)
                    if not target_exists:
                        issues.append(f"component references missing object {target_id} in {target_part}")
                        continue
                    unit_ratio = docs[target_part]["unit_to_mm"] / document["unit_to_mm"]
                    links.append(((target_part, target_id), transform, unit_ratio))
                graph[node] = links

        build = next((el for el in docs["3D/3dmodel.model"]["root"].iter() if local_name(el) == "build"), None)
        build_items = children(build, "item") if build is not None else []
        valid_builds = []
        build_items_report = []
        for index, item in enumerate(build_items):
            object_id = item.attrib.get("objectid")
            if object_id not in docs["3D/3dmodel.model"]["objects"]:
                issues.append(f"build item {index} references missing object {object_id}")
                continue
            try:
                transform = matrix_from(item.attrib.get("transform"))
            except (ValueError, VerificationError) as exc:
                issues.append(f"invalid build transform for object {object_id}: {exc}")
                continue
            printable = item.attrib.get("printable", "1") != "0"
            valid_builds.append((object_id, transform, printable))
            build_items_report.append({"index": index, "object_id": object_id, "printable": printable,
                                      "transform": manifest_matrix(transform)})

        visiting: set[tuple[str, str]] = set()
        cycle_checked: set[tuple[str, str]] = set()
        reachable: set[tuple[str, str]] = set()
        def check_cycles(node: tuple[str, str], depth: int = 0) -> None:
            if depth > MAX_GRAPH_DEPTH:
                issues.append(f"component graph exceeds maximum depth {MAX_GRAPH_DEPTH} at {node[0]} object {node[1]}")
                return
            if node in visiting:
                issues.append(f"component reference cycle at {node[0]} object {node[1]}")
                return
            if node in cycle_checked:
                return
            visiting.add(node)
            for child, _, _ in graph.get(node, []):
                check_cycles(child, depth + 1)
            visiting.remove(node)
            cycle_checked.add(node)

        for node in sorted(graph):
            check_cycles(node)

        def mark_reachable(node: tuple[str, str], depth: int = 0) -> None:
            if depth > MAX_GRAPH_DEPTH:
                issues.append(f"printable component graph exceeds maximum depth {MAX_GRAPH_DEPTH} at {node[0]} object {node[1]}")
                return
            if node in reachable:
                return
            reachable.add(node)
            obj = docs[node[0]]["objects"][node[1]]
            if obj["mesh"] is None and not graph.get(node):
                issues.append(f"referenced object has neither mesh nor components: {node[0]} object {node[1]}")
            for child, _, _ in graph.get(node, []):
                mark_reachable(child, depth + 1)

        for object_id, _, printable in valid_builds:
            if printable:
                mark_reachable(("3D/3dmodel.model", object_id))

        for source, mapping in all_relationships.items():
            for target in mapping.values():
                if target not in member_bytes:
                    issues.append(f"3D model relationship references missing part: {source} -> {target}")

        names_by_id: dict[str, str] = {}
        settings_data = member_bytes.get("Metadata/model_settings.config")
        plate_count = None
        if settings_data:
            try:
                settings = ET.fromstring(settings_data)
                for obj in children(settings, "object"):
                    name = next((meta.attrib.get("value", "") for meta in children(obj, "metadata")
                                 if meta.attrib.get("key") == "name"), None)
                    if name:
                        names_by_id[obj.attrib.get("id", "")] = name
                plate_count = len(children(settings, "plate")) or None
            except ET.ParseError as exc:
                issues.append(f"malformed Bambu model settings: {exc}")
        instance_counts = Counter(names_by_id.get(object_id, f"object:{object_id}")
                                  for object_id, _, printable in valid_builds if printable)

        instances: list[dict[str, Any]] = []
        def expand(node: tuple[str, str], accumulated: list[list[float]], root_id: str,
                   part_name: str, active: set[tuple[str, str]], build_index: int,
                   transform_chain: list[list[list[float]]], depth: int = 0) -> None:
            if depth > MAX_GRAPH_DEPTH:
                return
            if node in active:
                return
            active = active | {node}
            obj = docs[node[0]]["objects"][node[1]]
            if obj["mesh"] is not None:
                stats = obj["mesh"]
                if stats.get("mesh_status") == "PASS":
                    instances.append({"build_object_id": root_id, "part_name": part_name,
                                      "mesh_path": node[0], "mesh_object_id": node[1],
                                      "unit_declared": obj["unit"],
                                      "unit_effective": obj["effective_unit"],
                                      "transform": manifest_matrix(accumulated),
                                      "transform_chain": transform_chain,
                                      "bounds_mm": transform_bounds(stats["bounds"], accumulated),
                                      "bounds": transform_bounds(stats["bounds"], accumulated)})
            for child, component_transform, unit_ratio in graph.get(node, []):
                effective_component_transform = multiply(component_transform, uniform_scale(unit_ratio))
                expand(child, multiply(accumulated, effective_component_transform), root_id, part_name, active,
                       build_index, transform_chain + [manifest_matrix(component_transform)], depth + 1)

        for build_index, (object_id, item_transform, printable) in enumerate(valid_builds):
            if printable:
                root_unit_to_mm = docs["3D/3dmodel.model"]["unit_to_mm"]
                expand(("3D/3dmodel.model", object_id),
                       multiply(uniform_scale(root_unit_to_mm), item_transform), object_id,
                       names_by_id.get(object_id, f"object:{object_id}"), set(), build_index,
                       [manifest_matrix(item_transform)])

        main_objects = docs["3D/3dmodel.model"]["objects"]
        unreferenced_ids = sorted(object_id for object_id in main_objects
                                  if ("3D/3dmodel.model", object_id) not in reachable)
        used_parts = {part for part, _ in reachable}
        unreferenced_parts = sorted(path for path in model_paths
                                    if path != "3D/3dmodel.model" and path not in used_parts)
        mesh_failed = any(record["mesh"].get("mesh_status") != "PASS" for record in mesh_records)
        failed = bool(issues) or mesh_failed
        meshless_containers = sum(1 for node in reachable
                                  if docs[node[0]]["objects"][node[1]]["mesh"] is None
                                  and graph.get(node))
        relationship_targets = {target for mapping in all_relationships.values() for target in mapping.values()}
        redundant_model_rels = sorted(path for path in relationship_targets if path not in used_parts)
        graph_objects = []
        for part, document in sorted(docs.items()):
            for object_id, obj in sorted(document["objects"].items()):
                graph_objects.append({"part_path": part, "object_id": object_id,
                    "kind": "mesh" if obj["mesh"] is not None else ("component_container" if obj["components"] else "empty"),
                    "component_count": len(obj["components"]),
                    "unit_declared": obj["unit"], "unit_effective": obj["effective_unit"],
                    "referenced_by_printable_build": (part, object_id) in reachable,
                    "mesh_status": obj["mesh"].get("mesh_status") if obj["mesh"] is not None else None})
        rel_report = []
        for source, mapping in sorted(all_relationships.items()):
            for rel_id, target in sorted(mapping.items()):
                rel_report.append({"source_part": source, "relationship_id": rel_id, "target_part": target,
                                   "target_found": target in member_bytes, "used_by_printable_build": target in used_parts})
        rel_report.extend({"source_part": "_rels/.rels", "relationship_id": rel_id, "target_part": target,
                           "target_found": target in member_bytes, "used_by_printable_build": target in used_parts,
                           "primary_model": target == "3D/3dmodel.model"}
                          for rel_id, target in sorted(root_rels.items()))
        analysis = {
            "package_status": "FAIL" if failed else "PASS",
            "graph_status": "FAIL" if issues else "PASS",
            "mesh_checks_pass": not mesh_failed,
            "unit_declared": docs["3D/3dmodel.model"]["unit"],
            "unit_effective": docs["3D/3dmodel.model"]["effective_unit"],
            "unit_source": "declared" if docs["3D/3dmodel.model"]["unit"] else "3MF default",
            "model_part_units": {part: {"declared": doc["unit"],
                                         "effective": doc["effective_unit"],
                                         "source": "declared" if doc["unit"] else "3MF default"}
                                 for part, doc in sorted(docs.items())},
            "resource_object_count": len(main_objects),
            "object_count_all_parts": sum(len(doc["objects"]) for doc in docs.values()),
            "mesh_object_count": len(mesh_records),
            "meshless_container_count": meshless_containers,
            "build_instance_count": len(build_items),
            "printable_build_instance_count": sum(1 for _, _, printable in valid_builds if printable),
            "mesh_instance_count": len(instances),
            "named_instance_counts": dict(sorted(instance_counts.items())),
            "instances": instances,
            "build_items": build_items_report,
            "graph_objects": graph_objects,
            "component_references": component_references,
            "model_relationships": rel_report,
            "primary_model_metadata": model_metadata.get("3D/3dmodel.model", {}),
            "plate_count": plate_count,
            "unreferenced_resource_object_ids": unreferenced_ids,
            "unreferenced_package_parts": unreferenced_parts,
            "relationship_targets_not_used_by_components": redundant_model_rels,
            "issues": sorted(set(issues)),
            "mesh_file_count": len(mesh_records),
            "distinct_mesh_model_part_hash_count": len({r["sha256"] for r in members
                                                          if r["path"] in {m["path"] for m in mesh_records}}),
            "package_member_count": len(members),
        }
        # Attach each object's mesh result to its part member without treating duplicate hashes as failure.
        stats_by_part = {(record["path"], record["object_id"]): record["mesh"] for record in mesh_records}
        for record in members:
            if record["path"] in model_paths:
                try:
                    model_root = ET.fromstring(member_bytes[record["path"]])
                    object_rows = []
                    for resource in children(next((el for el in model_root.iter() if local_name(el) == "resources"), ET.Element("resources")), "object"):
                        object_id = resource.attrib.get("id")
                        if (record["path"], object_id) in stats_by_part:
                            object_rows.append({"object_id": object_id, "mesh": stats_by_part[(record["path"], object_id)]})
                    if object_rows:
                        record["objects"] = object_rows
                        if len(object_rows) == 1:
                            record["mesh"] = object_rows[0]["mesh"]
                except ET.ParseError:
                    pass
        return analysis, members
    except (ET.ParseError, ValueError, KeyError, IndexError) as exc:
        if isinstance(exc, VerificationError):
            raise
        raise VerificationError(f"invalid 3MF model structure: {exc}") from exc


def inspect_archive(path: Path, extract_dir: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    if path.stat().st_size > MAX_MEMBER_BYTES:
        raise VerificationError(f"archive exceeds {MAX_MEMBER_BYTES} bytes: {path}")
    archive_record = {"path": path.name, "format": FORMATS.get(path.suffix.lower(), "OTHER"),
                      "size_bytes": path.stat().st_size, "sha256": sha256_file(path),
                      "provenance": "local_upstream_unverified"}
    try:
        with zipfile.ZipFile(path) as zf:
            infos = validate_zip_metadata(zf)
            members = []
            resolved_destination = extract_dir.resolve()
            for info in sorted(infos, key=lambda item: item.filename):
                if info.is_dir():
                    continue
                relative = safe_member_path(info.filename)
                content = read_checked(zf, info)
                out = extract_dir.joinpath(*relative.parts)
                if not out.resolve().is_relative_to(resolved_destination):
                    raise VerificationError(f"extraction escapes destination: {info.filename}")
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(content)
                ext = Path(info.filename).suffix.lower()
                record: dict[str, Any] = {"path": info.filename, "size_bytes": len(content),
                    "format": FORMATS.get(ext, "OTHER"), "sha256": sha256(content),
                    "provenance": "member_of_local_archive"}
                if ext == ".3mf":
                    details, package_members = inspect_3mf(content)
                    record["analysis"] = details
                    record["package_members"] = package_members
                members.append(record)
    except zipfile.BadZipFile as exc:
        raise VerificationError(f"invalid ZIP archive {path.name}: {exc}") from exc
    archive_record["archive_status"] = "PASS"
    return archive_record, members


def inventory(upstream: Path, extract_dir: Path) -> dict[str, Any]:
    source = upstream.resolve()
    destination = extract_dir.resolve()
    if source == destination or source.is_relative_to(destination) or destination.is_relative_to(source):
        raise VerificationError("extraction directory must not overlap the upstream source tree")
    files = sorted(path for path in upstream.rglob("*") if path.is_file() or path.is_symlink())
    records = []
    for path in files:
        if path.is_symlink():
            raise VerificationError(f"symlink in upstream source tree is not allowed: {path}")
        ext = path.suffix.lower()
        if ext == ".zip":
            archive, members = inspect_archive(path, extract_dir / path.stem)
            records.append({"archive": archive, "members": members})
        else:
            size = path.stat().st_size
            file_record: dict[str, Any] = {"path": path.relative_to(upstream).as_posix(),
                "format": FORMATS.get(ext, "OTHER"), "size_bytes": size,
                "sha256": sha256_file(path), "provenance": "local_upstream_unverified"}
            record: dict[str, Any] = {"file": file_record}
            if ext == ".3mf":
                if size > MAX_MEMBER_BYTES:
                    raise VerificationError(f"3MF file exceeds {MAX_MEMBER_BYTES} bytes: {path}")
                details, package_members = inspect_3mf(path.read_bytes())
                file_record["analysis"] = details
                record["package_members"] = package_members
            records.append(record)
    seen: Counter[str] = Counter()
    for row in records:
        top = row.get("file") or row.get("archive")
        seen[top["sha256"]] += 1
        for nested in row.get("package_members", []):
            seen[nested["sha256"]] += 1
        for member in row.get("members", []):
            seen[member["sha256"]] += 1
            for nested in member.get("package_members", []):
                seen[nested["sha256"]] += 1
    return {"schema_version": 1, "scope": "assets/3d/upstream", "records": records,
            "exact_duplicate_hashes": sorted(digest for digest, count in seen.items() if count > 1),
            "limitations": ["3MF relationships, units, transforms, mesh topology and references are inspected without geometry repair.",
                            "Only 3MF mesh geometry is parsed; standalone STL/STEP/IGES and other CAD payloads are hashed but not decoded.",
                            "No physical fit, self-intersection, mesh orientation, slicer acceptance, or redistribution permission is asserted."]}


def has_failures(result: dict[str, Any]) -> bool:
    for record in result["records"]:
        file_record = record.get("file", {})
        if file_record.get("analysis", {}).get("package_status") == "FAIL":
            return True
        archive = record.get("archive")
        if archive and archive.get("archive_status") != "PASS":
            return True
        for member in record.get("members", []):
            analysis = member.get("analysis", {})
            if analysis.get("package_status") == "FAIL":
                return True
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream", type=Path, required=True)
    parser.add_argument("--extract-dir", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--check-manifest", action="store_true", help="compare generated JSON with existing manifest")
    args = parser.parse_args(argv)
    try:
        result = inventory(args.upstream, args.extract_dir)
        encoded = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        failed = has_failures(result)
        if args.check_manifest:
            existing = args.manifest.read_text(encoding="utf-8")
            if existing != encoded:
                print("FAIL: manifest differs from current upstream inventory", file=sys.stderr)
                return 1
            if failed:
                print("FAIL: manifest is deterministic but verification findings remain", file=sys.stderr)
                return 1
            print("PASS: manifest hashes and inventory match current upstream")
        else:
            args.manifest.parent.mkdir(parents=True, exist_ok=True)
            args.manifest.write_text(encoded, encoding="utf-8")
            print(f"{'FAIL' if failed else 'PASS'}: wrote {args.manifest}")
        return 1 if failed else 0
    except (OSError, VerificationError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
