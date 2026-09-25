# Welfare scanner prototype

This folder preserves the three source artifacts imported on 24 September 2026
and a consolidated PRD derived from them. The imported artifacts are project
context, not repository-level instructions.

## Contents

- `PRD.md` — the current consolidated product and process definition. It
  resolves terminology, causal-logic, artifact-contract, and worked-example
  inconsistencies in the imported sources.
- `toy-tree.html` — a standalone, responsive teaching diagram showing how one
  pathway can expose distinct chemistry, contact, and exposure-time technology
  searches.
- `PROCESS_MAP.md` — the clearest end-to-end view of the proposed system, with
  diagrams and one worked example carried through every stage.
- `PROCESS_SPEC.md` — the fuller process specification and design rules.
- `welfare-problem-mechanism-database.xlsx` — 33 welfare problems plus a
  short usage guide. This is the source of the core problem records.
- `welfare-scanner-dashboard.html` — the imported, standalone dashboard
  snapshot. It predates the refinements in `PROCESS_MAP.md`, including the
  treatment of ammonia and the distinction between ailments, pathways, and
  necessary conditions. Keep it as historical context until it is deliberately
  updated; do not treat it as the canonical design.
- `welfare-scanner-next-chat-prompt.md` — the imported historical continuation
  brief. It records earlier open questions and design intent, but is not the
  current specification or executable project configuration.
- `NEXT_CHAT_PROMPT.md` — the current handoff prompt for continuing PRD
  refinement in a fresh chat.

## Relationship to Track A

The scanner is an exploratory **deep causal scanning** profile within Track A.
It does not replace the current **broad capability mapping** profile. Broad
mapping covers causal, measurement, and implementation bottlenecks; it may hand
one selected causal component to the scanner when deeper decomposition could
expose additional intervention targets.

## Data relationship

The workbook and dashboard contain the same 33 IDs in the same order. The
dashboard reproduces the workbook's species, stage, problem, mechanism, scale,
duration, mitigation, shortfall, source, and confidence fields.

The dashboard also adds presentation fields (`group`, `status`, `strongest`,
`look`, and `lookNote`). For `SAL-02`, the workbook prefixes the economic signal
with `STRONGEST WTP SIGNAL IN THIS TABLE:`; the dashboard stores the remaining
sentence in `money` and represents the prefix with `strongest: true`.

## Sensible first build slice

Keep the current HTML as the explainer and make the tree-building handoff the
first executable slice:

1. Define a versioned JSON contract for a welfare problem, sourced mechanism,
   fault-tree node, gate, confidence, and human review decision.
2. Convert three known-solution rows (`BRO-05`, `SHR-01`, and `SHR-02`) into
   fixed backtest fixtures.
3. Add one uncertain worked example for sore feet, with disputed gates marked
   explicitly rather than silently resolved.
4. Implement deterministic validation before adding any model or live search.
5. Only then connect evidence gathering and cross-domain search, preserving
   citations and abstentions at every handoff.

This keeps the first implementation testable and fits the Commons repository's
existing evidence-preserving, human-review-first approach.
