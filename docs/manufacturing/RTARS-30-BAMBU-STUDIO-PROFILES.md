# RTARS-30 — Bambu Studio print profiles (draft)
Status: DOCUMENTED / NOT YET SLICER-VALIDATED. Jira: RTARS-30.

## Inputs and constraints
- Slicer: **Bambu Studio only**; OrcaSlicer references in Jira were corrected.
- Printer model, nozzle diameter/material, filament type/brand, filament condition, slicer version: **UNKNOWN** pending hardware evidence (RTARS-29).
- Do not import `HL-18 FAST 0.28mm @Elegoo Neptune4 0.4 nozzle` as a validated profile.
- Source: RTARS-28 `PART_CLASSIFICATION.csv` (13 types / 16 instances). Geometric mating surfaces and actual tolerances remain **NOT TESTED**.
- Source geometry is subject to MakerWorld Exclusive restrictions. Do not commit 3MF/STL, embedded geometry, G-code or screenshots exposing restricted geometry without permission.

## Proposed profile families — not exported or validated
| Field | RTARS-AESTHETIC | RTARS-FUNCTIONAL |
|---|---|---|
| Intended use | Visible outer shells, where no critical interface is affected | Structural, motion, mounting and interface features |
| Layer height (candidate, assuming suitable 0.4 mm nozzle) | 0.16 mm | 0.20 mm |
| Printer preset | Actual verified Bambu printer preset | Same verified printer preset |
| Filament preset | Verified material/vendor preset | Same verified material/vendor preset |
| Speed | Manufacturer's material/printer baseline; reduce outer-wall speed only after inspection | Manufacturer's baseline, conservative for dimensional surfaces after calibration |
| Walls/infill | Decide from part loads and preview; no universal numeric claim | Decide from load paths and test coupons; no unverified strength claim |
| Orientation | Prioritize visible surface and minimize support marks; protect mating surfaces | Prioritize load direction, layer adhesion, dimensional axes and critical interfaces |
| Supports | Only where preview identifies unsupported features; document interface/marks | Keep supports off mating surfaces where feasible; review overhangs and removal clearance |
| XY compensation / hole compensation / clearance | Default verified preset until measured | No arbitrary compensation; tune using RTARS-31 fit tests |

0.16/0.20 mm are **starting hypotheses**, not universal Bambu Lab recommendations. Confirm available layer heights and extrusion constraints for the actual nozzle. Functional classification can override visual classification for mixed-purpose shells.

## Per-part provisional routing (not a validated plate layout)
- Functional priority P0: P01 arm (2), P05 main body (1), P08 joystick (1), P13 servo arm (1).
- Mixed-purpose P1: P02/P03 arm shells, P04 body shell, P06 display housing, P07 camera cover, P09 bracket, P10/P11 PCB supports, P12 servo covers (3). Select profile per interface/face after visual inspection, not by name alone.
- Every orientation and support decision is **PENDING** actual Bambu Studio preview. Do not infer geometry from source labels.

## Minimal capture procedure
1. In Bambu Studio, capture About/version, printer model and nozzle diameter, filament preset (brand/type), build plate and printer process preset; mask account/device identifiers.
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
| RTARS-29 printer/nozzle/filament verification | NOT TESTED |
| Native presets exported/versioned | NOT TESTED |
| Part-by-part orientation/support justification | NOT TESTED |
| Four-plate Bambu Studio slicing with target presets | NOT TESTED |
| RTARS-31 functional fit test | NOT TESTED (downstream) |
| RTARS-32 definitive production | BLOCKED (downstream) |

No physical prints, fit tests, dimensional measurements or native preset exports are claimed.
