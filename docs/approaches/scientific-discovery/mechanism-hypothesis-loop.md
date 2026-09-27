# Mechanism and Hypothesis Loop

> **Status:** Exploratory pipeline; not implemented or validated
>
> **Source:** Extracted from Track 1 of the preserved
> [Animal Welfare Research Loop — Baseline v1](../../../archive/historical-designs/animal-welfare-research-loop-baseline-v1.md)

## Purpose

Use an evidence-grounded, experiment-driven loop to improve understanding of
an animal-welfare problem when the important causal mechanism is uncertain.

## Flow

```text
welfare problem
    -> map possible causal mechanisms
    -> choose a measurable and testable process
    -> state a falsifiable hypothesis
    -> design an experiment
    -> humans run the experiment
    -> analyse the data
    -> update or reject the hypothesis
    -> choose the next experiment
    -> repeat
```

The welfare problem normally remains fixed while the proposed mechanism,
measurement and intervention hypotheses change in response to evidence.

## Inputs

- a clearly scoped welfare problem;
- relevant welfare, veterinary, husbandry and biological literature;
- plausible competing mechanisms;
- available measurements, assays, sensors or outcome measures; and
- practical and ethical constraints on experimentation.

## Outputs

- an evidence-linked mechanism map;
- one or more falsifiable hypotheses;
- a measurable process and welfare outcome;
- an experiment that can distinguish relevant alternatives;
- a reproducible analysis; and
- an explicit update stating what the result changed and what should happen
  next.

## Proposed roles

| Role | Main job |
|---|---|
| Orchestrator | Holds the research objective and routes results back to the appropriate stage. |
| Literature scout | Retrieves evidence for plausible and competing mechanisms. |
| Deep evidence reviewer | Checks claims, contradictory findings, limitations and context. |
| Mechanism and measurement designer | Turns causal ideas into measurable and experimentally testable processes. |
| Experiment-design support | Specifies a study capable of discriminating between hypotheses. |
| Human researchers | Approve and physically conduct the experiment. |
| Data analyst | Analyses trial, sensor, behavioural, lesion-score or biological data. |
| Hypothesis updater | Revises the causal model and proposes the next informative test. |

An LLM may support these roles, but source retrieval, deterministic analysis and
human scientific review remain distinct responsibilities.

## Example: broiler footpad dermatitis

```text
Problem:
Painful footpad dermatitis in broilers

Competing questions:
Which exposure pathways materially contribute to lesions?
How do moisture intensity, contact and duration interact?

Testable process:
Moisture and cumulative exposure at the litter-foot interface

Experiment:
Manipulate or measure the proposed process while recording lesion and welfare
outcomes

Update:
Retain, narrow or reject the proposed mechanism, then choose the next test
```

The experiment should distinguish two questions:

1. Did the intervention or manipulation change the intended process?
2. Did that process change improve the animal-welfare outcome?

## Evaluation

Evaluate the loop using:

- recovery of established causal factors in historical cases;
- citation accuracy and retrieval of contradictory evidence;
- expert judgment of whether hypotheses are falsifiable;
- expert judgment of measurement validity and experimental feasibility;
- reproduction of accepted analyses on known datasets;
- correct updating after positive, negative and unexpected results; and
- retrospective or prospective prediction of useful next experiments.

The final test is empirical: does the loop produce better-calibrated causal
knowledge and increasingly informative experiments?

## Boundary with intervention discovery

This pipeline may use an intervention as an experimental probe. Its primary
goal, however, is learning rather than retrieving a deployable technology.

Move into [intervention discovery](../intervention-discovery/README.md) when the
evidence is strong enough to describe the required change without hiding a
material unresolved causal assumption.
