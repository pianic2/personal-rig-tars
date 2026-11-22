# RTARS-16 — ESP-IDF target and board configuration evidence

Issue: https://niccolopiazzi01.atlassian.net/browse/RTARS-16  
Captured: 2026-11-22 (Europe/Rome)  
Source: local ESP-IDF configuration log, sanitized before publication.  
Upstream: https://github.com/LuwuDynamics/rig_omni  
Upstream commit: `c2b42cd73ef65f5cd2a158d6949f0273869454dc`  
ESP-IDF: `v5.5.3`

## AC verification

| Acceptance criterion | Evidence | Result |
| --- | --- | --- |
| ESP32-S3 target | `CONFIG_IDF_TARGET="esp32s3"` | PASS |
| RIG-Tars board | `CONFIG_BOARD_TYPE_TARS=y` | PASS |
| Overseas region | `CONFIG_FIRMWARE_REGION_OVERSEAS=y` | PASS |
| Saved configuration | `sdkconfig` exists and is nonempty; SHA-256 below | PASS |
| ESP-IDF reconfiguration | CMake configure and generate completed | PASS |

Original local `sdkconfig` SHA-256 (integrity reference only, not a copy of the configuration):
```text
92d934afdeefe36cffc4d8161a257177275f8d193ce44d3ba08fb252fb04e3ea
```

## Selected sanitized log excerpts

```text
=== TOOLCHAIN ===
ESP-IDF v5.5.3
=== UPSTREAM ===
c2b42cd73ef65f5cd2a158d6949f0273869454dc
=== AC1 | TARGET ===
CONFIG_IDF_TARGET="esp32s3"
=== AC2 | BOARD ===
CONFIG_BOARD_TYPE_TARS=y
=== AC2 | REGION ===
CONFIG_FIRMWARE_REGION_OVERSEAS=y
=== CONFIG VALIDATION ===
Executing action: reconfigure
-- Board [tars] version: 3.8.0
-- Building ESP-IDF components for target esp32s3
-- App "rig-tars" version: 3.8.0
-- Using overseas wificonfig.eaf
-- Including Hey Kira wake word model in staging
-- Configuring done (57.0s)
-- Generating done (1.2s)
=== FINAL VERIFICATION ===
CONFIG_IDF_TARGET="esp32s3"
CONFIG_FIRMWARE_REGION_OVERSEAS=y
CONFIG_BOARD_TYPE_TARS=y
=== RESULT ===
RTARS-16 CONFIG CHECKS: PASS
```

## Non-blocking configuration diagnostics

- Kconfig warns that selection of the `BT_NIMBLE_ENABLED` choice by `PUPPY_ENABLE_BLE_CONTROL` has no effect.
- Kconfig warns that `USE_ESP_BLUFI_WIFI_PROVISIONING=y` attempts to select `BT_BLE_BLUFI_ENABLE` and `BT_BLE_42_FEATURES_SUPPORTED` despite unsatisfied Bluetooth/Bludroid dependencies.
- `CONFIG_NEWLIB_NANO_FORMAT` in upstream defaults is renamed to `CONFIG_LIBC_NEWLIB_NANO_FORMAT`.
- CMake reported optional ZLIB and PNG host libraries unavailable. Reconfiguration nevertheless completed.

These diagnostics were observed during configuration; they are **not** evidence of a successful firmware build, flash, or hardware test.

## Privacy and provenance

The original unredacted log remains local. This published evidence intentionally excludes usernames, home directories, absolute paths, temporary directory names, Python environment paths, and the exhaustive component-path dump. The upstream URL, commit SHA, toolchain version, chosen configuration symbols, and configuration checksum are retained for reproducibility. The complete `sdkconfig` is **not** committed because it has not undergone a line-by-line secrets audit.
