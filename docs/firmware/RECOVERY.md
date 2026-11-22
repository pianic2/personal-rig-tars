# RTARS-18 — Controlled firmware recovery

**Scope:** documented troubleshooting only. Recovery not performed on hardware. Keep the robot supported and actuators clear before any reset or write.

| Symptom | Non-destructive investigation | Escalation |
| --- | --- | --- |
| No serial port | USB data cable, power, device enumeration/permissions, other serial processes | Try known-good cable/port; follow ESP32-S3 download-mode instructions for the actual board |
| Cannot connect | Verify chip/port, close monitor, inspect boot log, safe reset into download mode | Retry chip query with conservative baud rate |
| Firmware boots but assets missing | Read serial errors; compare board, region, firmware/asset checksums | Reflash *matched* asset image after checking installed partition layout |
| Boot loop/invalid partition | Inspect logs, check flash package and generated offsets, check chip flash capacity | Reflash a verified full official matched regional package |
| Wrong edition / malfunction after update | Record version, preserve logs and recoverable settings | Reinstall the intended official edition |
| Failed/interrupted flash | Do not keep power cycling during a write; collect esptool errors, ensure reliable USB/power | Retry complete write with validated build-specific `flash_args` |

## Order of operations
1. Photograph/record symptoms without sharing Wi-Fi credentials, BLE identities, raw device identifiers or personal data.
2. Confirm firmware family (`rig_tars_rl` vs `rig_omni`), version, board model, region, package provenance and SHA-256.
3. Identify serial port; run read-only `python -m esptool --chip esp32s3 -p "$PORT" chip_id` (data should be sanitized).
4. Inspect logs using `idf.py monitor` or upstream `tools/tars_log/tars_serial.py status`/`errors`; exit monitor before other serial operations.
5. If recoverable without destructive writes, prefer configuration/connection repair.
6. If reflash is necessary, use [FLASHING.md](FLASHING.md) with the exact verified package. Recheck partition offsets and images.
7. Validate fresh boot, firmware identity, asset rendering and safe basic functions; record PASS/FAIL per check.

## Reset distinctions
The dedicated TARS 3.8.1 README documents a **top touch key held through a 10-second countdown** to clear Wi-Fi **and calibration**. Do **not** use that reset as a routine network fix: losing calibration may affect safe movement. It is distinct from MCU reset, ESP32-S3 download mode and flash erase. The latter can destroy NVS/calibration and error history.

`erase_flash` is intentionally **not included** as a routine recovery step. A full erase requires explicit approval, a documented data-loss assessment and a known restoration path. Never infer OTA recovery from the mere presence of two OTA partitions.

Official source: https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/README.md ; serial tool: https://github.com/LuwuDynamics/rig_tars_rl/blob/456e3ee95ccbe94deae9484568719e8686b4b68b/tools/tars_log/README.md
