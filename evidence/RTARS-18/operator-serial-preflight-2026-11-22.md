# RTARS-18 — Serial-port preflight

Date: 2026-11-22. Source: terminal output supplied by operator. Sanitized: no username, host, absolute personal paths, serial number, MAC address, unique chip identifier, or credentials.

## Observations

| Check | Result |
| --- | --- |
| Candidate USB serial interface, previously physically associated with TARS | Present — PASS |
| Current-user read/write permission | PASS |
| `fuser` detection of processes occupying the serial interface | PASS — none detected |
| ESP32-S3 ROM loader synchronization | **FAIL** on prior read-only probe (`NO_SERIAL_DATA` / `DOWNLOAD_SYNC_FAILED`) |
| Chip/actual flash capacity | NOT TESTED |
| Flash/erase/physical recovery | NOT TESTED |

This preflight performs no reset, flash write, erase, or firmware modification. A free and accessible USB serial interface does not prove that the ESP32-S3 bootloader is in download mode or that UART wiring/reset control is operational.

Next action: identify the exact board's BOOT/GPIO0 and RESET/EN controls from physical markings or official board-specific documentation before attempting manual download mode. Do not substitute the application's top touch key or configuration-reset sequence.
