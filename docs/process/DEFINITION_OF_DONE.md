# Definition of Done (DoD)

**Project:** RIG-TARS · **Tracking:** [RTARS-12](https://niccolopiazzi01.atlassian.net/browse/RTARS-12) · **Status:** proposed policy

A Jira issue may be marked **Done** only after all applicable conditions below are met. Passing the DoD does not imply that unrelated hardware characteristics have been certified.

## Checklist

- [ ] Every acceptance criterion is satisfied and supported by reproducible or inspectable evidence.
- [ ] Any deliverable and source changes are committed to the repository, **when applicable**.
- [ ] Affected technical documentation, interfaces, setup instructions and source references are updated, **when applicable**.
- [ ] Relevant tests or inspections have been executed and their results recorded (including failures and limitations).
- [ ] No unresolved **blocking** defect or unacceptable safety risk remains in the delivered scope.
- [ ] Residual limitations, follow-up work and accepted nonblocking risks are documented and linked to Jira.
- [ ] Repository changes have passed the relevant review/checks and are integrated into the target branch, **when applicable**.
- [ ] The Jira issue links the relevant commit, PR, document or inspection evidence and reflects the delivered result.
- [ ] For powered, wired or moving hardware, the applicable items in [Hardware Safety](HARDWARE_SAFETY.md) have been checked and evidence recorded.

## Evidence standard

- **PASS:** link a test run, commit, PR, log, photograph, measurement or signed inspection note that actually demonstrates the criterion.
- **FAIL / NOT TESTED:** never translate either into PASS. A blocking failure prevents Done.
- **N/A:** give a concise reason. Do not require firmware flashing for a documentation-only task, or mechanical movement testing for an unrelated research task.
- A follow-up ticket is **not** a substitute for acceptance of a blocking criterion or an unresolved safety issue.

## Completion workflow

1. Verify all relevant acceptance criteria.
2. Run the applicable tests/checklists and capture evidence.
3. Update documents and link evidence in Jira.
4. Review and integrate repository changes where applicable.
5. Mark the issue Done only after the preceding gates pass.

This policy is intentionally lightweight: the evidence and checks must scale with the actual scope and hazard of the change.
