# Animal Welfare Scientist — LLM Pipeline Design Workspace

> **Current status:** This repository is comparing possible LLM-assisted
> research approaches. No final pipeline or agent architecture has been
> selected.

The goal is to decide how an Animal Welfare Scientist should help with two
different jobs:

1. **Scientific discovery:** improve understanding of what causes an animal-
   welfare problem and what experiment should come next.
2. **Intervention discovery:** find existing or adaptable interventions that
   may change a sufficiently understood welfare-relevant process.

Custom agents should be designed only after the relevant pipeline, handoffs and
evaluation criteria are clear.

## Start here

The central design work is in the
[approaches index](docs/approaches/README.md).

| Approach family | Central question | Current entry point |
|---|---|---|
| **Scientific discovery** | What causes the suffering, and how could competing explanations be tested? | [Mechanism and hypothesis loop](docs/approaches/scientific-discovery/README.md) |
| **Intervention discovery** | Given what needs to change, what existing or adaptable intervention might change it? | [Intervention-discovery methods](docs/approaches/intervention-discovery/README.md) |

The initial routing question is:

```text
Do we understand the relevant causal mechanism well enough
to state what must change?

No or uncertain -> scientific discovery
Yes             -> intervention discovery
```

The two families share rules for evidence, provenance, human review,
uncertainty and evaluation. Those are recorded in
[shared foundations](docs/approaches/shared-foundations.md).

## Intervention-discovery methods under consideration

| Method | How it generates candidates | Scope |
|---|---|---|
| [Direct functional search](docs/approaches/intervention-discovery/direct-functional-search.md) | Translates a known required change directly into technical requirements and searches for matching interventions. | A simple end-to-end baseline when the required function is already clear. |
| [Welfare Technology Scanner](docs/approaches/intervention-discovery/welfare-technology-scanner/README.md) | Builds evidence-qualified causal pathways, turns approved conditions into search briefs, and searches patents, research and products. | A deeper intervention-discovery pipeline. |
| [Jev case-analogy retrieval](docs/approaches/intervention-discovery/jev-case-analogy-retrieval.md) | Finds similar problem cases and retrieves their attached known solutions as unverified candidates. | A candidate-generation module, not a complete research architecture. |

These methods may be alternatives or complementary stages. None has been
selected or validated.

## What the project is deciding

For each approach, ask:

1. What exact research problem does it solve?
2. What enters and leaves each stage?
3. Which stages need an LLM, search, ordinary code or a person?
4. How are evidence, uncertainty and provenance retained?
5. What failure or abstention behaviour is required?
6. What small test could show whether the approach is useful?

The intended sequence is:

```text
compare approaches
    -> select or deliberately combine them
    -> define stage and handoff contracts
    -> design the required custom agents
    -> build a small end-to-end version
    -> evaluate it on known welfare problems
```

## Repository structure

```text
README.md    Project purpose, current status and navigation
docs/        Current approaches, research notes and ideation
prototypes/  Supporting workbooks, interfaces and teaching artefacts
archive/     Preserved combined designs, code, website and experiments
```

## Preserved supporting material

- [`prototypes/welfare-scanner`](prototypes/welfare-scanner/README.md) contains
  the Welfare Scanner workbook, dashboard, teaching visual and historical
  handoff material.
- [`archive/historical-designs`](archive/historical-designs/) preserves the
  original combined Research Loop baseline and the broader original
  WelfareTech proposal.
- [`archive/agent-commons`](archive/agent-commons/README.md) preserves the 20
  deterministic research utilities, sample workflows, catalogue website,
  tests and implementation documents.

Nothing in the archive has been rejected or deleted. It is separated so that
earlier combined designs and implementation experiments do not obscure the
current approach comparison.
