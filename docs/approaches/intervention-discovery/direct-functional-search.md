# Direct Functional Search

> **Status:** Exploratory baseline; not implemented or validated
>
> **Source:** Extracted from Track 2A of the preserved
> [Animal Welfare Research Loop — Baseline v1](../../../archive/historical-designs/animal-welfare-research-loop-baseline-v1.md)

## Purpose

Find existing or adaptable interventions when the causal mechanism and required
functional change are already clear enough to search directly.

## Flow

```text
welfare problem
    -> supported causal mechanism
    -> required functional change
    -> engineering or operational requirements
    -> search patents, products, research and adjacent industries
    -> match candidates to requirements
    -> check evidence, feasibility, safety and prior use
    -> rank candidates
    -> human review
    -> pilot or validate remaining uncertainty
```

## Example

```text
Broiler footpad dermatitis
    -> prolonged wet-litter exposure contributes to lesions
    -> reduce, detect or interrupt damaging moisture exposure
    -> search moisture sensing, leak detection, drying, drainage,
       absorbent materials, contact barriers and exposure-reduction methods
```

## Proposed roles

| Role | Main job |
|---|---|
| Requirements translator | Converts the supported required change into faithful technical and operational requirements. |
| Patent and product scout | Searches existing patents, products and documented deployments. |
| Research scout | Searches engineering, materials, biological and adjacent-domain literature. |
| Requirements matcher | Checks whether a candidate performs the required function under relevant constraints. |
| Evidence and feasibility reviewer | Reviews effectiveness, failure modes, safety, modification burden, cost and deployment constraints. |
| Ranker | Compares candidates using explicit criteria while retaining uncertainty. |
| Human reviewer | Chooses whether to investigate, test, hold or reject a candidate. |

## When to use it

Use direct search when:

- the important mechanism is reasonably well supported;
- the required change can be stated without a hidden scientific assumption;
- the relevant functional requirements are clear; and
- likely technology or intervention categories are already visible.

Use the deeper
[Welfare Technology Scanner](welfare-technology-scanner/README.md) when direct
search returns generic results, the mechanism contains several interacting
conditions, or multiple intervention points need to be exposed.

## Evaluation

- recovery of known effective and ineffective interventions;
- recall and precision against curated patent, product and research sets;
- expert assessment of functional fit;
- identification of non-obvious adjacent-industry transfers;
- correct recognition of prior use and contradictory evidence;
- unsafe or infeasible candidate rate; and
- usefulness, cost and time compared with simpler keyword or semantic search.

## Limits

Direct search can be fast, but it can inherit an incorrect causal assumption or
produce only obvious technology categories. A candidate match does not establish
that the intervention will improve welfare in the target context.
