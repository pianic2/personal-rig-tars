"""Unit tests for verify_3d_models.py: python3 -m unittest scripts/test_verify_3d_models.py"""

import io
import json
import tempfile
import unittest
import zipfile
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from io import StringIO
from unittest import mock

from scripts.verify_3d_models import (VerificationError, inspect_3mf, inspect_archive, inventory,
                                      main, safe_member_path, sha256, validate_content_types)


MODEL = b'''<?xml version="1.0"?><model xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" unit="millimeter"><resources><object id="1" type="model"><mesh><vertices><vertex x="0" y="0" z="0"/><vertex x="1" y="0" z="0"/><vertex x="0" y="1" z="0"/></vertices><triangles><triangle v1="0" v2="1" v3="2"/></triangles></mesh></object></resources><build><item objectid="1"/></build></model>'''


def make_3mf() -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>')
        zf.writestr("_rels/.rels", '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="root" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel" Target="/3D/3dmodel.model"/></Relationships>')
        zf.writestr("3D/3dmodel.model", MODEL)
        zf.writestr("Metadata/readme.txt", b"fixture")
    return stream.getvalue()


def package_3mf(root_objects, build_items, parts=(), *, main_relationships=None, extra_files=(), root_unit="millimeter"):
    core = "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
    prod = "http://schemas.microsoft.com/3dmanufacturing/production/2015/06"
    unit_attr = f' unit="{root_unit}"' if root_unit is not None else ""
    model = (f'<model xmlns="{core}" xmlns:p="{prod}"{unit_attr} requiredextensions="p">'
             f'<resources>{root_objects}</resources><build>{build_items}</build></model>')
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>')
        zf.writestr("_rels/.rels", '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="root" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel" Target="/3D/3dmodel.model"/></Relationships>')
        zf.writestr("3D/3dmodel.model", model)
        if main_relationships is None:
            main_relationships = [f'<Relationship Id="r{i}" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel" Target="{path}"/>' for i, (path, _) in enumerate(parts, 1)]
        zf.writestr("3D/_rels/3dmodel.model.rels", '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' + "".join(main_relationships) + '</Relationships>')
        zf.writestr("Metadata/model_settings.config", '<config><plate/><object id="1"><metadata key="name" value="fixture"/></object></config>')
        for path, content in parts:
            zf.writestr(path.lstrip("/"), content)
        for path, content in extra_files:
            zf.writestr(path, content)
    return stream.getvalue()


def mesh_model(object_id="1", *, vertices='<vertex x="0" y="0" z="0"/><vertex x="1" y="0" z="0"/><vertex x="0" y="1" z="0"/>', triangles='<triangle v1="0" v2="1" v3="2"/>'):
    core = "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
    return (f'<model xmlns="{core}" unit="millimeter"><resources><object id="{object_id}" type="model"><mesh>'
            f'<vertices>{vertices}</vertices><triangles>{triangles}</triangles></mesh></object></resources><build/></model>')


class VerifyModelTests(unittest.TestCase):
    def test_sha256_is_stable(self):
        self.assertEqual(sha256(b"abc"), "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

    def test_rejects_malformed_or_wrong_model_content_types(self):
        with self.assertRaisesRegex(VerificationError, "malformed 3MF content types"):
            validate_content_types(b"<Types>", ["3D/3dmodel.model"])
        wrong = (b'<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                 b'<Default Extension="model" ContentType="text/xml"/></Types>')
        with self.assertRaisesRegex(VerificationError, "invalid 3D model content type"):
            validate_content_types(wrong, ["3D/3dmodel.model"])

    def test_rejects_path_traversal_and_absolute_paths(self):
        for name in ("../escape.stl", "/tmp/escape.stl", "C:/escape.stl", "a\\..\\escape.stl"):
            with self.subTest(name=name), self.assertRaises(VerificationError):
                safe_member_path(name)

    def test_rejects_malformed_archive(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / "bad.zip"
            archive.write_bytes(b"not a zip")
            with self.assertRaises(VerificationError):
                inspect_archive(archive, Path(tmp) / "out")

    def test_rejects_unsafe_member_before_extraction(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / "unsafe.zip"
            with zipfile.ZipFile(archive, "w") as zf:
                zf.writestr("../escape.stl", b"protected")
            with self.assertRaises(VerificationError):
                inspect_archive(archive, Path(tmp) / "out")
            self.assertFalse((Path(tmp) / "escape.stl").exists())

    def test_refuses_extraction_inside_upstream(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "upstream"
            source.mkdir()
            with self.assertRaises(VerificationError):
                inventory(source, source / "extracted")

    def test_rejects_symlink_in_upstream(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "upstream"
            source.mkdir()
            outside = Path(tmp) / "outside.stl"
            outside.write_bytes(b"not geometry")
            (source / "linked.stl").symlink_to(outside)
            with self.assertRaisesRegex(VerificationError, "symlink"):
                inventory(source, Path(tmp) / "extract")

    def test_finds_exact_duplicate_member_content_and_extracts(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / "models.zip"
            with zipfile.ZipFile(archive, "w") as zf:
                zf.writestr("part-a.stl", b"identical")
                zf.writestr("part-b.stl", b"identical")
            record, members = inspect_archive(archive, Path(tmp) / "out")
            self.assertEqual(record["archive_status"], "PASS")
            self.assertEqual(members[0]["sha256"], members[1]["sha256"])
            self.assertEqual((Path(tmp) / "out/part-a.stl").read_bytes(), b"identical")

    def test_parses_3mf_units_meshes_and_instances(self):
        data = make_3mf()
        details, members = inspect_3mf(data)
        self.assertEqual(details["unit_declared"], "millimeter")
        self.assertEqual(details["build_instance_count"], 1)
        mesh = next(row["mesh"] for row in members if "mesh" in row)
        self.assertEqual(mesh["triangle_count"], 1)
        self.assertEqual(mesh["mesh_status"], "PASS")
        self.assertFalse(mesh["watertight_by_edge_count"])

    def test_resolves_valid_component_container_and_multiple_instances(self):
        part_path = "/3D/Objects/leaf.model"
        component = f'<object id="1" type="model"><components><component p:path="{part_path}" objectid="1"/></components></object>'
        data = package_3mf(component, '<item objectid="1"/><item objectid="1"/>',
                           [(part_path, mesh_model())])
        analysis, _ = inspect_3mf(data)
        self.assertEqual(analysis["package_status"], "PASS")
        self.assertEqual(analysis["mesh_instance_count"], 2)
        self.assertEqual(analysis["meshless_container_count"], 1)
        self.assertEqual(analysis["unreferenced_package_parts"], [])

    def test_applies_composed_component_and_build_transforms_to_bounds(self):
        path = "/3D/Objects/leaf.model"
        root = f'<object id="1" type="model"><components><component p:path="{path}" objectid="1" transform="1 0 0 0 1 0 0 0 1 2 0 0"/></components></object>'
        build = '<item objectid="1" transform="0 1 0 -1 0 0 0 0 1 10 0 0"/>'
        analysis, _ = inspect_3mf(package_3mf(root, build, [(path, mesh_model())]))
        self.assertEqual(analysis["instances"][0]["bounds"], [[9.0, 10.0], [2.0, 3.0], [0.0, 0.0]])

    def test_applies_model_part_unit_conversion_to_instance_bounds(self):
        path = "/3D/Objects/leaf.model"
        root = (f'<object id="1" type="model"><components><component p:path="{path}" objectid="1" '
                'transform="1 0 0 0 1 0 0 0 1 10 0 0"/></components></object>')
        inch_mesh = mesh_model().replace('unit="millimeter"', 'unit="inch"')
        analysis, _ = inspect_3mf(package_3mf(root, '<item objectid="1"/>', [(path, inch_mesh)]))
        self.assertEqual(analysis["instances"][0]["bounds_mm"], [[10.0, 35.4], [0.0, 25.4], [0.0, 0.0]])
        self.assertEqual(analysis["component_references"][0]["target_to_source_unit_scale"], 25.4)

    def test_records_spec_default_unit_when_not_declared(self):
        analysis, _ = inspect_3mf(package_3mf(
            '<object id="1" type="model"><mesh><vertices><vertex x="0" y="0" z="0"/>'
            '<vertex x="1" y="0" z="0"/><vertex x="0" y="1" z="0"/></vertices>'
            '<triangles><triangle v1="0" v2="1" v3="2"/></triangles></mesh></object>',
            '<item objectid="1"/>', root_unit=None))
        self.assertIsNone(analysis["unit_declared"])
        self.assertEqual(analysis["unit_effective"], "millimeter")
        self.assertEqual(analysis["unit_source"], "3MF default")

    def test_marks_missing_object_reference_fail(self):
        root = '<object id="1" type="model"><components><component objectid="99"/></components></object>'
        analysis, _ = inspect_3mf(package_3mf(root, '<item objectid="1"/>'))
        self.assertEqual(analysis["package_status"], "FAIL")
        self.assertTrue(any("missing object" in issue for issue in analysis["issues"]))

    def test_marks_component_cycle_fail(self):
        root = '<object id="1" type="model"><components><component objectid="1"/></components></object>'
        analysis, _ = inspect_3mf(package_3mf(root, '<item objectid="1"/>'))
        self.assertEqual(analysis["graph_status"], "FAIL")
        self.assertTrue(any("cycle" in issue for issue in analysis["issues"]))

    def test_caps_excessive_component_graph_depth(self):
        objects = "".join(
            f'<object id="{index}" type="model"><components><component objectid="{index + 1}"/></components></object>'
            for index in range(1, 515))
        objects += ('<object id="515" type="model"><mesh><vertices>'
                    '<vertex x="0" y="0" z="0"/><vertex x="1" y="0" z="0"/>'
                    '<vertex x="0" y="1" z="0"/></vertices><triangles>'
                    '<triangle v1="0" v2="1" v3="2"/></triangles></mesh></object>')
        analysis, _ = inspect_3mf(package_3mf(objects, '<item objectid="1"/>'))
        self.assertEqual(analysis["package_status"], "FAIL")
        self.assertTrue(any("maximum depth" in issue for issue in analysis["issues"]))

    def test_marks_cycle_across_model_parts_fail(self):
        path_a, path_b = "/3D/Objects/a.model", "/3D/Objects/b.model"
        model_a = ('<model xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" '
                   'xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06"><resources>'
                   f'<object id="1" type="model"><components><component p:path="{path_b}" objectid="1"/>'
                   '</components></object></resources></model>')
        model_b = ('<model xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" '
                   'xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06"><resources>'
                   f'<object id="1" type="model"><components><component p:path="{path_a}" objectid="1"/>'
                   '</components></object></resources></model>')
        rels = [f'<Relationship Id="a" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel" Target="{path_a}"/>',
                f'<Relationship Id="b" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel" Target="{path_b}"/>']
        rel_type = "http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"
        rel_a = f'<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="b" Type="{rel_type}" Target="b.model"/></Relationships>'
        rel_b = f'<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="a" Type="{rel_type}" Target="a.model"/></Relationships>'
        analysis, _ = inspect_3mf(package_3mf(
            '<object id="1" type="model"><components><component objectid="1"/></components></object>',
            '<item objectid="1"/>', [(path_a, model_a), (path_b, model_b)],
            main_relationships=rels,
            extra_files=[("3D/Objects/_rels/a.model.rels", rel_a),
                         ("3D/Objects/_rels/b.model.rels", rel_b)]))
        self.assertEqual(analysis["graph_status"], "FAIL")
        self.assertTrue(any("cycle" in issue for issue in analysis["issues"]))

    def test_malformed_model_xml_is_error_not_pass(self):
        data = package_3mf('', '<item objectid="1"/>')
        with zipfile.ZipFile(io.BytesIO(data)) as source:
            entries = [(info.filename, source.read(info)) for info in source.infolist()]
        malformed = io.BytesIO()
        with zipfile.ZipFile(malformed, "w", zipfile.ZIP_DEFLATED) as target:
            for name, content in entries:
                target.writestr(name, b"<model><broken>" if name == "3D/3dmodel.model" else content)
        with self.assertRaises(VerificationError):
            inspect_3mf(malformed.getvalue())

    def test_rejects_duplicate_archive_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / "duplicate.zip"
            with zipfile.ZipFile(archive, "w") as zf:
                zf.writestr("same.stl", b"a")
                zf.writestr("same.stl", b"b")
            with self.assertRaisesRegex(VerificationError, "duplicate archive path"):
                inspect_archive(archive, Path(tmp) / "out")

    def test_rejects_symlink_archive_member(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / "symlink.zip"
            info = zipfile.ZipInfo("link.stl")
            info.create_system = 3
            info.external_attr = (0o120777 << 16)
            with zipfile.ZipFile(archive, "w") as zf:
                zf.writestr(info, b"target")
            with self.assertRaisesRegex(VerificationError, "symlink"):
                inspect_archive(archive, Path(tmp) / "out")

    def test_marks_missing_relationship_and_target_fail(self):
        path = "/3D/Objects/missing.model"
        root = f'<object id="1" type="model"><components><component p:path="{path}" objectid="1"/></components></object>'
        rels = []
        analysis, _ = inspect_3mf(package_3mf(root, '<item objectid="1"/>', main_relationships=rels))
        self.assertEqual(analysis["package_status"], "FAIL")
        self.assertTrue(analysis["issues"])

    def test_lists_unreferenced_resource_and_package_part_without_failing(self):
        path = "/3D/Objects/leaf.model"
        root = (f'<object id="1" type="model"><components><component p:path="{path}" objectid="1"/></components></object>'
                '<object id="2" type="model"><mesh><vertices><vertex x="0" y="0" z="0"/><vertex x="1" y="0" z="0"/><vertex x="0" y="1" z="0"/></vertices><triangles><triangle v1="0" v2="1" v3="2"/></triangles></mesh></object>')
        empty = '<model xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02"><resources/><build/></model>'
        analysis, _ = inspect_3mf(package_3mf(root, '<item objectid="1"/>', [(path, mesh_model()), ("/3D/Objects/unused.model", empty)]))
        self.assertEqual(analysis["package_status"], "PASS")
        self.assertIn("2", analysis["unreferenced_resource_object_ids"])
        self.assertIn("3D/Objects/unused.model", analysis["unreferenced_package_parts"])

    def test_invalid_mesh_sets_mesh_and_package_fail(self):
        path = "/3D/Objects/leaf.model"
        root = f'<object id="1" type="model"><components><component p:path="{path}" objectid="1"/></components></object>'
        bad_mesh = mesh_model(triangles='<triangle v1="0" v2="1" v3="99"/>')
        analysis, members = inspect_3mf(package_3mf(root, '<item objectid="1"/>', [(path, bad_mesh)]))
        self.assertEqual(analysis["package_status"], "FAIL")
        self.assertEqual(analysis["mesh_checks_pass"], False)
        self.assertTrue(any(m.get("mesh", {}).get("mesh_status") == "FAIL" for m in members))

    def test_cli_propagates_mesh_failure_and_writes_evidence(self):
        bad = package_3mf(
            '<object id="1" type="model"><mesh><vertices><vertex x="0" y="0" z="0"/>'
            '<vertex x="1" y="0" z="0"/><vertex x="0" y="1" z="0"/></vertices>'
            '<triangles><triangle v1="0" v2="1" v3="9"/></triangles></mesh></object>',
            '<item objectid="1"/>')
        with tempfile.TemporaryDirectory() as tmp:
            upstream = Path(tmp) / "upstream"
            upstream.mkdir()
            with zipfile.ZipFile(upstream / "source.zip", "w") as zf:
                zf.writestr("bad.3mf", bad)
            manifest = Path(tmp) / "manifest.json"
            with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                result = main(["--upstream", str(upstream), "--extract-dir", str(Path(tmp) / "out"),
                               "--manifest", str(manifest)])
            self.assertEqual(result, 1)
            evidence = json.loads(manifest.read_text())
            self.assertEqual(evidence["records"][0]["members"][0]["analysis"]["package_status"], "FAIL")

    def test_rejects_zip_bomb_by_uncompressed_budget_before_extract(self):
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("large.dat", b"x" * 2048)
        with tempfile.TemporaryDirectory() as tmp, mock.patch("scripts.verify_3d_models.MAX_UNCOMPRESSED_BYTES", 1024):
            archive = Path(tmp) / "bomb.zip"
            archive.write_bytes(stream.getvalue())
            with self.assertRaises(VerificationError):
                inspect_archive(archive, Path(tmp) / "out")
            self.assertFalse((Path(tmp) / "out").exists())

    def test_manifest_is_deterministic_across_extraction_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            upstream = Path(tmp) / "upstream"
            upstream.mkdir()
            with zipfile.ZipFile(upstream / "fixture.zip", "w") as zf:
                zf.writestr("model.3mf", make_3mf())
            one = inventory(upstream, Path(tmp) / "extract-one")
            two = inventory(upstream, Path(tmp) / "extract-two")
            self.assertEqual(json.dumps(one, sort_keys=True), json.dumps(two, sort_keys=True))

    def test_inventories_standalone_3mf_as_model_not_opaque_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            upstream = Path(tmp) / "upstream"
            upstream.mkdir()
            (upstream / "model.3mf").write_bytes(make_3mf())
            result = inventory(upstream, Path(tmp) / "extract")
            file_record = result["records"][0]["file"]
            self.assertEqual(file_record["analysis"]["package_status"], "PASS")
            self.assertTrue(result["records"][0]["package_members"])


if __name__ == "__main__":
    unittest.main()
