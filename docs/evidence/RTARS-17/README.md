# RTARS-17 — RIG-TARS upstream firmware build

## Provenance
- Jira: RTARS-17
- Upstream: https://github.com/LuwuDynamics/rig_omni
- Upstream commit: `c2b42cd73ef65f5cd2a158d6949f0273869454dc`
- Host OS: Debian 13, Linux 6.12.94 (hostname/user redacted)
- ESP-IDF: v5.5.3; Xtensa GCC 14.2.0; CMake 3.31.6
- Python: 3.13.5; numpy==2.5.5; pillow==13.0.0
- Target: ESP32-S3; Board: TARS; Region: Overseas
- Original sdkconfig SHA-256: `92d934afdeefe36cffc4d8161a257177275f8d193ce44d3ba08fb252fb04e3ea`

## Result
- Verification build: **PASS**, `idf.py -B build-rtars17-verify build`, exit code **0**.
- Output: `rig-tars.bin`, 3,590,368 bytes.
- ESP-IDF app partition free: 13%.
- Source checkout upstream commit above; `git status --short` only listed untracked generated `build-rtars17-verify/`.
- Previously failed attempts identified missing NumPy and Pillow in the ESP-IDF Python environment; installing them resolved these failures.
- Non-blocking warnings: unused TAG variable in `main/boards/tars/robot.cc`; Kconfig Bluetooth choice selection.

## Evidence
- `artifacts-sha256.txt`: artifact hashes and sizes (original output values).
- `build-result.txt`: success exit code and selected successful build output.
- Detailed source logs retained separately in the sanitized evidence archive; full private `sdkconfig` is deliberately excluded from GitHub.

## Limits
This was a resumed incremental build, not two completed independent clean builds; byte-for-byte reproducibility is **not yet proven**. Flashing and hardware functional testing were **not performed**.

## Privacy
No personal home directory, hostname, temporary build directory, credentials or raw `sdkconfig` is intentionally published. Absolute paths are replaced by descriptive variables in the offline sanitized log archive.
