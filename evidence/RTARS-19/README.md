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

Files: `toolchain.txt`, `result.txt`, `sha256.txt` are transcribed from the supplied anonymized evidence. `build-summary.log` is an explicitly abridged excerpt from a 2,838-line sanitized full log; **it is not the complete build log**.

Privacy: original workstation paths replaced with `<HOME>`, `<ESP_IDF_ROOT>` and `<PROJECT_ROOT>` in excerpt. Do not upload non-sanitized source log.

**Outstanding archive gate**: publish the complete sanitized build.log (or the sanitized archive containing it) to durable project evidence storage and link it here before claiming all RTARS-19 acceptance criteria are closed.
