# Welfare Technology Scanner

> **Status:** Exploratory pipeline design; not implemented or validated  
> **Role in the wider project:** One candidate LLM pipeline for discovering
> cross-domain technologies that may address animal-welfare problems

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

The approach is more developed on paper than the other candidates, but that
does not mean it has been selected or proven. The current materials define and
illustrate a possible pipeline.

## Canonical design material

The detailed files remain together in `prototypes/welfare-scanner` so their
existing relationships and history are preserved:

1. [Process map](../../prototypes/welfare-scanner/PROCESS_MAP.md) — the clearest
   end-to-end explanation and worked example.
2. [Process specification](../../prototypes/welfare-scanner/PROCESS_SPEC.md) —
   detailed rules, proposed roles and handoffs.
3. [Product requirements document](../../prototypes/welfare-scanner/PRD.md) —
   product boundary, artefact contracts, workflow states and acceptance
   criteria.
4. [Supporting artefact index](../../prototypes/welfare-scanner/README.md) —
   workbook, interface snapshots, teaching visual and provenance notes.

## Important boundary

The folder name `prototypes` describes the collection of design and interface
artefacts. It should not be read as evidence that the proposed LLM pipeline is
runnable. The dashboard and teaching visual demonstrate ideas; the Markdown
files describe the intended process.

Before implementation, this candidate still needs to be compared with the
other approaches, reduced to a testable first slice, and evaluated on shared
example problems.

