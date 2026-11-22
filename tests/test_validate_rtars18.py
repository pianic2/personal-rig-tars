#!/usr/bin/env python3
"""Offline regression tests for RTARS-18 manifest and provenance validation."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/validate_rtars18.py"
spec = importlib.util.spec_from_file_location("validate_rtars18", SCRIPT)
assert spec and spec.loader
import sys
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class TestRtars18(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.build = Path(self.tmp.name)
        self.files = {
            "bootloader/bootloader.bin": (0x0, 16256),
            "partition_table/partition-table.bin": (0x8000, 3072),
            "ota_data_initial.bin": (0xD000, 8192),
            "rig-tars.bin": (0x20000, 3951136),
            "board_assets.bin": (0x800000, 2380815),
        }
        for rel in self.files:
            p = self.build / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            # Small dummy image sizes, no production firmware involved.
            p.write_bytes(b"A" * 16)

    def manifest(self, entries=None, prefix="--flash_mode dio --flash_freq 80m --flash_size 16MB"):
        pairs = entries if entries is not None else [
            (offset, rel) for rel, (offset, _) in self.files.items()
        ]
        self.path = self.build / "flash_args"
        self.path.write_text(prefix + " " + " ".join(f"0x{offset:X} {rel}" for offset, rel in pairs))
        return self.path

    def test_valid_five_images(self):
        images = module.image_arguments(self.manifest(), self.build)
        self.assertEqual(len(images), 5)
        self.assertTrue(module.image_ranges_valid(images))

    def test_missing_ota_image_rejected(self):
        entries = [(o, r) for r, (o, _) in self.files.items()
                   if r != "ota_data_initial.bin"]
        with self.assertRaises(ValueError):
            module.image_arguments(self.manifest(entries), self.build)

    def test_extra_image_rejected(self):
        entries = [(o, r) for r, (o, _) in self.files.items()]
        entries.append((0x300000, "extra.bin"))
        with self.assertRaises(ValueError):
            module.image_arguments(self.manifest(entries), self.build)

    def test_duplicate_image_rejected(self):
        entries = [(o, r) for r, (o, _) in self.files.items()]
        entries[-1] = entries[0]
        with self.assertRaises(ValueError):
            module.image_arguments(self.manifest(entries), self.build)

    def test_offset_tampering_rejected(self):
        entries = [(o + 0x1000 if r == "ota_data_initial.bin" else o, r)
                   for r, (o, _) in self.files.items()]
        with self.assertRaises(ValueError):
            module.image_arguments(self.manifest(entries), self.build)

    def test_unexpected_option_rejected(self):
        with self.assertRaises(ValueError):
            module.image_arguments(self.manifest(prefix="--erase-all yes"), self.build)

    def test_manifest_path_traversal_rejected(self):
        entries = [(o, "../rig-tars.bin" if r == "rig-tars.bin" else r)
                   for r, (o, _) in self.files.items()]
        with self.assertRaises(ValueError):
            module.image_arguments(self.manifest(entries), self.build)

    def test_images_do_not_overlap(self):
        images = module.image_arguments(self.manifest(), self.build)
        self.assertTrue(module.image_ranges_valid(images))
        # OTA partition exactly 8192 bytes: an overflowing OTA image is rejected.
        (self.build / "ota_data_initial.bin").write_bytes(b"x" * 8193)
        self.assertFalse(module.image_ranges_valid(images))

    def test_partition_human_readable_sizes(self):
        self.assertEqual(module.parse_partition_number("16K"), 0x4000)
        self.assertEqual(module.parse_partition_number("8M"), 0x800000)
        self.assertEqual(module.parse_partition_number("0x410000"), 0x410000)
        self.assertFalse(module.partition_layout_matches("nvs,data,nvs,0x9000,16K"))

    def test_source_partition_csv(self):
        data = """# Name,Type,SubType,Offset,Size,Flags
nvs,data,nvs,0x9000,16K,
otadata,data,ota,0xd000,8K,
phy_init,data,phy,0xf000,4K,
tars_err,data,nvs,0x10000,16K,
ota_0,app,ota_0,0x20000,0x3f0000,
ota_1,app,ota_1,0x410000,0x3f0000,
assets,data,spiffs,0x800000,8M,
"""
        self.assertTrue(module.partition_layout_matches(data))
        self.assertFalse(module.partition_layout_matches(data.replace("0x410000", "0x420000")))

    def test_forged_incomplete_marker_rejected(self):
        sdk = self.build / "sdkconfig"
        sdk.write_text("CONFIG_BOARD_TYPE_TARS=y\n")
        lock = self.build / "dependencies.lock"
        lock.write_text("dependencies: {}\n")
        marker = self.build / ".rtars18-validation.json"
        marker.write_text(json.dumps({
            "source_commit": module.UPSTREAM_SHA,
            "sdkconfig_sha256": module.sha256(sdk),
            "dependencies_lock_sha256": module.sha256(lock),
            "artifacts": {"rig-tars.bin": module.sha256(self.build / "rig-tars.bin")},
        }))
        self.assertFalse(module.reusable_build(marker, self.build, sdk, lock))


if __name__ == "__main__":
    unittest.main()
