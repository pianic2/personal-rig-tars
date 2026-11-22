# RTARS-18 — Powered ESP32-S3 chip and flash-capacity probe

Date: 2026-11-22. Evidence source: operator-provided sanitized output from read-only `esptool` probes on their Debian host. This is **operator-observed evidence**, not a direct hardware execution by the assistant. No unique identifier or personal information is retained.

## Preconditions and change in conditions
- Before corrective action: USB serial bridge enumerated as WCH CH343, while `esptool chip_id` returned `NO_SERIAL_DATA`; controller switch was ON but the battery was disconnected.
- The official TARS assembly instructions call for the kit-specified battery connected, power switched on and USB data cable connected during firmware flashing.
- After the operator proceeded to the **powered** diagnostic, the probe results below were reported. The before/after result supports an **inadequate target-power / power-arrangement hypothesis**, without establishing a measured electrical root cause.

## Sanitized results

| Check | Operator-observed result |
| --- | --- |
| CH343 USB serial adapter present | **PASS** |
| `esptool --chip esp32s3 chip_id` | **PASS** |
| `esptool --chip esp32s3 flash_id` | **PASS** |
| Flash capacity reported | **16 MB** |
| At least 16 MB flash capacity | **PASS** |
| Flash write, erase, boot/recovery exercise | **NOT TESTED** |

The complete console output provided by the operator was:
```text
=== RTARS-18 | POWERED CHIP DIAGNOSTIC ===
PASS: CH343 USB adapter detected
PASS: chip_id
PASS: flash_id
FLASH CAPACITY: 16 MB
PASS: 16MB requirement
=== END DIAGNOSTIC ===
```

## Boundaries
The esptool commands communicate with the target and may reset the MCU, but **do not write or erase flash**. The successful chip and flash-id commands confirm that the physical target is now reachable using the selected ESP32-S3 protocol, and reports adequate flash size; they do **not** validate flashed firmware version, installed OTA selection or runtime behavior.

Sources:
- [Official TARS assembly procedure](https://wiki.xgorobot.com/kb/pet-tars/ce146b389ed40020944a3aef7)
- [Espressif esptool ESP32-S3 troubleshooting](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/troubleshooting.html)
- [RTARS-18 power/bootloader documentary research](official-power-bootloader-research-2026-11-22.md)

**Anonymization:** no host paths, usernames, MAC addresses, serial numbers, eFuse identities or unique device IDs.
