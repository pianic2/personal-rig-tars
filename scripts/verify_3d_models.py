#!/usr/bin/env python3
"""Inventory and statically inspect protected upstream 3D archives.

Only Python's standard library is required. Extracted files must be directed to
a disposable working directory; this script never writes into the input tree.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
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
MAX_MEMBER = 512 * 1024 * 1024


class VerificationError(ValueError):
    """Unsafe or invalid input archive."""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_member_path(name: str) -> PurePosixPath:
    """Reject traversal, absolute paths, drive paths and ambiguous separators."""
    if "\\" in name or "\x00" in name:
        raise VerificationError(f"unsafe archive path: {name!r}")
    path = PurePosixPath(name)
    if path.is_absolute() or not path.parts or any(p in ("", ".", "..") for p in path.parts):
        raise VerificationError(f"unsafe archive path: {name!r}")
    if path.parts[0].endswith(":"):
        raise VerificationError(f"unsafe archive path: {name!r}")
    return path


def read_checked(zf: zipfile.ZipFile, info: zipfile.ZipInfo) -> bytes:
    safe_member_path(info.filename)
    mode = info.external_attr >> 16
    if stat.S_ISLNK(mode):
        raise VerificationError(f"symlink archive member not allowed: {info.filename}")
    if info.file_size > MAX_MEMBER:
        raise VerificationError(f"archive member exceeds size limit: {info.filename}")
    try:
        data = zf.read(info)
    except (zipfile.BadZipFile, RuntimeError, OSError) as exc:
        raise VerificationError(f"cannot read {info.filename}: {exc}") from exc
    if len(data) != info.file_size:
        raise VerificationError(f"size mismatch for {info.filename}")
    return data


def mesh_stats(xml_data: bytes) -> dict[str, Any]:
    root = ET.fromstring(xml_data)
    unit = root.attrib.get("unit")
    vertices: list[tuple[float, float, float]] = []
    triangles: list[tuple[int, int, int]] = []
    for mesh in root.iter():
        if mesh.tag.rsplit("}", 1)[-1] != "mesh":
            continue
        for child in mesh:
            tag = child.tag.rsplit("}", 1)[-1]
            if tag == "vertices":
                for v in child:
                    vertices.append(tuple(float(v.attrib[k]) for k in ("x", "y", "z")))
            elif tag == "triangles":
                for t in child:
                    triangles.append(tuple(int(t.attrib[k]) for k in ("v1", "v2", "v3")))
    if not vertices or not triangles:
        raise VerificationError("3MF model contains no mesh vertices or triangles")
    if any(not math.isfinite(c) for v in vertices for c in v):
        raise VerificationError("mesh has non-finite vertex coordinates")
    if any(i < 0 or i >= len(vertices) for tri in triangles for i in tri):
        raise VerificationError("mesh triangle references an invalid vertex")
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
            if sum(x*x for x in cross) <= 1e-24:
                degenerate += 1
        for x, y in ((a, b), (b, c), (c, a)):
            edges[tuple(sorted((x, y)))] += 1
    bounds = [[min(v[i] for v in vertices), max(v[i] for v in vertices)] for i in range(3)]
    counts = Counter(edges.values())
    duplicate_triangles = len(triangles) - len({tuple(sorted(tri)) for tri in triangles})
    return {
        "unit_declared": unit,
        "vertex_count": len(vertices), "triangle_count": len(triangles),
        "bounds": bounds, "degenerate_triangle_count": degenerate,
        "duplicate_triangle_count": duplicate_triangles,
        "edge_incidence": {str(k): counts[k] for k in sorted(counts)},
        "watertight_by_edge_count": bool(edges) and all(n == 2 for n in edges.values()),
        "manifold_by_edge_count": bool(edges) and all(n <= 2 for n in edges.values()),
        "mesh_status": "FAIL" if degenerate or duplicate_triangles else "PASS",
    }


def inspect_3mf(data: bytes) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    try:
        from io import BytesIO
        with zipfile.ZipFile(BytesIO(data)) as zf:
            infos = zf.infolist()
            names: set[str] = set()
            for info in infos:
                path = safe_member_path(info.filename)
                if info.filename in names:
                    raise VerificationError(f"duplicate archive path: {info.filename}")
                names.add(info.filename)
                if not info.is_dir():
                    read_checked(zf, info)
            model_info = next((i for i in infos if i.filename == "3D/3dmodel.model"), None)
            if model_info is None:
                raise VerificationError("3MF is missing 3D/3dmodel.model")
            model_bytes = read_checked(zf, model_info)
            root = ET.fromstring(model_bytes)
            ns = {"c": "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"}
            unit = root.attrib.get("unit")
            objects = []
            for obj in root.findall(".//c:resources/c:object", ns):
                mesh = obj.find("c:mesh", ns)
                comps = obj.find("c:components", ns)
                objects.append({"object_id": obj.attrib.get("id"),
                                "kind": "mesh" if mesh is not None else "component_container",
                                "component_count": len(list(comps)) if comps is not None else 0})
            build = root.find("c:build", ns)
            instances = []
            if build is not None:
                instances = [item.attrib.get("objectid") for item in build.findall("c:item", ns)]
            names_by_id: dict[str, str] = {}
            if "Metadata/model_settings.config" in names:
                settings = ET.fromstring(read_checked(zf, zf.getinfo("Metadata/model_settings.config")))
                for obj in settings.findall("object"):
                    for meta in obj.findall("metadata"):
                        if meta.attrib.get("key") == "name":
                            names_by_id[obj.attrib.get("id", "")] = meta.attrib.get("value", "")
            instance_counts = Counter(names_by_id.get(obj_id, f"object:{obj_id}") for obj_id in instances)
            plate_count = None
            if "Metadata/model_settings.config" in names:
                settings_for_plates = ET.fromstring(read_checked(zf, zf.getinfo("Metadata/model_settings.config")))
                plate_count = len(settings_for_plates.findall("plate")) or None
            if "Metadata/project_settings.config" in names:
                try:
                    project_settings = json.loads(read_checked(zf, zf.getinfo("Metadata/project_settings.config")))
                    plate_values = project_settings.get("plateList") or project_settings.get("plates")
                    if isinstance(plate_values, list):
                        plate_count = len(plate_values)
                except (json.JSONDecodeError, UnicodeDecodeError):
                    plate_count = None
            member_records = []
            for info in sorted(infos, key=lambda x: x.filename):
                if info.is_dir():
                    continue
                member_data = read_checked(zf, info)
                record: dict[str, Any] = {"path": info.filename, "size_bytes": info.file_size,
                                          "sha256": sha256(member_data)}
                has_mesh = any(el.tag.rsplit("}", 1)[-1] == "mesh" for el in ET.fromstring(member_data).iter()) if info.filename.endswith(".model") else info.filename.endswith(".stl")
                if info.filename.startswith("3D/") and has_mesh:
                    try:
                        record["mesh"] = mesh_stats(member_data)
                    except (ET.ParseError, UnicodeDecodeError, KeyError, ValueError) as exc:
                        record["mesh"] = {"mesh_status": "FAIL", "error": str(exc)}
                member_records.append(record)
            return ({"package_status": "PASS", "unit_declared": unit,
                     "resource_object_count": len(objects), "objects": objects,
                     "build_instance_count": len(instances), "build_instances": instances,
                     "named_instance_counts": dict(sorted(instance_counts.items())),
                     "plate_count": plate_count,
                     "mesh_file_count": sum("mesh" in r for r in member_records),
                     "component_file_count": sum(r["path"].startswith("3D/Objects/") for r in member_records),
                     "distinct_mesh_hash_count": len({r["sha256"] for r in member_records if "mesh" in r}),
                     "mesh_checks_pass": all(r.get("mesh", {}).get("mesh_status") == "PASS" for r in member_records if "mesh" in r),
                     "package_member_count": len(member_records)}, member_records)
    except (zipfile.BadZipFile, ET.ParseError, OSError) as exc:
        raise VerificationError(f"invalid 3MF package: {exc}") from exc


def inspect_archive(path: Path, extract_dir: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    raw = path.read_bytes()
    archive_record = {"path": path.name, "format": FORMATS.get(path.suffix.lower(), "OTHER"),
                      "size_bytes": len(raw), "sha256": sha256(raw), "provenance": "local_upstream_unverified"}
    try:
        with zipfile.ZipFile(path) as zf:
            if zf.testzip() is not None:
                raise VerificationError("archive CRC test failed")
            members = []
            seen_paths: set[str] = set()
            for info in sorted(zf.infolist(), key=lambda x: x.filename):
                rel = safe_member_path(info.filename)
                if info.filename in seen_paths:
                    raise VerificationError(f"duplicate archive path: {info.filename}")
                seen_paths.add(info.filename)
                if info.is_dir():
                    continue
                data = read_checked(zf, info)
                out = extract_dir.joinpath(*rel.parts)
                # resolve() check prevents a pre-existing symlink in the work dir escaping it.
                if not out.resolve().is_relative_to(extract_dir.resolve()):
                    raise VerificationError(f"extraction escapes destination: {info.filename}")
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(data)
                ext = Path(info.filename).suffix.lower()
                record: dict[str, Any] = {"path": info.filename, "size_bytes": len(data),
                    "format": FORMATS.get(ext, "OTHER"), "sha256": sha256(data),
                    "provenance": "member_of_local_archive"}
                if ext == ".3mf":
                    details, package_members = inspect_3mf(data)
                    record["analysis"] = details
                    record["package_members"] = package_members
                members.append(record)
            archive_record["archive_status"] = "PASS"
            return archive_record, members
    except zipfile.BadZipFile as exc:
        raise VerificationError(f"invalid ZIP archive {path.name}: {exc}") from exc


def inventory(upstream: Path, extract_dir: Path) -> dict[str, Any]:
    source = upstream.resolve()
    destination = extract_dir.resolve()
    if source == destination or source.is_relative_to(destination) or destination.is_relative_to(source):
        raise VerificationError("extraction directory must not overlap the upstream source tree")
    files = sorted(p for p in upstream.rglob("*") if p.is_file())
    records = []
    for path in files:
        ext = path.suffix.lower()
        if ext == ".zip":
            archive, members = inspect_archive(path, extract_dir / path.stem)
            records.append({"archive": archive, "members": members})
        else:
            data = path.read_bytes()
            records.append({"file": {"path": path.relative_to(upstream).as_posix(),
                "format": FORMATS.get(ext, "OTHER"), "size_bytes": len(data),
                "sha256": sha256(data), "provenance": "local_upstream_unverified"}})
    seen: Counter[str] = Counter()
    for row in records:
        file = row.get("file") or row.get("archive")
        seen[file["sha256"]] += 1
        for member in row.get("members", []):
            seen[member["sha256"]] += 1
            for package_member in member.get("package_members", []):
                seen[package_member["sha256"]] += 1
    duplicates = sorted(h for h, n in seen.items() if n > 1)
    return {"schema_version": 1, "scope": "assets/3d/upstream", "records": records,
            "exact_duplicate_hashes": duplicates,
            "limitations": ["3MF metadata/mesh topology inspected without geometry repair.",
                "Only 3MF units are explicit when declared; other CAD formats are not parsed.",
                "No official MakerWorld download or physical fit test is asserted."]}


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
        if args.check_manifest:
            existing = args.manifest.read_text(encoding="utf-8")
            if existing != encoded:
                print("FAIL: manifest differs from current upstream inventory", file=sys.stderr)
                return 1
            print("PASS: manifest hashes and inventory match current upstream")
        else:
            args.manifest.parent.mkdir(parents=True, exist_ok=True)
            args.manifest.write_text(encoded, encoding="utf-8")
            print(f"PASS: wrote {args.manifest}")
        return 0
    except (OSError, VerificationError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
