# Definition of Ready (DoR)

**Project:** RIG-TARS · **Tracking:** [RTARS-12](https://niccolopiazzi01.atlassian.net/browse/RTARS-12) · **Status:** proposed policy

A Jira issue is **Ready** when an implementer can begin work without needing to guess its scope, prerequisites or success criteria. This gate applies before starting work, not before opening an issue.

## Checklist

- [ ] Objective and expected deliverable are explicit.
- [ ] Acceptance criteria are observable and testable.
- [ ] Dependencies, blockers and prerequisites are identified; any blockers preventing safe execution are resolved.
- [ ] Required sources, specifications and references are linked, or knowledge gaps are explicitly identified with a plan to resolve them.
- [ ] Required tools, hardware, access and environment are available, **when applicable**.
- [ ] Known risks and safety constraints are identified, **when applicable**.
- [ ] Completion can be judged objectively using the acceptance criteria and the [DoD](DEFINITION_OF_DONE.md).

## Operating rules

1. Record the applicable criteria in the Jira issue. Mark irrelevant criteria `N/A` with a short reason rather than treating them as failed.
2. For *research/discovery* issues, unknowns are expected: the deliverable must instead define which questions, evidence and decisions the research will produce. Unknowns do not prevent Ready unless they make the work unsafe or unbounded.
3. An issue not meeting this gate remains in backlog/clarification; do not silently treat it as ready.
4. A hardware activity with unresolved electrical or motion safety prerequisites is **not** Ready. See [Hardware Safety](HARDWARE_SAFETY.md).
5. Jira is the source of truth for scope, status and acceptance criteria; repository documents are the versioned source for project policies and evidence.
