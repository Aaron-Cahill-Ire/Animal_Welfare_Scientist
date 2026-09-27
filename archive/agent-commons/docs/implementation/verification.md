# Verification record

2026-09-13, development implementation. Main runtime: Python 3.9.6. Browser-runtime check: Pyodide 0.27.7 / Python 3.12.7 executed under Node (not a full browser UI test).

- 52 unittest tests pass, including exact numerical checks, generated-script reproduction, schema validation, typed capability handoffs, human/external gates and two reproduced review regressions.
- 84 semantic starter cases pass across all 20 agents; each is paired with its actual simple-baseline run. See benchmarks/results/starter.json for individual outcomes and configuration identity.
- All 20 supported examples and the same 84 starter cases execute successfully in the pinned WebAssembly Python runtime.
- Four full workflows generate gate-by-gate transcripts from actual software execution with explicitly simulated decisions and external result artifacts. No real study/approval/registration is implied.
- Static site contract check confirms 33 records, matching example/evaluation configuration identities, bundled executable source and rejection of an invalid worker agent ID. JavaScript syntax checks pass.
- Native POSIX deadline, private-input rejection, source count/input-byte budgets and configuration changes on budget changes are implemented. Runtime preemption in other embedding threads is not claimed.
- Code-reuse/quality/efficiency review applied dead-code cleanup, removed repeated source hashing from site generation, avoided repeated DOM reads and duplicate missingness/count scans. Other small helper consolidations were skipped to avoid coupling independent task modules for negligible benefit. Worker lifetime is intentionally bounded and ends after each trial.

Known validation limits: no independent scientific review, no real-farm test, no browser/device accessibility conformance audit, and no native WebMCP registration verification. The site uses native semantic controls, escaped untrusted text, safe URL protocols and responsive layouts; those implementation choices do not certify WCAG conformance.

Initial runner test demonstrated missing module failure before implementation. Review regressions demonstrated false full coverage from incompatible candidates and an aborted no-candidate discovery before their fixes; both now pass. Other feature coverage was written during implementation, and no universal test-first claim is made.
