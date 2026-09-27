# Welfare Technology Scanner

> **Status:** Exploratory pipeline design; not implemented or validated  
> **Role in the wider project:** A deeper intervention-discovery pipeline based
> on evidence-qualified causal decomposition

## Purpose

The Welfare Technology Scanner starts with a defined welfare harm, builds and
checks possible causal pathways, and turns approved parts of those pathways
into species-neutral technology-search requirements.

Its proposed flow is:

```text
welfare harm
    -> evidence-qualified causal pathways
    -> necessary conditions and stopping decisions
    -> species-neutral search requirements
    -> patent, research and product searches
    -> mechanism and prior-use checks
    -> ranked candidates
    -> human decision
```

The approach is more developed on paper than the other methods, but that
does not mean it has been selected or proven. The current materials define and
illustrate a possible pipeline.

## Canonical design material

The canonical design documents remain together in this folder:

1. [Process map](process-map.md) — the clearest end-to-end explanation and
   worked example.
2. [Process specification](process-specification.md) —
   detailed rules, proposed roles and handoffs.
3. [Product requirements document](prd.md) —
   product boundary, artefact contracts, workflow states and acceptance
   criteria.
4. [Supporting artefact index](../../../../prototypes/welfare-scanner/README.md) —
   workbook, interface snapshots, teaching visual and provenance notes.

## Important boundary

The Markdown files in this folder describe the intended process. The workbook,
dashboard and teaching visual under `prototypes/welfare-scanner` support that
design but do not make the proposed LLM pipeline runnable.

Before implementation, this candidate still needs to be compared with the
other approaches, reduced to a testable first slice, and evaluated on shared
example problems.
