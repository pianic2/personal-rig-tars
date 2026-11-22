#!/usr/bin/env python3
"""RTARS-30: regenerate the two Bambu Studio process presets from an original ZIP.

No third-party dependencies. Does not modify the original archive.
Usage: python3 tools/manufacturing/rebuild_rtars30_presets.py "Process presets.zip" output-dir
"""
import hashlib
import json
import pathlib
import sys
import zipfile

SOURCES = [
    ("HL-18 QUALITY 0.20mm @Elegoo Neptune4 0.4 nozzle.json",
     "RTARS-AESTHETIC-CANDIDATE-0.16mm@Elegoo-Neptune4-0.4.json",
     "RTARS-AESTHETIC CANDIDATE 0.16mm @Elegoo Neptune4 0.4 nozzle",
     {"layer_height": "0.16"},
     "d1de21d70d9146e16a79656243147c75295e3930dd79bdadab5c5b7741c6ece8"),
    ("PLA_DIAGNOSTIC_CONSERVATIVE 0.20mm @Elegoo Neptune4 0.4 nozzle.json",
     "RTARS-FUNCTIONAL-CANDIDATE-0.20mm@Elegoo-Neptune4-0.4.json",
     "RTARS-FUNCTIONAL CANDIDATE 0.20mm @Elegoo Neptune4 0.4 nozzle",
     {},
     "3493204d0bd54ac68945e28208d2c294cd1e08be1f99b952b525a0f487c6d38d"),
]
SOURCE_SHA256 = "26f41f13772589bdeb85dbb3520e3a09d85a93c722a14ac493b4700f354d13ae"


def sha256(blob: bytes) -> str:
    return hashlib.sha256(blob).hexdigest()


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: rebuild_rtars30_presets.py SOURCE.zip OUTPUT_DIR")
    source = pathlib.Path(sys.argv[1])
    outdir = pathlib.Path(sys.argv[2])
    if sha256(source.read_bytes()) != SOURCE_SHA256:
        raise SystemExit("FAIL: unexpected input archive SHA-256; refusing to generate")
    pending = []
    with zipfile.ZipFile(source) as archive:
        for filename, dest, name, changes, expected_hash in SOURCES:
            original = json.loads(archive.read(filename))
            assert original.get("name") == filename[:-5], "Unexpected source process preset"
            assert "layer_height" in original and "print_settings_id" in original, "Missing process preset keys"
            assert len(original) == 280, "Unexpected process export field count"
            output = {**original, "name": name, "print_settings_id": name, **changes}
            assert len(output) == len(original), "Unexpected change in field count"
            changed = {k for k in original if original[k] != output[k]}
            assert changed == {"name", "print_settings_id", *changes}, "Unexpected changed fields"
            blob = (json.dumps(output, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
            if sha256(blob) != expected_hash:
                raise SystemExit(f"FAIL: output SHA mismatch: {dest}")
            pending.append((dest, blob))
    outdir.mkdir(parents=True, exist_ok=True)
    for filename, blob in pending:
        (outdir / filename).write_bytes(blob)
        print(f"PASS {filename}: {sha256(blob)}")


if __name__ == "__main__":
    main()
