# Animal Welfare Scientist — LLM Pipeline Design Workspace

> **Current status:** This repository is being used to compare possible LLM
> research pipelines. No final pipeline or agent architecture has been selected.

The main goal is to decide **which end-to-end LLM pipeline should be built for
discovering and evaluating possible animal-welfare interventions**. Custom agents
should be designed only after that pipeline and its handoffs are clear.

## Start here: candidate pipelines

The core design work is collected in [`docs/approaches`](docs/approaches/README.md).
There are currently three candidate approaches:

| Candidate | Central idea | Best current entry point |
|---|---|---|
| **Welfare Technology Scanner** | Decompose a welfare harm into supported causal pathways and searchable technical requirements, then search across patents, research and products. | [Approach overview](docs/approaches/welfare-technology-scanner.md) and [process map](prototypes/welfare-scanner/PROCESS_MAP.md) |
| **Animal Welfare Research Loop — Baseline v1** | Move from welfare problem to mechanism, measurable process, intervention, experiment and updated hypothesis. | [Read the baseline](docs/approaches/animal-welfare-research-loop-baseline-v1.md) |
| **Jev Welfare-Case Analogy Pipeline** | Represent problem cases on shared welfare dimensions, retrieve similar known cases and transfer their linked solutions as unverified hypotheses. | [Read the analogy pipeline](docs/approaches/jev-welfare-case-analogy-pipeline.md) |

These are exploratory proposals. They may turn out to be alternatives,
complementary stages, or unsuitable. The repository does not yet claim that one
is the preferred architecture.

## The decision this repository should support

The immediate work is to compare the candidate pipelines and answer:

1. What exact research problem does each pipeline solve?
2. What information enters and leaves each stage?
3. Which stages genuinely need an LLM, ordinary code, search, or human review?
4. How does the pipeline preserve evidence, uncertainty and provenance?
5. Can it search biological, engineering, material, sensing and operational
   interventions without producing unmanageable noise?
6. How would useful output be distinguished from a plausible but unsafe or
   unsupported suggestion?
7. What small test would show whether the pipeline is worth building?

After a pipeline is selected, the intended sequence is:

```text
compare candidate pipelines
        -> select or deliberately combine a pipeline
        -> define stage and handoff contracts
        -> design the required custom agents
        -> build a small end-to-end version
        -> evaluate it on known welfare problems
```

## Repository structure

```text
README.md    Project purpose, current status and decision path
docs/        Candidate pipeline descriptions and current research notes
prototypes/  Detailed artefacts that directly explain a candidate approach
archive/     Preserved earlier proposals, code, website and experiments
```

The root is intentionally small. Someone arriving here should first understand
that the project is **still mapping and evaluating possible approaches**.

## Supporting material

- [`prototypes/welfare-scanner`](prototypes/welfare-scanner/README.md) contains
  the Welfare Technology Scanner's process map, detailed specification, PRD,
  workbook and interface snapshots. These explain one candidate; they do not
  show that it has been selected or implemented end to end.
- [`archive/agent-commons`](archive/agent-commons/README.md) preserves the 20
  deterministic research utilities, sample workflows, catalogue website,
  tests and implementation documents. They are possible future building blocks,
  not the chosen LLM architecture.
- [`archive/historical-designs`](archive/historical-designs/) preserves the
  broader original WelfareTech proposal.

Nothing in the archive has been rejected or deleted. It is separated so that
earlier implementation work does not obscure the current pipeline decision. A
supporting artefact can move back into the main design only when a selected
pipeline shows why it is required.
