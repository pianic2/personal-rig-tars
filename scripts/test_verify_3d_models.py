"""Unit tests for verify_3d_models.py: python3 -m unittest scripts/test_verify_3d_models.py"""

import io
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.verify_3d_models import VerificationError, inspect_3mf, inspect_archive, inventory, safe_member_path, sha256


MODEL = b'''<?xml version="1.0"?><model xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" unit="millimeter"><resources><object id="1" type="model"><mesh><vertices><vertex x="0" y="0" z="0"/><vertex x="1" y="0" z="0"/><vertex x="0" y="1" z="0"/></vertices><triangles><triangle v1="0" v2="1" v3="2"/></triangles></mesh></object></resources><build><item objectid="1"/></build></model>'''


def make_3mf() -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("3D/3dmodel.model", MODEL)
        zf.writestr("Metadata/readme.txt", b"fixture")
    return stream.getvalue()


class VerifyModelTests(unittest.TestCase):
    def test_sha256_is_stable(self):
        self.assertEqual(sha256(b"abc"), "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

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


if __name__ == "__main__":
    unittest.main()
