# RTARS-19 — Firmware baseline build evidence

Issue: https://niccolopiazzi01.atlassian.net/browse/RTARS-19

- Source: https://github.com/LuwuDynamics/rig_omni
- Upstream commit: `c2b42cd73ef65f5cd2a158d6949f0273869454dc`
- Build timestamp: 2026-11-22T17:10:58+01:00
- ESP-IDF: v5.5.3
- Compiler: xtensa-esp-elf-gcc 14.2.0 (esp-14.2.0_20251107)
- Target: esp32s3; board: tars 3.8.0
- Build result: PASS, exit code 0
- Flash: NOT PERFORMED as part of RTARS-19
- Output: rig-tars.bin SHA-256 `7efd1514bed279a690a817c9a54cce1f1f73bc0fc1eecb48e7caa989dc070185`

Files: `toolchain.txt`, `result.txt`, `sha256.txt` are transcribed from the supplied anonymized evidence. The complete sanitized `build.log` is archived here (2,838 lines, 307,648 bytes, SHA-256 `5f40794605bedce22a82c2a830b5fe29046f736900aaa359e4b39f93bf68216b`). `build-summary.log` remains a labeled, abridged excerpt for quick review.

Privacy: original workstation paths replaced with `<HOME>`, `<ESP_IDF_ROOT>` and `<PROJECT_ROOT>` in excerpt. Do not upload non-sanitized source log.

**Acceptance evidence**: complete sanitized build log, build result, toolchain version and SHA-256 manifests are archived under this directory. No binary firmware payloads were committed.
