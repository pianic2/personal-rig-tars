# RTARS-30 — Audit of user-exported Bambu Studio process presets

Input: `Process presets.zip`, provided 2026-11-22. SHA-256: `26f41f13772589bdeb85dbb3520e3a09d85a93c722a14ac493b4700f354d13ae`. Contains 5 JSON process presets; inspection was of archive contents, not a physical print or slicing validation. Do not commit the unreviewed source archive until licensing/privacy checks.

| Process preset | Layer mm | Outer wall mm/s | Inner wall mm/s | Infill mm/s | Default acceleration mm/s² |
|---|---:|---:|---:|---:|---:|
| HL-18 FAST 0.28 | 0.28 | 100 | 150 | 180 | 4000 |
| HL-18 QUALITY 0.20 | 0.20 | 50 | 70 | 80 | 1500 |
| HL-18 ULTRAFAST 0.28 | 0.28 | 120 | 220 | 250 | 6000 |
| HL-18 ULTRAFAST 0.32 | 0.32 | 200 | 350 | 400 | 10000 |
| PLA_DIAGNOSTIC_CONSERVATIVE 0.20 | 0.20 | 35 | 45 | 55 | 700 |

Common settings present: 3 wall loops, 25% gyroid sparse infill, automatic normal supports enabled, support top Z distance 0.2 mm, both XY hole and contour compensation 0. JSON version value: `2.3.0.70` in all five (export file version; do **not** assume it proves current installed application version). `compatible_printers: []` in all five: no printer compatibility binding attested by this field.

## Assessment
- **PASS:** archive readable, five process-preset JSON files and settings inventoried. This is genuine user-provided configuration evidence.
- **NOT TESTED:** native printer preset (machine dimensions, kinematics, start/end G-code), filament preset for ELEGOO PLA Metallic Bronze (temperature, flow, cooling), active slicing settings, orientation/support quality on actual meshes, successful 4-plate slicing, printed accuracy/fit.
- Candidate baselines: QUALITY 0.20 or DIAGNOSTIC CONSERVATIVE 0.20 for future tests, subject to Neptune 4 Standard machine/filament verification. Neither is approved as RTARS-FUNCTIONAL. AESTHETIC 0.16 has not been exported and must not be claimed as existing.
- Do not carry FAST/ULTRAFAST settings to functional interfaces. High wall speeds/accelerations in these exports do not establish achievable quality.

## Minimal next collection
Export or locate **Printer preset** and **Filament preset** as JSON from Bambu Studio's user preset configuration or relevant export options, without source 3MF/G-code. If only process exports are offered, identify locally saved custom printer and filament presets; don't substitute names or screenshots for configuration contents. Before any real print confirm machine-specific start/end G-code and safety limits against ELEGOO Neptune 4 Standard.
