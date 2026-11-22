# RTARS-30 — Bambu Studio print profiles (draft)
Status: DOCUMENTED / NOT YET SLICER-VALIDATED. Jira: RTARS-30.

## Inputs and constraints
- Slicer: **Bambu Studio only**; OrcaSlicer references in Jira were corrected.
- **USER-CONFIRMED 2026-11-22:** printer ELEGOO Neptune 4 Standard; nozzle diameter 0.4 mm; ELEGOO PLA Metallic Metal Bronze; digital caliper available. Nozzle material/wear, firmware, filament dryness, Bambu Studio version, exact printer preset and actual slicer configuration **NOT VERIFIED**. Hardware testimony is not a physical inspection or slicer proof.
- Do not import `HL-18 FAST 0.28mm @Elegoo Neptune4 0.4 nozzle` as a validated profile.
- Source: RTARS-28 `PART_CLASSIFICATION.csv` (13 types / 16 instances). Geometric mating surfaces and actual tolerances remain **NOT TESTED**.
- Source geometry is subject to MakerWorld Exclusive restrictions. Do not commit 3MF/STL, embedded geometry, G-code or screenshots exposing restricted geometry without permission.

## Proposed profile families — not exported or validated
| Field | RTARS-AESTHETIC | RTARS-FUNCTIONAL |
|---|---|---|
| Intended use | Visible outer shells, where no critical interface is affected | Structural, motion, mounting and interface features |
| Layer height (candidate, assuming suitable 0.4 mm nozzle) | 0.16 mm | 0.20 mm |
| Printer preset | Native `Elegoo Neptune 4 0.4 nozzle` preset **if confirmed in installed Bambu Studio** | Same verified Neptune 4 0.4 mm preset |
| Filament preset | ELEGOO PLA Metallic Bronze custom filament preset after checking manufacturer's material settings | Same verified Metallic Bronze preset |
| Speed | Manufacturer's material/printer baseline; reduce outer-wall speed only after inspection | Manufacturer's baseline, conservative for dimensional surfaces after calibration |
| Walls/infill | Decide from part loads and preview; no universal numeric claim | Decide from load paths and test coupons; no unverified strength claim |
| Orientation | Prioritize visible surface and minimize support marks; protect mating surfaces | Prioritize load direction, layer adhesion, dimensional axes and critical interfaces |
| Supports | Only where preview identifies unsupported features; document interface/marks | Keep supports off mating surfaces where feasible; review overhangs and removal clearance |
| XY compensation / hole compensation / clearance | Default verified preset until measured | No arbitrary compensation; tune using RTARS-31 fit tests |

0.16/0.20 mm are **starting hypotheses**, not universal Bambu Lab recommendations. Confirm available layer heights and extrusion constraints for the actual nozzle. Functional classification can override visual classification for mixed-purpose shells.

## Verified references and filament limits
- Official ELEGOO Neptune 4 printer specification: https://www.elegoo.com/products/elegoo-neptune-4-fdm-3d-printer (Standard model; Klipper; PLA capable). This is a machine specification, not proof of correct G-code.
- Official ELEGOO PLA Metallic product documentation: https://www.elegoo.com/products/pla-metal-filament-1-75-mm-colored-1-kg (Metallic Bronze variant; manufacturer's published bed range 35–65 °C, subject to build plate). Do not import settings from **Bambu PLA Metal**, a different product. Do not assume the material contains actual metal powder.
- Bambu Studio source contains Elegoo printer/filament preset definitions: https://github.com/bambulab/BambuStudio/tree/master/resources/profiles/Elegoo . Presence in upstream source does **not** prove the user's installed version ships or activates the exact Neptune 4 Standard 0.4 mm profile.
- Before printing, verify start/end G-code, bed dimensions, kinematics, temperature limits and Klipper compatibility against **the correct Neptune 4 Standard** preset. Do not blindly use G-code from Bambu or Neptune 4 Pro/Plus/Max profiles.
- RTARS-34 original four-plate estimates remain historical. A second four-plate **HL-18 QUALITY 0.20 mm / Generic PLA** preview is now documented in [RTARS-30-QUALITY-SLICING-EVIDENCE.md](RTARS-30-QUALITY-SLICING-EVIDENCE.md): 23h19m, 87.04 m, 259.61 g (MODEL aggregate only). These are two distinct runs, not proof of equivalent inputs; neither qualifies as a validated dedicated RTARS profile.

## Per-part provisional routing (not a validated plate layout)
- Functional priority P0: P01 arm (2), P05 main body (1), P08 joystick (1), P13 servo arm (1).
- Mixed-purpose P1: P02/P03 arm shells, P04 body shell, P06 display housing, P07 camera cover, P09 bracket, P10/P11 PCB supports, P12 servo covers (3). Select profile per interface/face after visual inspection, not by name alone.
- Every orientation and support decision is **PENDING** actual Bambu Studio preview. Do not infer geometry from source labels.

## Minimal capture procedure
1. In Bambu Studio, capture About/version and specifically select **Elegoo Neptune 4 (Standard), 0.4 mm** rather than Neptune 4 Pro/Plus/Max or a Bambu Lab machine. Capture printer, filament (ELEGOO PLA Metallic Bronze), nozzle and selected process presets, build plate; mask account/device identifiers. If the exact Neptune 4 Standard 0.4 mm preset is absent, STOP: no G-code export or machine execution based on another printer's profile.
2. Open the locally licensed original 3MF, confirm source hash against `MODEL_MANIFEST.json`; do not edit source geometry. Save a separate local working copy.
3. Duplicate the applicable native process preset twice, name `RTARS-AESTHETIC` and `RTARS-FUNCTIONAL`; record every overridden setting versus factory preset.
4. For each of four plates, inspect every part and classify selected process, orientation, supports, overhangs, seam, toolpath preview and warnings. Capture screenshot evidence only if it does not redistribute protected geometry; otherwise capture sanitized settings and text-only inspection results.
5. Slice each plate; record slicer version, printer/nozzle/material, preset names, time and filament estimates, warnings and status. Estimates are not print measurements. Reconcile with RTARS-34 (four plates; current total estimated 12h03m14s and 269.85g, from previous screenshot only).
6. Export native user presets from Bambu Studio and record their exact format, paths and SHA-256. Review export contents for embedded source geometry, identifiers, credentials and licensing before committing. If native export cannot be safely shared, keep it local and document the blocker; do not claim AC satisfied.
7. For RTARS-31, print a small functional test coupon or designated original part, measure with caliper and log dimensional deviation and fit; no forced mating or geometry changes without review.

## Evidence matrix
| Gate | Status |
|---|---|
| Jira scope uses Bambu Studio | PASS |
| DoR/DoD and RTARS-28 classification consulted | PASS |
| RTARS-29 printer/nozzle/filament identification (user declaration) | PASS (declaration only) |
| Installed slicer version, correct machine preset, filament condition and temperatures | NOT TESTED |
| Native presets exported/versioned | NOT TESTED |
| Part-by-part orientation/support justification | NOT TESTED |
| Four-plate Bambu Studio slicing **with legacy QUALITY + Generic PLA** | PASS — screenshot of estimates only; toolpaths/supports not shown |
| Four-plate Bambu Studio slicing **with dedicated RTARS target presets** | NOT TESTED |
| RTARS-31 functional fit test | NOT TESTED (downstream) |
| RTARS-32 definitive production | BLOCKED (downstream) |

No physical prints, fit tests, dimensional measurements, G-code safety verification, **dedicated profile slicing** or native RTARS preset exports are claimed. A screenshot confirms that the user obtained **one four-plate slicing summary using a legacy QUALITY process and Generic PLA**; detailed per-part toolpaths and support inspection remain NOT TESTED.
