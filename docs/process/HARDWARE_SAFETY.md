# Hardware safety checklist

**Project:** RIG-TARS · **Tracking:** [RTARS-12](https://niccolopiazzi01.atlassian.net/browse/RTARS-12) · **Status:** proposed policy

Use this checklist **before first power-on and after changes to power, wiring, actuators or mechanical assembly**, as appropriate. It is a project inspection aid, **not** a substitute for verified manufacturer instructions, qualified electrical assessment or formal product certification.

**Stop rule:** If a relevant safety check fails, the specification is uncertain, or an unexpected behavior occurs, stop the test, disconnect power when safe, document the issue and do not resume until it has been resolved.

## 1. Power — before energizing

- [ ] Intended supply voltage and polarity are verified against documentation for the **actual board revision**; do not assume values from another variant.
- [ ] The supply's current capability, connectors and cable rating are appropriate for the connected load according to verified specifications.
- [ ] No visible short, damaged insulation, exposed conductor or loose conductive object is present.
- [ ] Wiring changes were made **with power removed** and any relevant stored energy handled safely.
- [ ] The power disconnect is known, reachable and suitable for promptly stopping an unsafe test.
- [ ] When applicable, voltage/polarity checks are recorded **before** connecting sensitive electronics.

## 2. Wiring — before energizing or moving

- [ ] Pinout, cable orientation and connector placement match the **actual hardware revision**.
- [ ] Connectors are fully seated; no cable or joint is visibly damaged or insecure.
- [ ] Cables cannot enter actuator travel, be pinched, snagged or abraded during the intended test.
- [ ] Exposed conductors and temporary connections are secured/insulated appropriately.
- [ ] Ground and power connections have been checked against the applicable verified schematic, when available.

## 3. Motion — before and during the first test

- [ ] Robot stands on a stable surface with a cleared test area, away from people, pets and fragile objects.
- [ ] Initial motion uses conservative limits and a controlled test sequence **if supported by the hardware/firmware**; unknown safe limits must not be guessed.
- [ ] No obvious mechanical interference, loose fastener or trapped cable exists through the planned travel.
- [ ] A practical, immediate stop/disconnect procedure is available and tested without creating an additional hazard.
- [ ] An operator continuously supervises the first power-on and initial motion tests.
- [ ] Motion stops immediately if there is abnormal sound, overheating, smoke, unexpected motion or loss of control.

## Inspection record (copy into Jira or an evidence document)

| Field | Value |
| --- | --- |
| Jira issue | RTARS-… |
| Date / operator | … |
| Hardware/board revision | … / unknown (do not assume) |
| Firmware version / commit | … / N/A |
| Manufacturer reference(s) | … |
| Checks applied | Power / Wiring / Motion / N/A with reason |
| Result | PASS / FAIL / NOT TESTED |
| Evidence | Link to measurements, photos or test log |
| Outstanding risks / follow-up | … |

## Limits and source discipline

The checklist does **not** prescribe numerical voltage/current thresholds, fuse sizes, actuator speeds or torque limits: these must come from authoritative documentation and/or validated measurements for the installed configuration. Use the repository [official sources index](../references/OFFICIAL_SOURCES_INDEX.md) to trace source documents; mark missing or contradictory specifications as **unverified**. Never perform a risky test solely to fill in missing evidence.
