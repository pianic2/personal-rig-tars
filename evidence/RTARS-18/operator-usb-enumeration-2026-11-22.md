# RTARS-18 — Serial interface enumeration (operator evidence)

Date: 2026-11-22. Source: operator-provided sanitized serial-interface enumeration on the Debian workstation. No firmware write or chip query performed.

| Check | Result | Evidence |
| --- | --- | --- |
| Serial enumeration available | PASS | Python `serial.tools.list_ports` returned serial interfaces |
| USB serial adapter candidate detected | PASS | One `ttyACM*` device with USB vendor/product `1A86:55D3` |
| Candidate adapter family | INFORMATIONAL | VID:PID is consistent with WCH USB-serial CH343; this **does not identify the ESP32-S3** |
| Physical identification of TARS behind this adapter | NOT TESTED | Requires explicit device association / probe |
| ESP32-S3 identity, actual installed flash size | NOT TESTED | Requires opt-in `esptool` probe |
| Flash / erase | NOT TESTED | Not attempted |

Non-USB serial ports were also enumerated, but are excluded from the device candidate. Device names were generalized to avoid creating machine-specific instructions.

No user paths, hostnames, serial numbers, MAC addresses, physical chip identifiers or credentials included. Next step: inspect the active USB port on the operator host, then issue a read-only chip/flash-ID query with explicit permission; note that chip interrogation may automatically reset the controller.
