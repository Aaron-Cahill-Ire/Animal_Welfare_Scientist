# Animal Welfare Scientist Approaches

> **Status:** Exploration and comparison. No pipeline has been selected for
> implementation.

The design space is organised by **objective first**, then by method. This
prevents a complete research loop, a search pipeline and a retrieval module
from being presented as though they were equivalent alternatives.

## Two approach families

| Family | Use it when | Primary output |
|---|---|---|
| [Scientific discovery](scientific-discovery/README.md) | The important causal mechanism is uncertain, or the relationship between a process and welfare needs experimental testing. | Better-supported or rejected hypotheses and a useful next experiment. |
| [Intervention discovery](intervention-discovery/README.md) | The problem is understood well enough to state what should change. | Evidence-traceable intervention candidates for review or testing. |

The families share the evidence, review and evaluation rules in
[shared foundations](shared-foundations.md).

## Routing rule

```text
welfare problem
    -> define the harm and context
    -> review the available causal evidence
    -> can we state what must change?

       no or uncertain -> scientific discovery
       yes             -> intervention discovery
```

The route is not permanent. Scientific work may establish a process that can
then enter intervention discovery. A failed intervention may expose a weak
mechanism assumption and send the work back to scientific discovery.

## Intervention-discovery methods

| Method | Main strength | Important boundary |
|---|---|---|
| [Direct functional search](intervention-discovery/direct-functional-search.md) | Fast search when a required function is already clear. | May return obvious or shallow candidates. |
| [Welfare Technology Scanner](intervention-discovery/welfare-technology-scanner/README.md) | Deep, evidence-gated causal decomposition before technology search. | Necessary-condition rules may exclude important contributory factors. |
| [Jev case-analogy retrieval](intervention-discovery/jev-case-analogy-retrieval.md) | Generates cross-domain leads from similar problem profiles. | Similar welfare outcomes do not establish compatible mechanisms. |

The Jev method is an optional candidate generator. It needs a source library
and downstream scientific, engineering, safety and ethical review. It is not a
replacement for the complete discovery workflow.

## How to compare approaches

Apply the same questions:

1. **Purpose:** What decision or discovery task does it improve?
2. **Pipeline:** What are its stages, inputs, outputs and feedback loops?
3. **Division of labour:** What belongs to an LLM, search, deterministic code or
   a person?
4. **Evidence:** How are source claims, context, uncertainty and provenance
   retained?
5. **Safety:** How is an interesting candidate prevented from being mistaken
   for a validated intervention?
6. **Feasibility:** What data, tools and human expertise are required?
7. **Evaluation:** What backtest or prospective test could disconfirm its value?

## Preserved source material

The original combined
[Animal Welfare Research Loop — Baseline v1](../../archive/historical-designs/animal-welfare-research-loop-baseline-v1.md)
is preserved unchanged. The current scientific-discovery, direct-search and
shared-foundation documents make its distinct roles easier to inspect.

[AI research-system precedents](../research/ai-scientist-precedents.md) are
background research, not additional approach candidates.
