# Candidate LLM Pipelines

> **Status:** Exploration and comparison. No pipeline has been selected for
> implementation.

This folder contains the repository's central design work. Its purpose is to
make possible LLM pipelines easy to inspect side by side before custom agents
are built.

## Current candidates

| Candidate | How it searches for interventions | Intended output | Current maturity |
|---|---|---|---|
| [Welfare Technology Scanner](welfare-technology-scanner.md) | Builds evidence-qualified causal pathways, translates approved nodes into species-neutral requirements, and searches patents, research and products. | Ranked technologies tied to explicit causal and evidence paths. | Detailed process and PRD; not implemented or validated. |
| [Animal Welfare Research Loop — Baseline v1](animal-welfare-research-loop-baseline-v1.md) | Moves from a welfare problem through mechanisms and measurable processes to intervention search, testing and iteration. | Testable intervention and mechanism hypotheses, followed by experimental learning. | Exploratory baseline; not implemented or validated. |
| [Jev Welfare-Case Analogy Pipeline](jev-welfare-case-analogy-pipeline.md) | Classifies source and target problems on shared welfare dimensions, finds similar cases and retrieves their linked solutions. | Cross-domain solutions labelled as derived, unverified research candidates. | Exploratory retrieval proposal; not implemented or validated. |

## How to compare them

Apply the same questions to every candidate:

1. **Purpose:** What decision or discovery task does it improve?
2. **Pipeline:** What are its exact stages, inputs, outputs and feedback loops?
3. **Division of labour:** What should an LLM do, and what should be handled by
   search, ordinary code or a person?
4. **Evidence:** How are claims, quotations, context, uncertainty and provenance
   retained?
5. **Search breadth:** Can it surface medical, biological, engineering,
   materials, sensing and operational solutions?
6. **Transfer safety:** How does it prevent an analogy or match from being
   mistaken for proof?
7. **Feasibility:** What data, models, tools and human expertise are required?
8. **Evaluation:** What small backtest or prospective test could falsify its
   value?

## How to read the candidates

- For the Welfare Technology Scanner, start with its
  [process map](../../prototypes/welfare-scanner/PROCESS_MAP.md), then consult the
  [process specification](../../prototypes/welfare-scanner/PROCESS_SPEC.md) and
  [PRD](../../prototypes/welfare-scanner/PRD.md).
- For the Research Loop, begin with the core flow and then compare its
  scientific-discovery and technology-transfer tracks.
- For the Jev pipeline, begin with the summary, the boundary around what is
  vectorised, and the worked examples.

The candidates are not assumed to be mutually exclusive. For example, analogy
retrieval could eventually supply leads to a deeper causal or experimental
pipeline. Any combination should be an explicit design decision made after the
individual approaches have been evaluated, not an accidental mixture.

## Decision sequence

1. Bring every serious candidate to a comparable level of detail.
2. Test each candidate on the same small set of welfare problems.
3. Record strengths, failures, cost and human-review burden.
4. Select one pipeline or document a deliberate combination.
5. Define the stage contracts and only then specify the custom agents.

