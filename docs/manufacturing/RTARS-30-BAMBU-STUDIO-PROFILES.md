# RTARS-30 — Bambu Studio print profiles (draft)
Status: TWO NATIVE PRESETS VERSIONED / THREE-PART FUNCTIONAL SLICING VERIFIED / THREE-PART PREVIEW OPERATOR PASS. Jira: RTARS-30.

## Inputs and constraints
- Slicer: **Bambu Studio only**; OrcaSlicer references in Jira were corrected.
- **USER-CONFIRMED 2026-11-22:** printer ELEGOO Neptune 4 Standard; nozzle diameter 0.4 mm; ELEGOO PLA Metallic Metal Bronze; digital caliper available. RTARS-29 subsequently documented **hardened steel 0.4 mm nozzle**, Bambu Studio version **2.8.2.61**, filament preset **Generic PLA @Elegoo**, nozzle temperatures **210°C first layer / 205°C subsequent**, bed **60°C**, machine inspection and previous G-code readability, all under operator testimony and selectively corroborated by Filament Manager photographs. See [RTARS-29 evidence](../../evidence/RTARS-29/README.md) and [inspection.json](../../evidence/RTARS-29/inspection.json); RTARS-29 is Done. Machine start/end G-code for the functional pilot has been inspected statically in the supplied G-code; motion safety on the live printer, nozzle wear and filament dryness are not independently measured. Operator observations are not a third-party certification.
- Do not import `HL-18 FAST 0.28mm @Elegoo Neptune4 0.4 nozzle` as a validated profile.
- Source: RTARS-28 `PART_CLASSIFICATION.csv` (13 types / 16 instances). Geometric mating surfaces and actual tolerances remain **NOT TESTED**.
- Source geometry is subject to MakerWorld Exclusive restrictions. Do not commit 3MF/STL, embedded geometry, G-code or screenshots exposing restricted geometry without permission.

## Profile families — exported and versioned as candidates; physical performance not validated
| Field | RTARS-AESTHETIC | RTARS-FUNCTIONAL |
|---|---|---|
| Intended use | Visible outer shells, where no critical interface is affected | Structural, motion, mounting and interface features |
| Layer height (candidate, assuming suitable 0.4 mm nozzle) | 0.16 mm | 0.20 mm |
| Printer preset | Native `Elegoo Neptune 4 0.4 nozzle` preset **if confirmed in installed Bambu Studio** | Same verified Neptune 4 0.4 mm preset |
| Filament preset | Generic PLA @Elegoo observed in RTARS-29; temperatures within ELEGOO Metallic specifications, but filament-specific flow/cooling calibration not established | Same observed Generic PLA @Elegoo with the same qualification limits |
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

## Quantitative reference from the closed RTARS-29 hardware inspection

- ELEGOO PLA Metallic limits: nozzle **190–230°C**, bed **35–65°C**, recommended **hardened-steel nozzle ≥0.4 mm**. Operator declares hardened-steel 0.4 mm (replacement of brass documented); setpoints **210°C initial, 205°C rest**, bed **60°C** satisfy the manufacturer temperature envelope. Official product: https://www.elegoo.com/products/pla-metal-filament-1-75-mm-colored-1-kg.
- `Generic PLA @Elegoo` Filament Manager screenshots showed 1.75 mm, these setpoints and cooling controls. This is **documented operational compatibility within temperatures**, not a filament-specific flow/PA calibration.
- RTARS-29 is recorded Done; do not reopen its accepted discovery DoD merely because RTARS-30 has deeper quality gates. The operator subsequently supplied a body-shell and a three-part G-code file whose start/end command sequences were inspected statically. Previous reports of successful prints do **not** independently certify current motion safety or live Klipper behavior.
- Source-specific RTARS process candidates are **generated and checksum-verified**; user reported successful import of both. Rebuild recipe: [rebuild_rtars30_presets.py](../../tools/manufacturing/rebuild_rtars30_presets.py). The complete native JSON presets are **now versioned** under [`docs/manufacturing/presets/`](presets/); both are byte-identical to the distributed candidate ZIP.

## Per-part provisional routing (not a validated plate layout)
- Functional priority P0: P01 arm (2), P05 main body (1), P08 joystick (1), P13 servo arm (1).
- Mixed-purpose P1: P02/P03 arm shells, P04 body shell, P06 display housing, P07 camera cover, P09 bracket, P10/P11 PCB supports, P12 servo covers (3). Select profile per interface/face after visual inspection, not by name alone.
- The user **confirmed PASS of a local Preview inspection on the three-part functional pilot batch**, covering stable bed contact, supports clear of critical interfaces and removable, load-compatible orientation, and no slicer warnings. The evidence is a single **batch-level operator declaration** applied to three objects, not independent third-party verification. See [recorded checklist](RTARS-30-THREE-PART-ORIENTATION-SUPPORT-CHECKLIST.md). **All other original model parts remain not inspected** and must be reviewed before their own prints.

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
| RTARS-29 hardware and filament identification | PASS for RTARS-29 AC; operator record and partial UI evidence, issue Done |
| Hardened-steel nozzle 0.4 mm, temperature setpoints 210/205/60°C | PASS for manufacturer range and operator declaration; physical measurement NOT TESTED |
| Bambu Studio version and Generic PLA @Elegoo settings | PASS documented via RTARS-29; functional pilot G-code start/end inspected statically, live behavior NOT TESTED |
| Native candidate presets exported/versioned | PASS — both native JSONs under `docs/manufacturing/presets/`, byte-identical to original ZIP |
| User import in Bambu Studio | PASS — user declaration |
| Three-part functional G-code slicing | PASS — metadata inspected; see [`RTARS-30-THREE-PART-GCODE-AUDIT.md`](RTARS-30-THREE-PART-GCODE-AUDIT.md) |
| Pilot three-part orientation/support justification | PASS operator-declared batch Preview review — [inspection record](RTARS-30-THREE-PART-ORIENTATION-SUPPORT-CHECKLIST.md); geometry not republished |
| Remaining model parts (outside three-part batch) | NOT TESTED — future printing requires their individual Preview checks |
| Four-plate Bambu Studio slicing **with legacy QUALITY + Generic PLA** | PASS — screenshot of estimates only; toolpaths/supports not shown |
| Four-plate Bambu Studio slicing **with dedicated RTARS target presets** | NOT TESTED |
| RTARS-31 functional fit test | NOT TESTED (downstream) |
| RTARS-32 definitive production | BLOCKED (downstream) |

No new physical prints, fit tests or dimensional measurements are claimed. **Functional-profile slicing is documented for three distinct objects**; static G-code inspection completed; **local spatial supports/orientations marked PASS by the operator for this pilot batch** only. Both complete native candidate process JSONs are committed in GitHub. A screenshot confirms that the user obtained **one four-plate slicing summary using a legacy QUALITY process and Generic PLA**; remaining original model parts outside the pilot batch have no orientation/support approval.
