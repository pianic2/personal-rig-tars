#!/usr/bin/env python3
"""Safely validate a pinned RIG-TARS source build; flashing is opt-in."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

UPSTREAM_URL = "https://github.com/LuwuDynamics/rig_tars_rl.git"
UPSTREAM_SHA = "456e3ee95ccbe94deae9484568719e8686b4b68b"
# Exact five-image ESP-IDF manifest observed in the operator's TARS Global build.
EXPECTED_IMAGES = {
    "bootloader.bin": (0x0, 0x8000),
    "partition-table.bin": (0x8000, 0x9000),
    "ota_data_initial.bin": (0xD000, 0xF000),
    "rig-tars.bin": (0x20000, 0x410000),
    "board_assets.bin": (0x800000, 0x1000000),
}
# Limited ESP-IDF esptool flash flags; unknown options fail closed.
FLASH_OPTIONS = {"--flash_mode", "--flash_freq", "--flash_size", "--spi-connection"}
REQUIRED_ARTIFACTS = {
    "flash_args", "bootloader/bootloader.bin",
    "partition_table/partition-table.bin", "ota_data_initial.bin",
    "rig-tars.bin", "board_assets.bin",
}
EXPECTED_TARGET = "esp32s3"
EXPECTED_BOARD = "CONFIG_BOARD_TYPE_TARS=y"
EXPECTED_REGION = "CONFIG_FIRMWARE_REGION_OVERSEAS=y"
FLASH_PHRASE = "FLASH RTARS-18 TARS GLOBAL"


@dataclass
class Check:
    name: str
    result: str
    detail: str


def run(argv: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(argv, cwd=cwd, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, check=False)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def add(checks: list[Check], name: str, result: str, detail: str) -> None:
    checks.append(Check(name, result, detail))


def get_serial_ports() -> list[tuple[str, str]] | None:
    try:
        from serial.tools import list_ports  # type: ignore[import-not-found]
    except ImportError:
        return None
    try:
        return [(port.device, port.description or "USB serial") for port in list_ports.comports()]
    except (AttributeError, OSError):
        return None


def image_arguments(flash_args: Path, build_dir: Path) -> list[tuple[int, Path]]:
    """Parse all manifest arguments, reject extra images/options and escaped paths."""
    tokens = shlex.split(flash_args.read_text(encoding="utf-8"))
    images: list[tuple[int, Path]] = []
    names: set[str] = set()
    index = 0
    # Options must precede images and have a single value.
    while index < len(tokens) and tokens[index].startswith("--"):
        option = tokens[index]
        if option not in FLASH_OPTIONS or index + 1 >= len(tokens):
            raise ValueError("unrecognized or incomplete flash option")
        value = tokens[index + 1]
        if value.startswith("--") or value.startswith("0x"):
            raise ValueError("invalid flash option value")
        index += 2
    if (len(tokens) - index) != 2 * len(EXPECTED_IMAGES):
        raise ValueError("unexpected image count or trailing manifest tokens")
    while index < len(tokens):
        address, relative = tokens[index:index + 2]
        if not re.fullmatch(r"0[xX][0-9a-fA-F]+", address):
            raise ValueError("invalid flash address")
        if Path(relative).is_absolute() or ".." in Path(relative).parts:
            raise ValueError("flash image path escapes build directory")
        candidate = (build_dir / relative).resolve()
        if not candidate.is_relative_to(build_dir.resolve()):
            raise ValueError("flash image path resolves outside build directory")
        name = candidate.name
        if name not in EXPECTED_IMAGES or name in names:
            raise ValueError("unexpected or duplicate flash image")
        offset = int(address, 16)
        if offset != EXPECTED_IMAGES[name][0]:
            raise ValueError("flash image offset mismatch")
        names.add(name)
        images.append((offset, candidate))
        index += 2
    if names != set(EXPECTED_IMAGES):
        raise ValueError("missing required flash images")
    return images


def image_ranges_valid(images: list[tuple[int, Path]]) -> bool:
    intervals: list[tuple[int, int]] = []
    for offset, path in images:
        if not path.is_file() or path.stat().st_size <= 0:
            return False
        end = offset + path.stat().st_size
        if end > EXPECTED_IMAGES[path.name][1]:
            return False
        intervals.append((offset, end))
    intervals.sort()
    return all(left[1] <= right[0] for left, right in zip(intervals, intervals[1:]))


def parse_partition_number(value: str) -> int:
    """Decode ESP-IDF CSV offsets and sizes, including KiB/MiB suffixes."""
    match = re.fullmatch(r"(0[xX][0-9A-Fa-f]+|[0-9]+)\s*([KMG]?)B?", value.strip(), re.I)
    if not match:
        raise ValueError("invalid partition number")
    number = int(match.group(1), 0) if match.group(1).lower().startswith("0x") else int(match.group(1))
    return number * (1024 ** {"": 0, "K": 1, "M": 2, "G": 3}[match.group(2).upper()])


def partition_layout_matches(decoded_csv: str) -> bool:
    expected = {
        "nvs": (0x9000, 0x4000), "otadata": (0xD000, 0x2000),
        "phy_init": (0xF000, 0x1000), "tars_err": (0x10000, 0x4000),
        "ota_0": (0x20000, 0x3F0000), "ota_1": (0x410000, 0x3F0000),
        "assets": (0x800000, 0x800000),
    }
    actual: dict[str, tuple[int, int]] = {}
    try:
        for row in csv.reader(decoded_csv.splitlines()):
            if len(row) < 5 or row[0].strip().startswith("#"):
                continue
            name = row[0].strip()
            if name in expected:
                if name in actual:
                    return False
                actual[name] = (parse_partition_number(row[3]), parse_partition_number(row[4]))
    except (ValueError, IndexError):
        return False
    return actual == expected


def reusable_build(marker_path: Path, build_dir: Path, sdkconfig: Path, lockfile: Path) -> bool:
    if not sdkconfig.is_file() or not lockfile.is_file() or not marker_path.is_file():
        return False
    try:
        marker = json.loads(marker_path.read_text(encoding="utf-8"))
        if (marker.get("source_commit") != UPSTREAM_SHA
                or marker.get("sdkconfig_sha256") != sha256(sdkconfig)
                or marker.get("dependencies_lock_sha256") != sha256(lockfile)):
            return False
        recorded = marker.get("artifacts")
        return (isinstance(recorded, dict)
                and set(recorded) == REQUIRED_ARTIFACTS
                and all(isinstance(digest, str)
                        and re.fullmatch(r"[a-f0-9]{64}", digest)
                        and (build_dir / rel).is_file()
                        and sha256(build_dir / rel) == digest
                        for rel, digest in recorded.items()))
    except (OSError, ValueError, TypeError):
        return False


def write_build_marker(marker_path: Path, build_dir: Path, sdkconfig: Path,
                       lockfile: Path, artifacts: list[Path]) -> None:
    manifest = {
        "source_commit": UPSTREAM_SHA,
        "sdkconfig_sha256": sha256(sdkconfig),
        "dependencies_lock_sha256": sha256(lockfile),
        "artifacts": {str(path.relative_to(build_dir)): sha256(path) for path in artifacts},
    }
    marker_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def redact_path(value: Path, roots: list[Path]) -> str:
    resolved = value.resolve()
    for root in roots:
        try:
            return str(resolved.relative_to(root.resolve()))
        except ValueError:
            continue
    return "<external-path>"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True,
                        help="local rig_tars_rl checkout (must be the pinned commit)")
    parser.add_argument("--region", choices=("gb",), default="gb",
                        help="validated build profile (only Global/English is supported)")
    parser.add_argument("--build", action="store_true", help="run idf.py build if artifacts are absent")
    parser.add_argument("--build-dir", type=Path, help="build directory; defaults to build/packages/tars-gb")
    parser.add_argument("--probe", action="store_true",
                        help="run read-only chip_id and flash_id on an explicitly selected detected device")
    parser.add_argument("--flash", action="store_true", help="write the validated manifest to the detected device")
    parser.add_argument("--confirm", default="", help=f"required with --flash: {FLASH_PHRASE!r}")
    parser.add_argument("--port", help="explicit serial port; must match a detected device")
    args = parser.parse_args()

    repo = args.source.resolve()
    root = Path(__file__).resolve().parents[1]
    build_dir = (args.build_dir or repo / "build/packages/tars-gb").resolve()
    sdkconfig = repo / "build/package-configs/sdkconfig.tars-gb"
    checks: list[Check] = []
    fatal = False
    python_exe = shutil.which("python3") or sys.executable

    git = shutil.which("git")
    idf = shutil.which("idf.py")
    add(checks, "git available", "PASS" if git else "FAIL", "git executable detected" if git else "git missing")
    add(checks, "ESP-IDF available", "PASS" if idf else "FAIL", "idf.py detected" if idf else "idf.py missing")

    if not repo.is_dir():
        add(checks, "upstream checkout", "FAIL", "source directory not found")
        fatal = True
    else:
        revision = run([git, "-C", str(repo), "rev-parse", "HEAD"]) if git else None
        actual = revision.stdout.strip() if revision else ""
        good = bool(revision and revision.returncode == 0 and actual == UPSTREAM_SHA)
        add(checks, "dedicated upstream revision", "PASS" if good else "FAIL",
            "pinned rig_tars_rl revision verified" if good else "expected pinned rig_tars_rl commit; no rig_omni fallback")
        fatal |= not good
        if git:
            dirty = run([git, "-C", str(repo), "status", "--porcelain"]) if git else None
            status_lines = dirty.stdout.splitlines() if dirty else []
            permitted_lock = all(line[3:] == "dependencies.lock" and line.startswith("?? ")
                                 for line in status_lines)
            clean = bool(dirty and dirty.returncode == 0 and (not status_lines or permitted_lock))
            add(checks, "upstream working tree", "PASS" if clean else "FAIL",
                "clean except for generated dependency lock" if clean and status_lines else
                "clean" if clean else "modified or unreadable")
            fatal |= not clean

    idf_path = os.environ.get("IDF_PATH")
    add(checks, "IDF_PATH", "PASS" if idf_path and Path(idf_path).is_dir() else "FAIL",
        "ESP-IDF installation found" if idf_path and Path(idf_path).is_dir() else "unset or unavailable")
    if idf:
        version = run([idf, "--version"])
        version_ok = version.returncode == 0 and "5.5.3" in version.stdout
        add(checks, "ESP-IDF version", "PASS" if version_ok else "FAIL",
            "v5.5.3" if version_ok else "expected ESP-IDF v5.5.3")
        targets = run([idf, "--list-targets"])
        target_ok = targets.returncode == 0 and EXPECTED_TARGET in targets.stdout.split()
        add(checks, "ESP32-S3 target support", "PASS" if target_ok else "FAIL",
            "esp32s3 listed" if target_ok else "esp32s3 unavailable")
        fatal |= not version_ok or not target_ok
        idf_tools = Path(idf_path) / "tools/idf_tools.py" if idf_path else None
        tool_check = run([python_exe, str(idf_tools), "check"]) if idf_tools and idf_tools.is_file() else None
        tools_ok = bool(tool_check and tool_check.returncode == 0)
        add(checks, "ESP-IDF installed dependencies", "PASS" if tools_ok else "FAIL",
            "idf_tools.py check completed" if tools_ok else "ESP-IDF tool check missing or failed")
        fatal |= not tools_ok
    else:
        fatal = True

    required_tools = ("python3", "cmake", "ninja")
    missing_tools = [name for name in required_tools if not shutil.which(name)]
    add(checks, "build tools", "PASS" if not missing_tools else "FAIL",
        "python, cmake and ninja available" if not missing_tools else "missing: " + ", ".join(missing_tools))
    fatal |= bool(missing_tools)
    serial_tools_ok = importlib.util.find_spec("serial") is not None
    esptool_available = importlib.util.find_spec("esptool") is not None or shutil.which("esptool") is not None
    add(checks, "serial dependencies", "PASS" if serial_tools_ok and esptool_available else "FAIL",
        "pyserial and esptool available" if serial_tools_ok and esptool_available else
        "pyserial or esptool missing; port probe/flash unavailable")
    fatal |= (args.probe or args.flash) and not (serial_tools_ok and esptool_available)

    if repo.is_dir():
        config_source = repo / "configs/tars-gb.sdkconfig"
        if config_source.is_file():
            config_text = config_source.read_text(encoding="utf-8", errors="replace")
            config_ok = (f'CONFIG_IDF_TARGET="{EXPECTED_TARGET}"' in config_text
                         and EXPECTED_BOARD in config_text and EXPECTED_REGION in config_text
                         and 'CONFIG_ESPTOOLPY_FLASHSIZE="16MB"' in config_text)
            add(checks, "Global TARS configuration", "PASS" if config_ok else "FAIL",
                "ESP32-S3, TARS board and Global region profile verified" if config_ok else "profile symbols do not match expected Global TARS")
            fatal |= not config_ok
        else:
            add(checks, "Global TARS configuration", "FAIL", "configs/tars-gb.sdkconfig missing")
            fatal = True
        manifest = repo / "main/idf_component.yml"
        if manifest.is_file():
            manifest_text = manifest.read_text(encoding="utf-8", errors="replace")
            constraint_ok = bool(re.search(r"(?m)^\s+idf:\s*$", manifest_text)
                                 and re.search(r"(?m)^\s+version:\s*['\"]?>=5\.5\.2", manifest_text))
            add(checks, "component manifest", "PASS" if constraint_ok else "FAIL",
                "ESP-IDF >=5.5.2 constraint verified against required 5.5.3" if constraint_ok else "missing or incompatible ESP-IDF constraint")
            fatal |= not constraint_ok
        else:
            add(checks, "component manifest", "FAIL", "main/idf_component.yml missing")
            fatal = True
        if not sdkconfig.exists() and args.build and config_source.is_file():
            sdkconfig.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(config_source, sdkconfig)
        if sdkconfig.is_file():
            saved = sdkconfig.read_text(encoding="utf-8", errors="replace")
            saved_ok = (f'CONFIG_IDF_TARGET="{EXPECTED_TARGET}"' in saved and EXPECTED_BOARD in saved
                        and EXPECTED_REGION in saved and 'CONFIG_ESPTOOLPY_FLASHSIZE="16MB"' in saved)
            add(checks, "saved sdkconfig", "PASS" if saved_ok else "FAIL",
                "contains required target/board/region symbols" if saved_ok else "saved config differs from required profile")
            fatal |= not saved_ok
        else:
            result = "FAIL" if args.build or args.flash else "NOT TESTED"
            add(checks, "saved sdkconfig", result,
                "could not prepare package sdkconfig" if args.build or args.flash else "not materialized in dry-run; --build creates it from the pinned Global profile")
            fatal |= args.build or args.flash

    lockfile = repo / "dependencies.lock"
    marker_path = build_dir / ".rtars18-validation.json"
    build_reusable = reusable_build(marker_path, build_dir, sdkconfig, lockfile)
    prevalidated_build = build_reusable
    build_command_ok = build_reusable
    flash_args = next((path for path in (build_dir / "flash_args", build_dir / "flasher_args.json") if path.is_file()), None)
    if args.build and not build_reusable:
        if fatal:
            add(checks, "source build", "NOT TESTED", "preflight environment/source/configuration failed")
        else:
            cmd = [idf or "idf.py", "-B", str(build_dir), f"-DSDKCONFIG={sdkconfig}",
                   f"-DSDKCONFIG_DEFAULTS={repo / 'sdkconfig.defaults'};{repo / 'sdkconfig.defaults.esp32s3'}",
                   "-DIDF_TARGET=esp32s3", "build"]
            built = run(cmd, cwd=repo)
            add(checks, "source build", "PASS" if built.returncode == 0 else "FAIL",
                "idf.py build completed" if built.returncode == 0 else "idf.py build failed; raw output omitted from evidence")
            fatal |= built.returncode != 0
            build_command_ok = built.returncode == 0
            flash_args = next((path for path in (build_dir / "flash_args", build_dir / "flasher_args.json") if path.is_file()), None)
    elif build_reusable:
        add(checks, "source build", "PASS", "reusing provenance-marked build; source, config, lock and artifact hashes match")
    else:
        add(checks, "source build", "NOT TESTED", "no verified build provenance marker; pass --build to build")

    artifacts: list[tuple[str, Path]] = []
    manifest_images: list[tuple[int, Path]] = []
    if flash_args and flash_args.name == "flash_args":
        try:
            artifacts.append(("flash_args", flash_args))
            manifest_images = image_arguments(flash_args, build_dir)
            known_assets = {"board_assets.bin"}
            for offset, path in manifest_images:
                artifacts.append((f"image at 0x{offset:x}", path))
            all_exist = bool(manifest_images) and all(path.is_file() for _, path in manifest_images)
            add(checks, "flash_args", "PASS" if all_exist else "FAIL",
                "all manifest images exist" if all_exist else "manifest missing images or has no offset/image pairs")
            fatal |= not all_exist
            offsets_ok = (len(manifest_images) == len(EXPECTED_IMAGES)
                          and {path.name for _, path in manifest_images} == set(EXPECTED_IMAGES)
                          and all(EXPECTED_IMAGES[path.name][0] == offset
                                  for offset, path in manifest_images))
            add(checks, "manifest offsets", "PASS" if offsets_ok else "FAIL",
                "known TARS image offsets match source package profile" if offsets_ok else "image offset differs from TARS source profile")
            fatal |= not offsets_ok
            asset = next((path for _, path in manifest_images if path.name in known_assets), None)
            add(checks, "assets image", "PASS" if asset and asset.is_file() else "FAIL",
                "matching build assets image found" if asset and asset.is_file() else "build manifest has no TARS assets image")
            fatal |= not (asset and asset.is_file())
        except (OSError, ValueError):
            add(checks, "flash_args", "FAIL", "manifest could not be parsed")
            fatal = True
    elif flash_args:
        add(checks, "flash_args", "NOT TESTED", "JSON manifest format detected; inspect with upstream tooling before any write")
    else:
        add(checks, "flash_args", "NOT TESTED", "build manifest unavailable")

    try:
        import yaml  # type: ignore[import-not-found]
        lock_data = yaml.safe_load(lockfile.read_text(encoding="utf-8")) if lockfile.is_file() else None
        lock_ok = isinstance(lock_data, dict) and bool(lock_data.get("dependencies"))
    except Exception:
        lock_ok = False
    add(checks, "resolved dependency lock for writes", "PASS" if lock_ok else "NOT TESTED",
        "resolved component versions are pinned" if lock_ok else "no valid dependencies.lock; flash is blocked")
    if lock_ok:
        artifacts.append(("resolved component lock", lockfile))

    partition_bin = build_dir / "partition_table/partition-table.bin"
    if partition_bin.is_file():
        artifacts.append(("generated partition table", partition_bin))
        decoder = Path(idf_path) / "components/partition_table/gen_esp32part.py" if idf_path else None
        decoded = run([python_exe, str(decoder), str(partition_bin)]) if decoder and decoder.is_file() else None
        table_text = decoded.stdout if decoded and decoded.returncode == 0 else ""
        expected = decoded is not None and decoded.returncode == 0 and partition_layout_matches(table_text)
        add(checks, "generated partition table", "PASS" if expected else "FAIL",
            "decoded table contains expected TARS layout" if expected else "decode failed or layout differs from pinned CSV")
        fatal |= not expected
    else:
        add(checks, "generated partition table", "NOT TESTED", "partition-table.bin unavailable")

    if manifest_images and partition_bin.is_file():
        size_ok = image_ranges_valid(manifest_images)
        add(checks, "image sizes", "PASS" if size_ok else "FAIL",
            "all five images fit declared ranges without overlap" if size_ok else "image out of range, missing, empty or overlapping")
        fatal |= not size_ok
        add(checks, "artifact SHA-256", "PASS" if all(p.is_file() for _, p in artifacts) else "FAIL",
            "checksums calculated for available manifest images" if all(p.is_file() for _, p in artifacts) else "one or more images unavailable")
    else:
        add(checks, "image sizes", "NOT TESTED", "manifest and generated partition table required")
        add(checks, "artifact SHA-256", "NOT TESTED", "build artifacts unavailable")

    artifact_paths = list(dict.fromkeys(
        ([flash_args] if flash_args and flash_args.name == "flash_args" else [])
        + [path for _, path in manifest_images]
        + ([partition_bin] if partition_bin.is_file() else [])
    ))
    artifact_names = {str(p.relative_to(build_dir)) for p in artifact_paths
                      if p.is_relative_to(build_dir)}
    required_artifacts_ok = artifact_names == REQUIRED_ARTIFACTS
    required_checks = {"flash_args", "manifest offsets", "assets image", "generated partition table",
                       "image sizes", "artifact SHA-256", "resolved dependency lock for writes"}
    validated_artifacts = (required_artifacts_ok and all(path.is_file() for path in artifact_paths)
                           and required_checks <= {check.name for check in checks if check.result == "PASS"})
    if args.build and not build_reusable and build_command_ok and validated_artifacts and not fatal:
        try:
            write_build_marker(marker_path, build_dir, sdkconfig, lockfile, artifact_paths)
            build_reusable = True
            add(checks, "build provenance marker", "PASS", "local source/config/lock/artifact hashes recorded")
        except (OSError, ValueError):
            add(checks, "build provenance marker", "FAIL", "could not write local artifact provenance")
            fatal = True
    if args.flash and not build_reusable:
        fatal = True

    ports = get_serial_ports()
    detected = [device for device, _ in ports] if ports is not None else []
    port_result = "PASS" if ports else "NOT TESTED"
    port_detail = ("one or more serial interfaces detected; names withheld" if ports else
                   "pyserial unavailable; device enumeration not tested" if ports is None else
                   "no serial interface detected")
    add(checks, "serial port detection", port_result, port_detail)
    selected = None
    if args.port:
        try:
            requested = Path(args.port).resolve(strict=True)
            selected = next((device for device in detected
                             if Path(device).resolve(strict=True) == requested), None)
        except OSError:
            selected = None
    if args.port and not selected:
        add(checks, "requested serial port", "FAIL", "requested device is not currently detected")
        fatal = True
    if (args.probe or args.flash) and not (serial_tools_ok and esptool_available):
        add(checks, "chip interrogation", "FAIL", "pyserial/esptool dependency missing")
    elif args.probe or args.flash:
        if not selected:
            add(checks, "chip interrogation", "NOT TESTED", "requires an explicitly selected port that is currently detected")
        elif shutil.which("esptool") or python_exe:
            esptool = shutil.which("esptool")
            cmd_prefix = [esptool] if esptool else [python_exe, "-m", "esptool"]
            chip_query = run(cmd_prefix + ["--chip", "esp32s3", "-p", selected, "chip_id"])
            queried = run(cmd_prefix + ["--chip", "esp32s3", "-p", selected, "flash_id"]) if chip_query.returncode == 0 else chip_query
            capacity = re.search(r"Detected flash size:\s*(\d+)MB", queried.stdout, re.IGNORECASE)
            ok = chip_query.returncode == 0 and queried.returncode == 0 and capacity and int(capacity.group(1)) >= 16
            add(checks, "chip/flash interrogation", "PASS" if ok else "FAIL",
                "ESP32-S3 identified and flash capacity is at least 16 MiB" if ok else "read-only chip/flash query failed or capacity is insufficient; identifiers omitted")
            fatal |= not ok
        else:
            add(checks, "chip/flash interrogation", "FAIL", "esptool unavailable")
            fatal = True
    else:
        add(checks, "chip interrogation", "NOT TESTED", "read-only probe disabled; pass --probe to interrogate a detected serial device")

    if args.flash:
        preflight_ok = (not fatal and lock_ok and build_reusable and prevalidated_build
                        and flash_args and flash_args.name == "flash_args" and selected)
        if args.confirm != FLASH_PHRASE:
            print(f"Flash blocked: repeat with --confirm {shlex.quote(FLASH_PHRASE)} after reviewing the preflight report.", file=sys.stderr)
            preflight_ok = False
        if not preflight_ok:
            add(checks, "flash write", "FAIL", "blocked: required confirmation or preflight checks missing")
            fatal = True
        else:
            write = run([python_exe, "-m", "esptool", "--chip", "esp32s3",
                         "-p", selected, "-b", "460800", "--before", "default_reset", "--after", "hard_reset",
                         "write_flash", "@flash_args"], cwd=build_dir)
            add(checks, "flash write", "PASS" if write.returncode == 0 else "FAIL",
                "esptool write completed" if write.returncode == 0 else "esptool write failed; raw output omitted")
            fatal |= write.returncode != 0
    else:
        add(checks, "flash write", "NOT TESTED", "dry-run is the default; no device write was attempted")

    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    report_path = root / "evidence/RTARS-18/validation-report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# RTARS-18 automated validation", "", f"Generated: {generated}",
             "Mode: " + ("FLASH" if args.flash else "DRY-RUN"),
             f"Firmware source: `{UPSTREAM_URL}` at `{UPSTREAM_SHA}`; ESP-IDF v5.5.3; profile TARS Global/English.",
             "No raw command output, username, hostname, serial path, chip identifier, MAC, or credentials are recorded.", "",
             "| Check | Result | Sanitized detail |", "| --- | --- | --- |"]
    lines += [f"| {c.name} | **{c.result}** | {c.detail.replace('|', '¦')} |" for c in checks]
    lines += ["", "## Artifact manifest", "", "| Artifact | Bytes | SHA-256 |", "| --- | ---: | --- |"]
    found: set[Path] = set()
    for label, path in artifacts:
        if path in found:
            continue
        found.add(path)
        if path.is_file():
            lines.append(f"| {label} (`{redact_path(path, [repo, build_dir])}`) | {path.stat().st_size} | `{sha256(path)}` |")
    if not found:
        lines.append("| No validated build artifacts | — | — |")
    lines += ["", "A `NOT TESTED` result is not a pass. Do not close RTARS-18 while required evidence remains missing.",
              "The report is regenerated on each run; review it for accidental sensitive data before publishing.", ""]
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {report_path.relative_to(root)}")
    print("Checks: " + ", ".join(f"{c.name}={c.result}" for c in checks))
    return 1 if fatal else 0


if __name__ == "__main__":
    raise SystemExit(main())
