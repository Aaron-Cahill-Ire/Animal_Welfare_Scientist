# Shared Foundations

> **Status:** Exploratory cross-cutting rules; not implemented or validated

Scientific discovery and intervention discovery have different objectives, but
they require the same disciplined foundation.

## Shared start

Every run begins by defining:

- the animal population and context;
- the welfare harm in scope;
- the timeframe and exclusions;
- the evidence already available;
- the causal or functional uncertainty being investigated; and
- the decision the run is intended to support.

The system then decides whether the immediate need is better scientific
understanding or an intervention search. If the evidence is insufficient to
route confidently, it should record the uncertainty and begin with bounded
scientific work.

## Shared rules

### Evidence and provenance

- Retain the source, relevant passage or result, context and retrieval date for
  every material claim.
- Keep sourced findings separate from model inference and human judgment.
- Preserve supporting, contradictory and inconclusive evidence.
- Treat incomplete search coverage as uncertainty, not negative evidence.

### Human review

- People approve material causal assumptions before they control downstream
  work.
- People review candidate interventions before testing or practical use.
- No LLM output by itself establishes scientific validity, safety, efficacy,
  novelty or ethical acceptability.

### Uncertainty and abstention

- Missing information must not silently become evidence of absence.
- Weak or conflicting evidence should produce an unresolved state.
- A stage should stop or request more evidence when its minimum evidence bar is
  not met.

### Structured handoffs

Every handoff should identify:

- the producing stage;
- the exact input and output versions;
- the claims and evidence used;
- unresolved assumptions;
- the human decisions already made; and
- the permitted next action.

## Shared evaluation principle

Use the closest available external ground truth at each stage:

```text
source text
    -> expert-reviewed causal knowledge
    -> known datasets and analysis results
    -> historical intervention outcomes
    -> new experiments and welfare outcomes
```

Useful evaluations include:

- retrieval recall and citation accuracy;
- reconstruction of established causal mechanisms;
- expert review of testability and causal relevance;
- recovery of known effective and ineffective interventions;
- rejection of unsafe or functionally incompatible transfers;
- reproduction of accepted analyses;
- retrospective time-split tests; and
- preregistered prospective experiments.

The closer a claim is to practical deployment, the less it should depend on
LLM judgment and the more it should depend on empirical evidence and qualified
human review.

## Relationship between the families

```text
scientific discovery
    -> establishes or revises what process matters
    -> hands a supported required change to intervention discovery

intervention discovery
    -> finds and reviews candidate ways to cause that change
    -> returns failures or contradictory results to scientific discovery
```

The original combined reasoning and detailed benchmark proposals remain in the
archived
[Research Loop baseline](../../archive/historical-designs/animal-welfare-research-loop-baseline-v1.md).
