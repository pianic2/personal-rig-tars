# RTARS-18 — USB serial port association

Date: 2026-11-22. Origin: operator-supplied terminal output. Sanitized before publication; no host paths, usernames, serial numbers, MAC addresses or device-unique hardware identifiers retained.

## Two-snapshot physical association

A baseline snapshot was collected **with the RIG-TARS USB cable unplugged**; a second snapshot was collected after connecting the robot, using Python `serial.tools.list_ports`.

| Observation | Outcome |
| --- | --- |
| USB serial device count before plugging in | 0 |
| New serial USB device after connecting TARS | one `ttyACM*` interface |
| USB vendor/product ID (non-unique) | `1A86:55D3` |
| Additional/removed serial USB devices | No ambiguity reported |
| Association of added serial port with physically connected TARS | **PASS** |
| ESP32-S3 bootloader communication | **FAIL (earlier esptool attempt: no serial data / download sync failure)** |
| Identified flash chip size | **NOT TESTED** |
| Flash/erase | **NOT TESTED** |

Note: USB serial enumeration and cable association establish the attached serial adapter, **not** successful ESP32-S3 ROM communications. Port names are represented generically because they may change between hosts. No firmware writes or resets performed during this USB association check.

This report contains only non-unique USB vendor/product identifiers and generic device-class names.
