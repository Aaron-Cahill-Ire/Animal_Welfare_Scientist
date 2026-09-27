Here’s a PRD you could hand directly to yourself, a collaborator, or a coding agent.

# WelfareTech Explorer

## 1. Product Summary

WelfareTech Explorer is an AI-assisted research system for discovering, evaluating, and prioritising novel technologies that could materially improve the welfare of farmed pigs, chickens, and fish.

The system is inspired by Ambitious Impact’s research funnel, but shifts the starting point earlier.

Instead of beginning with a predefined list of interventions, WelfareTech Explorer will:

1. Map important welfare problems.
2. Identify measurable indicators and current interventions.
3. Search for relevant technologies both within and outside animal agriculture.
4. Generate novel problem × technology combinations.
5. Search papers, patents, products, startups, and organisations for prior art.
6. Eliminate ideas that are crowded, infeasible, low-impact, or unlikely to be adopted.
7. Progress promising ideas through increasingly expensive research stages.

The ultimate output is a small number of high-quality, evidence-backed welfare technology opportunities worth building, funding, researching, or investigating further.

---

# 2. Problem

There are large numbers of farmed animals experiencing serious welfare problems, but identifying useful technological interventions is difficult.

Existing research processes have several limitations:

- Welfare problems and technologies are documented across disconnected literatures.
- Researchers tend to search within their own field rather than across industries.
- Many “innovative” ideas already exist as academic prototypes, patents, commercial products, or abandoned projects.
- AI brainstorming tends to produce obvious ideas such as computer-vision monitoring.
- Technologies that measure welfare do not necessarily improve welfare.
- It is difficult to systematically compare hundreds of possible interventions.
- Deep research is expensive, so most ideas cannot receive equal attention.

There may therefore be valuable technologies sitting in the gap between:

**important welfare problem × available technical capability × limited existing adoption**

WelfareTech Explorer is intended to systematically search this space.

---

# 3. Primary Objective

Discover genuinely promising and relatively neglected technological interventions that could substantially improve the welfare of farmed:

- pigs
- chickens
- fish

The system should maximise the probability of finding interventions that score highly on:

**animals affected × welfare improvement × technical feasibility × adoption probability × neglectedness**

Novelty alone is not sufficient.

---

# 4. Secondary Objective

Use WelfareTech Explorer as an experimental platform for understanding how AI research systems should be designed.

The system should make it possible to test:

- different prompts
- different models
- different search strategies
- different research agents
- different graph structures
- different ranking methods
- different stopping rules
- parallel vs sequential research
- cross-domain analogy generation
- different novelty-checking procedures

The longer-term goal is to optimise the research process using evaluation data.

---

# 5. Non-Goals

Version 1 is not intended to:

- autonomously start companies
- perform laboratory research
- replace domain experts
- prove that an invention is patentable
- generate engineering-ready hardware designs
- provide definitive animal-welfare assessments
- cover all farmed species
- automatically fund or deploy interventions

The initial system is a research and prioritisation engine.

---

# 6. Target Users

## Primary

### Welfare technology entrepreneur

Wants to identify a high-impact project or company worth pursuing.

### Animal-welfare researcher

Wants to identify neglected technological opportunities.

### Grantmaker / incubator

Wants to identify projects worth further investigation or funding.

### Independent researcher

Wants a systematic method for searching the welfare-tech opportunity space.

## Initial user

The initial product should be optimised for a single technically literate researcher using the system interactively.

Multi-user features are not required for v1.

---

# 7. Core Research Model

The system should represent opportunities using a structured research graph.

Core entities:

```text
Species
↓
Production system
↓
Production stage
↓
Welfare problem
↓
Welfare consequence
↓
Observable indicator
↓
Existing mitigation
↓
Remaining bottleneck
↓
Technology primitive
↓
Potential intervention
↓
Evidence
↓
Existing work / prior art
↓
Evaluation
```

Example:

```text
Pig
↓
Transport
↓
Heat stress
↓
Respiratory distress / mortality / suffering
↓
Temperature + humidity + behavioural indicators
↓
Ventilation / scheduling
↓
Poor continuous welfare visibility
↓
Environmental sensing + acoustic analysis
↓
Trailer welfare monitoring system
```

---

# 8. Species Scope

## Pigs

Examples include:

- piglet crushing
- tail biting
- aggression
- lameness
- respiratory problems
- heat stress
- enrichment deficiencies
- handling
- loading
- transport
- slaughter
- stunning failures

## Chickens

Initial focus should include broilers and laying hens.

Examples:

- lameness
- footpad dermatitis
- keel-bone damage
- feather pecking
- overcrowding
- heat stress
- litter quality
- catching
- loading
- transport
- slaughter
- ineffective stunning

## Fish

Fish should not be represented as one homogeneous biological category.

The graph should support species-level distinctions.

Initial candidates may include:

- Atlantic salmon
- rainbow trout
- tilapia
- carp

Problems include:

- hypoxia
- crowding
- injury
- parasitic infection
- handling
- grading
- transport
- water-quality stress
- disease
- slaughter

---

# 9. Core Workflow

## Stage 1 — Welfare Problem Mapping

### Goal

Construct a structured ontology of important welfare problems.

### Agent responsibilities

Search:

- academic reviews
- welfare assessments
- NGO reports
- veterinary literature
- industry guidance
- government documents

Extract:

- species
- production stage
- welfare issue
- prevalence
- severity
- duration
- animals affected
- known causes
- measurable indicators
- current mitigation
- remaining bottlenecks

### Output

A structured welfare-problem database.

---

# 10. Stage 2 — Bottleneck Identification

The system should distinguish between the existence of a welfare problem and the reason it remains unsolved.

Possible bottlenecks:

- cannot detect problem reliably
- detection is too expensive
- detection occurs too late
- intervention requires labour
- intervention is technically difficult
- farmer incentives are weak
- intervention lowers productivity
- regulation is absent
- intervention cannot scale
- no suitable hardware exists
- existing hardware is unreliable
- individual animals cannot be identified
- environmental conditions interfere with sensing
- intervention exists but adoption is low

Output:

```text
Problem
Current solution
Why current solution is insufficient
Primary bottleneck
Confidence
Evidence
```

---

# 11. Stage 3 — Technology Primitive Mapping

Instead of searching only for agricultural technologies, the system should build a broad library of technical capabilities.

Examples:

- RGB computer vision
- thermal imaging
- radar
- lidar
- acoustic sensing
- vibration sensing
- sonar
- hyperspectral imaging
- biosensors
- wearable sensors
- environmental sensors
- robotics
- soft robotics
- automated control systems
- microfluidics
- digital twins
- anomaly detection
- time-series forecasting
- reinforcement learning
- edge computing
- smart materials
- automated inspection systems

Each primitive should include:

- what it measures or controls
- cost characteristics
- maturity
- environmental limitations
- industries using it
- relevant example applications

---

# 12. Stage 4 — Cross-Domain Analogy Search

This is one of the most important components.

The system should search for structurally similar problems outside animal agriculture.

Example:

```text
Welfare problem:
Detect abnormal locomotion among thousands of chickens.

Analogous problems:
- human gait diagnostics
- athlete injury detection
- airport crowd analysis
- warehouse safety monitoring
- wildlife tracking
```

The agent should ask:

> What technological capability used elsewhere solves an analogous sensing, prediction, control, or intervention problem?

Output:

```text
Welfare problem
External domain
Analogous problem
Technology used
Transfer hypothesis
Reason transfer may work
Likely barriers
```

---

# 13. Stage 5 — Candidate Invention Generation

Candidate interventions should be generated from structured inputs rather than unconstrained brainstorming.

Inputs:

- welfare problem
- bottleneck
- observable indicator
- technology primitive
- cross-domain analogy
- deployment environment
- adoption constraints

The invention agent proposes a concrete intervention.

Example output:

```text
Name:
Trailer Welfare Black Box

Problem:
Pig heat stress and injury during transport.

Intervention:
Low-cost sensor unit combining environmental sensing, vehicle vibration and acoustic analysis to identify periods of likely welfare deterioration.

Mechanism:
Detect dangerous conditions and associate them with journey segments and handling practices.

Potential user:
Transport company / integrator / processor.

Expected welfare pathway:
Detection → accountability / intervention → improved transport practices.
```

---

# 14. Stage 6 — Prior-Art / Novelty Search

Every candidate invention must undergo an aggressive search for existing work.

Search sources should eventually include:

- Google Scholar / scholarly databases
- Crossref / OpenAlex
- patents
- Google Patents
- Espacenet where practical
- company websites
- startup databases
- NGO reports
- agricultural equipment companies
- university projects
- conference papers
- research grants

The system should explicitly search multiple terminology variants.

For every idea determine:

- exact solution already exists
- close substitute exists
- academic prototype exists
- patent exists
- adjacent product exists
- previous attempt failed
- apparently unexplored
- insufficient evidence to determine novelty

Novelty should never be inferred simply because the first search found nothing.

---

# 15. Stage 7 — Novelty Assassin

A specialised adversarial agent should attempt to eliminate the idea.

It should search for:

- existing competitors
- existing patents
- equivalent interventions under different terminology
- technical failure modes
- biological invalidity
- measurement problems
- adoption problems
- welfare trade-offs
- cost barriers
- incentives against deployment
- existing superior solutions

Its objective is:

> Find the strongest reason this opportunity is not worth pursuing.

Output:

```text
Strongest objection
Evidence
Severity
Can objection be mitigated?
Revised confidence
Recommendation
```

---

# 16. Stage 8 — Quick Prioritisation

Surviving ideas enter an AIM-inspired prioritisation stage.

Approximate research budget:

**5–15 minutes per idea**

Score:

### Scale

How much suffering could potentially be reduced?

### Welfare magnitude

How substantial is the expected improvement per affected animal?

### Technical tractability

Can the intervention plausibly work?

### Adoption probability

Would relevant actors realistically use it?

### Neglectedness

How little serious work is currently being done?

### Scalability

Can the solution reach large numbers of animals?

### Additionality

Would the intervention produce welfare improvement that would otherwise not occur?

### Evidence strength

How strong is the evidence behind key assumptions?

### Information value

How valuable would further investigation be?

Output:

**Reject / Hold / Shallow Dive**

---

# 17. Stage 9 — Shallow Dive

Target research time:

**approximately 1–2 hours equivalent research effort per idea**

Investigate:

- size of affected animal population
- welfare severity
- biological mechanism
- existing technologies
- existing companies
- patents
- research activity
- technical feasibility
- rough economics
- likely purchaser
- adoption incentives
- regulation
- implementation barriers
- welfare risks
- key uncertainties

Output should be a concise research memo.

Decision:

**Reject / Hold / Deep Dive**

---

# 18. Stage 10 — Deep Dive

Deep dives are reserved for approximately the top 1–5% of generated ideas.

Research may include:

- comprehensive literature review
- patent landscape
- competitor analysis
- expert interviews
- cost-effectiveness model
- engineering feasibility assessment
- deployment pathway
- adoption analysis
- stakeholder incentives
- regulatory analysis
- prototype specification
- experimental validation plan

Output:

A decision-quality opportunity report.

---

# 19. Funnel

Initial target:

```text
1,000 problem × technology hypotheses

        ↓

300 plausible interventions

        ↓

100 surviving novelty checks

        ↓

30 quick-prioritisation survivors

        ↓

10 shallow dives

        ↓

3 deep dives

        ↓

1–3 opportunities worth acting on
```

Exact thresholds should be configurable.

---

# 20. Research Agents

Initial agents:

## Problem Mapper

Builds and updates welfare ontology.

## Bottleneck Analyst

Determines why each welfare problem persists.

## Technology Scout

Finds relevant technological capabilities.

## Analogy Agent

Searches other industries for structurally similar problems.

## Invention Agent

Generates candidate interventions.

## Literature Researcher

Searches academic literature.

## Patent Researcher

Searches prior art.

## Commercial Landscape Agent

Finds companies and existing products.

## Novelty Assassin

Attempts to invalidate novelty.

## Technical Skeptic

Looks for engineering and biological failure modes.

## Adoption Analyst

Models incentives and barriers to deployment.

## Welfare Evaluator

Estimates likely welfare consequences.

## Prioritisation Agent

Ranks opportunities.

## Evidence Auditor

Checks claims against supporting sources.

## Synthesis Agent

Produces final research memos.

---

# 21. Agent Design Principle

Agents should not simply communicate using unrestricted prose.

Where practical, outputs should use structured schemas.

Example:

```json
{
  "claim": "No automated pig-transport welfare system was identified",
  "claim_type": "literature_gap",
  "confidence": 0.74,
  "sources": [],
  "search_queries": [],
  "counterevidence": [],
  "requires_verification": true
}
```

This allows claims to be:

- inspected
- challenged
- updated
- evaluated
- traced to sources

---

# 22. Evidence Requirements

Every material factual claim should be source-backed.

The system must distinguish:

- directly supported fact
- source author claim
- system inference
- speculative hypothesis

Every intervention should expose:

- supporting evidence
- contradictory evidence
- confidence
- unresolved uncertainties

The system must not interpret “no result found” as evidence that no prior art exists.

---

# 23. User Interface — MVP

The initial UI can be minimal.

Primary screens:

## Opportunity Explorer

Table containing:

- idea
- species
- welfare problem
- technology
- stage
- novelty score
- impact score
- tractability score
- neglectedness score
- confidence
- recommendation

## Opportunity Page

Shows:

- intervention description
- causal pathway
- sources
- existing work
- critic arguments
- scoring
- research history
- unresolved questions

## Research Graph

Visualises:

```text
welfare problem
→ bottleneck
→ technology
→ analogy
→ candidate solution
→ evidence
```

## Research Queue

Shows opportunities awaiting:

- novelty checking
- quick evaluation
- shallow dive
- deep dive

---

# 24. Human-in-the-Loop Controls

Users should be able to:

- approve/reject ideas
- alter scores
- flag bad evidence
- request further research
- freeze particular assumptions
- promote an idea manually
- add new problems
- add technologies
- provide expert evidence

The system should preserve human decisions separately from model-generated ones.

---

# 25. Data Model

Core objects:

### Species

### ProductionSystem

### ProductionStage

### WelfareProblem

### WelfareIndicator

### Bottleneck

### TechnologyPrimitive

### ExternalAnalogy

### CandidateIntervention

### Source

### Claim

### PriorArt

### Evaluation

### ResearchRun

### AgentOutput

### HumanDecision

Relationships should form a queryable graph even if the MVP initially stores them relationally.

---

# 26. Technical Architecture — MVP

Suggested architecture:

```text
Python
+
PostgreSQL
+
LLM APIs
+
search/retrieval tools
+
background research jobs
+
simple web interface
```

Possible UI:

- Streamlit for fastest experimentation

or

- Next.js if the system is expected to evolve into a richer product

The research engine should remain separate from the frontend.

---

# 27. Research Pipeline

Conceptually:

```python
problems = map_welfare_problems()

for problem in problems:

    bottlenecks = identify_bottlenecks(problem)

    technologies = retrieve_candidate_technologies(
        problem,
        bottlenecks
    )

    analogies = search_cross_domain_analogies(
        problem,
        technologies
    )

    ideas = generate_interventions(
        problem,
        bottlenecks,
        technologies,
        analogies
    )

    for idea in ideas:

        prior_art = search_prior_art(idea)

        criticism = attack_idea(
            idea,
            prior_art
        )

        if survives(idea, criticism):

            evaluation = quick_prioritise(idea)

            if evaluation.advance:
                queue_shallow_dive(idea)
```

---

# 28. Research Provenance

Every research run should save:

- prompt
- model
- tools used
- queries performed
- retrieved sources
- intermediate outputs
- scores
- decisions
- timestamps
- parent research node

This is essential for later evaluation.

---

# 29. Evaluation System

The system should eventually measure whether different research configurations produce better discoveries.

Possible evaluation datasets:

### Historical backtesting

Give the system only evidence available before a cutoff year.

Test whether it identifies technologies that subsequently became important.

### Expert evaluation

Ask animal-welfare and technical experts to independently rate generated opportunities.

### Known intervention recovery

Hide known strong interventions and test whether the system independently discovers them.

### Novelty benchmark

Include:

- obviously existing products
- obscure patented ideas
- genuinely unusual combinations

Measure whether novelty search correctly distinguishes them.

### Citation accuracy

Check whether cited sources actually support generated claims.

---

# 30. Metrics

## Discovery quality

- proportion judged genuinely interesting
- proportion genuinely novel
- proportion worth further investigation
- expert ratings

## Research efficiency

- useful discoveries per £ of model/search cost
- useful discoveries per research hour
- percentage eliminated before expensive research

## Evidence quality

- citation correctness
- unsupported-claim rate
- contradictory evidence discovered

## Funnel quality

- false-negative rate
- false-positive rate
- ranking correlation with expert judgement

## Novelty

- distance from existing products/research
- number of close prior-art matches

---

# 31. Experimentation Framework

Every pipeline component should eventually be configurable.

Example experiment:

### Hypothesis

Cross-domain analogy improves novel idea generation.

### Control

Generate intervention directly from welfare problem.

### Treatment

Generate analogous external-industry problems first, then generate intervention.

### Evaluation

Blind expert scoring of:

- novelty
- plausibility
- welfare impact
- usefulness

This turns WelfareTech Explorer into both a practical research system and a research project on AI-assisted scientific/strategic discovery.

---

# 32. MVP

Version 0.1 should not attempt the full autonomous research system.

Build only:

### A. Welfare ontology

Pigs, chickens and selected fish species.

### B. Bottleneck mapping

Structured descriptions of why important problems remain unresolved.

### C. Technology primitive library

Approximately 50–100 technical capabilities.

### D. Cross-domain analogy agent

Given a welfare problem, retrieve analogous external problems and technologies.

### E. Intervention generator

Generate structured candidate interventions.

### F. Basic novelty search

Search academic literature, patents and commercial products.

### G. Research table

Save and compare generated ideas.

Success means the system produces **several non-obvious ideas that survive manual prior-art investigation**.

---

# 33. MVP Success Criterion

The MVP succeeds if, after generating and investigating approximately 100–300 candidate interventions:

- at least 5 seem meaningfully non-obvious
- at least 3 survive a serious prior-art search
- at least 1 is judged worth a human-led shallow dive

The system does not need to discover a successful company idea immediately.

It needs to demonstrate that the discovery process generates valuable search directions more efficiently than ordinary brainstorming.

---

# 34. First Implementation Milestones

## Milestone 1

Define schemas and ontology.

Deliverable:

```text
species
→ production stage
→ welfare problem
→ indicator
→ mitigation
→ bottleneck
```

## Milestone 2

Populate welfare map from reliable sources.

## Milestone 3

Build technology-primitive database.

## Milestone 4

Build analogy-generation workflow.

## Milestone 5

Generate first 100 candidate interventions.

## Milestone 6

Implement automated literature + prior-art searches.

## Milestone 7

Run novelty assassin against all candidates.

## Milestone 8

Manually review top 20.

## Milestone 9

Perform AIM-style shallow dives on top 5–10.

---

# 35. Key Risks

## Hallucinated novelty

The system concludes something is new because it searched poorly.

Mitigation:

Multiple search agents, terminology expansion and explicit uncertainty.

## Obvious ideas dominate

Models repeatedly propose cameras, sensors and dashboards.

Mitigation:

Cross-domain analogy generation and diversity constraints.

## Proxy optimisation

The system identifies technologies that measure welfare without improving it.

Mitigation:

Every intervention must contain an explicit causal pathway from deployment to reduced suffering.

## Productivity mistaken for welfare

Agricultural technology may improve production while having ambiguous welfare consequences.

Mitigation:

Separate welfare outcomes from productivity outcomes.

## Adoption ignored

Technically impressive solutions may never be deployed.

Mitigation:

Adoption probability is a first-class evaluation dimension.

## Fish treated too generically

Different fish species have different welfare requirements.

Mitigation:

Species-specific ontology.

## Research graph becomes overly complex

Agent infrastructure could become the project instead of welfare discovery.

Mitigation:

Begin with a very small pipeline and add agents only when evaluations demonstrate value.

---

# 36. Central Product Principle

The system is not trying to generate the cleverest invention.

It is trying to repeatedly answer:

> **What important source of animal suffering appears technically solvable, insufficiently addressed, scalable, and worth investigating now?**

Everything in the architecture should serve that question.

---

# 37. Long-Term Vision

WelfareTech Explorer becomes a continuously updating map of technological opportunities for animal welfare.

New research, patents and companies continuously modify the opportunity graph.

The system identifies:

- newly solvable problems
- emerging technologies
- abandoned approaches worth revisiting
- cross-industry technologies becoming cheap enough for agriculture
- overlooked welfare bottlenecks
- gaps between measurement and intervention
- potentially fundable research programmes
- startup opportunities
- public-goods datasets and infrastructure

Eventually the same research architecture could be applied to other high-impact domains.

The first test case is farmed-animal welfare because it contains enormous welfare stakes, heterogeneous technical problems, substantial existing research, and many potentially underexplored opportunities.

The first thing I’d implement from this is **not the multi-agent architecture**. I’d build the structured welfare ontology and get roughly 50–100 high-quality problem/bottleneck records across pigs, chickens and fish; that becomes the substrate we can evaluate every subsequent agent against.
