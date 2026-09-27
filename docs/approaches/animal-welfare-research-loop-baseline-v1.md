# Animal Welfare Research Loop — Baseline v1

> **Status:** Exploratory approach; not implemented or validated  
> **Role in the wider project:** Candidate baseline for a mechanism-led scientific-discovery and technology-transfer loop

## Purpose
A simple baseline for adapting the Robin-style scientific discovery workflow to animal welfare problems.

## Core Flow

**Welfare problem**
→ **Possible causal mechanisms**
→ **Choose a measurable/testable process**
→ **Find interventions that could change that process**
→ **Test in the real world**
→ **Analyze results**
→ **Update the mechanism or intervention hypothesis**
→ **Test again**

## Direct Analogy to the Robin Pipeline

| Robin / biomedical version | Animal-welfare analogue |
|---|---|
| Disease | Welfare problem |
| Disease mechanism | Causal mechanism of suffering |
| Testable biological process | Measurable welfare-relevant process |
| Drug | Intervention / technology / management change |
| Cell experiment | Farm or controlled-animal trial |
| Biological outcome | Welfare outcome |
| New hypothesis | Revised mechanism or better intervention |

## Example: Broiler Footpad Dermatitis

### 1. Welfare problem
Broiler chickens develop footpad dermatitis.

### 2. Possible causal mechanisms
Examples might include:
- Wet litter
- Prolonged contact with moisture
- Irritating litter conditions
- Drinker leakage
- Poor ventilation or drying
- Other interacting husbandry factors

### 3. Choose a measurable process
Examples:
- Litter moisture
- Duration of exposure to wet litter
- Moisture at the bird-foot interface
- Frequency or severity of lesions

The key filter is: **can we measure this reliably enough to test whether an intervention changes it?**

### 4. Find interventions
Instead of looking for drugs, look for technologies or practices that could change the selected process.

Examples:
- Moisture sensors
- Leak detection
- Ventilation changes
- Litter-drying systems
- Litter additives
- Management changes
- Breeding/genetic interventions

### 5. Test
Run a controlled or on-farm experiment.

Ask two separate questions:
1. Did the intervention change the intended process?
2. Did changing that process actually improve animal welfare?

### 6. Analyze and loop
The result determines where to loop back.

- **Same mechanism, different intervention:** the process appears important, but the first intervention is weak.
- **Different process:** the intervention result suggests another measurable process may be more important.
- **Different causal mechanism:** strong evidence undermines the original explanation of the welfare problem.
- **Scale/adoption optimization:** the intervention works biologically, so search for a cheaper, easier, more scalable way to achieve the same effect.

## Mental Model

The workflow starts as a **funnel**:

**welfare problem → causes → testable process → interventions**

Once real experiments start, it becomes a **feedback loop**:

**hypothesis → experiment → result → analysis → updated hypothesis → next experiment**

The welfare problem normally stays fixed while the mechanism, process, and intervention hypotheses evolve.


## Agent Map by Step

The animal-welfare version can reuse the same **functional roles** as the FutureHouse/Robin setup, even if the implementation is adapted for welfare research.

| Step | Main agent role | What it does |
|---|---|---|
| 1. Define the welfare problem | **Orchestrator (Robin-like)** | Holds the overall research objective and coordinates the whole pipeline. |
| 2. Map possible causal mechanisms | **Broad literature scout (Crow-like)** | Searches animal-welfare, veterinary, husbandry, physiology, and related literature to identify plausible causes/mechanisms. |
| 3. Turn mechanisms into measurable/testable processes | **Crow-like scout + Orchestrator** | Finds ways each mechanism could be operationalized as something measurable in a lab, farm, sensor system, or controlled trial. |
| 4. Rank mechanisms / testable processes | **LLM judge / ranker** | Compares candidate mechanisms and experimental approaches, ideally pairwise, to decide which are most promising and tractable to investigate. |
| 5. Search for interventions | **Technology / Patent Scout** | Searches patents, products, engineering literature, adjacent industries, management practices, and biological interventions that could alter the chosen process. |
| 6. Deep-check each candidate intervention | **Deep evidence checker (Falcon-like)** | Investigates mechanism of action, prior evidence, practical constraints, failure modes, costs, safety, likely adoption barriers, and reasons the intervention may not work. |
| 7. Rank candidate interventions | **LLM judge / ranker** | Compares intervention candidates on evidence quality, expected welfare effect, technical feasibility, scalability, and other chosen criteria. |
| 8. Run experiment / field trial | **Human researchers / farm partners** | Physically implement the trial. The AI may help design the study, but real-world execution is still human-led. |
| 9. Analyze experimental data | **Data analyst (Finch-like)** | Writes/runs analysis code and analyzes sensor data, video, lesion scores, behavior, environmental measurements, or other trial outputs. |
| 10. Interpret the result and generate the next hypothesis | **Orchestrator + Crow/Falcon as needed** | Uses the new evidence to decide whether to try another intervention, investigate another process, revisit the mechanism, or run a mechanistic follow-up study. |
| 11. Repeat | **Orchestrator** | Routes the updated hypothesis back into the relevant part of the pipeline rather than necessarily restarting from the beginning. |

### Simplified Agent Flow

**Orchestrator**
→ **Crow-like broad research**
→ **Judge selects a mechanism/process**
→ **Technology/Patent Scout finds interventions**
→ **Falcon-like deep evidence review**
→ **Judge ranks interventions**
→ **Humans test**
→ **Finch-like analysis**
→ **Orchestrator updates the hypothesis**
→ **loop back to the appropriate stage**

### Important adaptation from FutureHouse

The biomedical system primarily searches for **therapeutic compounds**.

The animal-welfare system needs a wider intervention search space, including:

- Hardware
- Sensors and computer vision
- Environmental-control systems
- Housing/equipment changes
- Feed or biological interventions
- Genetics/breeding
- Management practices
- Monitoring and early-warning systems
- Existing commercial products
- Patented technologies from adjacent industries

That is why the **Technology / Patent Scout** is a distinct role in this version.




## Canonical Two-Track Architecture

The system should now be thought of as having **two main tracks** after the shared welfare-problem stage.

---

### Track 1 — Animal Welfare Hypothesis / Scientific Discovery

Use this when the main uncertainty is scientific:

> We do not yet know enough about the causal mechanism, or whether a proposed intervention really changes the welfare-relevant process.

#### Flow

**Welfare problem**
→ **Map possible causal mechanisms**
→ **Choose a testable process**
→ **Generate intervention hypotheses**
→ **Design experiment**
→ **Humans run experiment**
→ **Finch-like analysis**
→ **Update mechanism/intervention hypothesis**
→ **Repeat**

#### Endpoint

New empirical knowledge about:
- which mechanism matters;
- which intervention affects it;
- why an intervention worked or failed;
- what experiment should come next.

---

### Track 2 — Existing Technology / Technology Transfer

Use this when the main uncertainty is technological:

> We know enough about the welfare problem to ask whether an existing or lightly adaptable technology can solve it.

There are now **two valid sub-options** within this track.

---

#### Track 2A — Direct Function-to-Technology Search

Use this when the causal mechanism is already clear enough that it can be translated directly into a technical requirement.

#### Flow

**Welfare problem**
→ **Causal mechanism**
→ **Required functional change**
→ **Translate into engineering/technical requirements**
→ **Search patents, products, engineering literature, and adjacent industries**
→ **Match candidate technologies to requirements**
→ **Deep feasibility / due diligence**
→ **Rank candidates**
→ **Pilot or validate remaining uncertainty**
→ **Deploy / adapt**

#### Example

Footpad dermatitis
→ prolonged wet-litter exposure contributes to lesions
→ reduce or detect excessive moisture exposure
→ technical requirement: sense, prevent, or rapidly remove wetness
→ search moisture sensors, leak detection, drying systems, airflow control, absorbent materials, etc.

This is the **faster / shallower** path and should be used when the required function is already obvious.

---

#### Track 2B — Requisite-Condition Decomposition Before Technology Search

Use this when jumping directly from cause to technology would be too shallow.

Instead of asking only:

> “What technology addresses this cause?”

ask:

> “What conditions have to remain true for this harmful mechanism to continue?”

Then decompose the causal mechanism into smaller **necessary, enabling, or contributing conditions**.

#### Flow

**Welfare problem**
→ **Causal mechanism**
→ **Decompose into requisite conditions**
→ **Create one research/search thread per condition**
→ **Translate each condition into a technical function**
→ **Search patents, products, literature, and adjacent industries for each function**
→ **Collect candidate technologies**
→ **Recombine and compare candidates at the welfare-problem level**
→ **Deep feasibility / due diligence**
→ **Rank**
→ **Pilot / validate remaining uncertainty**
→ **Deploy / adapt**

#### Example: Footpad dermatitis

Causal mechanism:
**prolonged exposure to wet litter contributes to skin damage**

Possible requisite/enabling conditions:
- moisture accumulates;
- moisture persists rather than drying;
- birds remain exposed to the wet area;
- exposure reaches a damaging duration/intensity;
- the skin remains vulnerable to the moisture/chemical environment.

Each condition spawns a separate search:

- What technologies prevent moisture accumulation?
- What technologies detect local wetness early?
- What technologies accelerate drying?
- What technologies reduce exposure duration?
- What technologies protect tissue despite wet conditions?

The technology may come from an unrelated domain such as:
- greenhouse management;
- industrial drying;
- leak detection;
- construction moisture control;
- food processing;
- materials science;
- environmental sensing.

This is the **deeper / decompositional** path and is preferred when the mechanism is complex or the obvious technology search returns shallow results.

---

### Decision Rule Inside the Technology Track

Choose **Track 2A** when:
- the mechanism is well understood;
- the required function is obvious;
- existing technology categories are already visible.

Choose **Track 2B** when:
- the mechanism contains several interacting conditions;
- direct search produces generic or obvious technologies;
- the relevant solution may exist in a distant industry;
- we want to identify multiple intervention points rather than one.

Track 2B can also feed back into Track 2A:
once a requisite condition has been isolated, that condition can be treated as a well-specified function and searched directly.

---

### Overall Architecture

**Shared start:**
welfare problem → mechanism map

Then choose:

**Track 1 — Scientific / hypothesis discovery**
→ experiment-driven loop

or

**Track 2 — Existing technology**
→ choose either:

- **2A: direct function-to-technology search**
- **2B: requisite-condition decomposition → parallel function-specific technology searches**

Both tracks ultimately aim at:

**a scalable intervention that measurably improves animal welfare.**


## Shared vs Branch-Specific Agents

The system has **two downstream tracks** after the shared welfare-problem/mechanism stage:

1. **Animal Welfare Hypothesis / Scientific Discovery Track**
2. **Animal Welfare Existing-Technology / Technology-Transfer Track**

They share a common core, then diverge where the work becomes genuinely different.

### Shared core agents

Used in both tracks:

| Agent role | Main job |
|---|---|
| **Orchestrator (Robin-like)** | Coordinates the workflow, decides which stage comes next, and routes outputs into the correct branch or back to an earlier stage. |
| **Broad literature scout (Crow-like)** | Retrieves animal-welfare, veterinary, husbandry, engineering, and other relevant literature. |
| **Deep evidence reviewer (Falcon-like)** | Performs detailed evidence checks, identifies contradictory evidence, limitations, failure modes, and practical constraints. |
| **LLM judge / ranker** | Compares candidate mechanisms, processes, interventions, or technologies using explicit criteria and pairwise ranking where useful. |

### Track A — Animal Welfare Hypothesis / Scientific Discovery

Use when the main uncertainty is **scientific**: we do not yet know whether a mechanism or intervention relationship is true.

Additional roles:

| Agent role | Main job |
|---|---|
| **Mechanism / assay generator** | Converts causal hypotheses into measurable and experimentally testable processes. |
| **Experiment-design support agent** | Helps specify what experiment would discriminate between competing hypotheses. |
| **Finch-like data analyst** | Analyzes experimental, farm-trial, sensor, lesion-score, behavioral, or biological data. |
| **Hypothesis updater** | Uses new experimental results to revise the mechanism or intervention hypothesis and decide what should be tested next. |

Typical loop:

**mechanism hypothesis → testable process → intervention hypothesis → experiment → analysis → revised hypothesis → repeat**

### Track B — Animal Welfare Existing Technology / Technology Transfer

Use when the main uncertainty is **technological**: we know reasonably well what function needs to change, but not whether an existing technology can achieve it.

Additional roles:

| Agent role | Main job |
|---|---|
| **Patent / product scout** | Searches existing patents, commercial products, and known technologies. |
| **Adjacent-industry transfer scout** | Searches other industries for technologies that perform the same underlying function in a different context. |
| **Technical-requirements matcher** | Maps the welfare mechanism into engineering requirements and scores candidate technologies against them. |
| **Engineering feasibility reviewer** | Evaluates modification burden, environmental compatibility, cost, robustness, integration, maintenance, safety, and deployment constraints. |

Typical loop:

**required function → technical requirements → search → match → due diligence → pilot/deploy → refine requirements → search again**

### Evaluation rule

- For **shared/reused capabilities**, use the closest FutureHouse-style evaluation approach: retrieval benchmarks, citation checks, expert comparison, consistency testing, ablations, and end-to-end validation.
- For **new technology-transfer capabilities**, create custom benchmarks specific to the job: known-solution retrieval, patent/product recall, technical-fit classification, feasibility-review agreement with engineers, and retrospective/pilot outcome validation.

### Current architecture in one line

**Shared front end:** welfare problem → mechanisms → required change

Then branch to either:

**A. Scientific discovery:** hypothesis → experiment → evidence → revised hypothesis

or:

**B. Existing technology:** requirements → technology search → fit/due diligence → pilot/deploy


## Benchmark and Evaluation Layer

The animal-welfare system should not rely only on an LLM judge saying that an output "looks good." Each major stage should have an evaluation that is as close as possible to external ground truth.

### Evaluation map by agent / stage

| Stage / agent | Suggested benchmark or eval | What counts as ground truth |
|---|---|---|
| **Crow-like broad literature scout** | Give it known welfare questions with expert-curated reference sets; measure whether it retrieves the key papers, correctly states their findings, and avoids nonexistent citations. | Expert-curated literature set; citation existence; factual agreement with source text. |
| **Mechanism-generation stage** | Use welfare problems where the important causal factors are already reasonably well established. Hide the expert answer and ask the system to reconstruct the mechanism map. | Veterinary/welfare review articles, expert causal maps, consensus evidence. |
| **Testable-process stage** | Ask whether the proposed process is actually measurable, causally relevant, and experimentally manipulable. Have domain experts independently score proposals. | Expert judgment plus existence of validated measures/assays/sensors. |
| **LLM mechanism/process ranker** | Compare its pairwise rankings against blinded rankings from animal-welfare/veterinary experts; measure agreement and repeatability across repeated runs. | Expert rankings and internal consistency. |
| **Technology / Patent Scout** | Create a set of known technologies or patents relevant to specific welfare mechanisms and test retrieval recall, precision, and novelty. Include "adjacent-industry" examples that require non-obvious transfer. | Patent databases, product catalogues, known prior-art sets, expert relevance labels. |
| **Falcon-like deep evidence checker** | Give it candidate interventions with known evidence profiles and test whether it correctly identifies supporting evidence, contradictory evidence, limitations, costs, and failure modes. | Expert evidence review; source-level verification; known trial outcomes. |
| **Intervention ranker** | Compare AI rankings with rankings from blinded experts using an explicit rubric: expected welfare impact, technical feasibility, cost, adoption probability, evidence quality, scalability, and neglectedness. | Expert rankings plus later real-world outcomes where available. |
| **Finch-like data analyst** | Give it previously completed farm trials or experimental datasets where the accepted analysis/result is known. Test whether it reproduces the main statistical conclusions and detects known data-quality issues. | Gold-standard analysis scripts/results; expert-reviewed conclusions. |
| **Experiment interpretation stage** | Hide the known follow-up from historical studies and ask the system what experiment or intervention should come next. Compare with what experts chose and with actual later evidence. | Historical follow-up studies, expert proposals, subsequent experimental results. |
| **Orchestrator / routing** | Run end-to-end simulated research tasks and test whether it sends failures back to the correct level: drug/intervention, measurable process, or causal mechanism. | Expert-labelled routing decisions and task-completion outcomes. |

### Analogue of the FutureHouse ablation test

FutureHouse tested whether specialist agents actually added value by removing them and checking what got worse.

We should do the same.

Examples:

- Remove the **literature scout** and use a general LLM → does citation accuracy or mechanism quality fall?
- Remove the **patent/technology scout** → does the system miss relevant engineering interventions?
- Remove the **deep evidence checker** → do weak or impractical interventions rank too highly?
- Replace the **Finch-like analyst** with a one-shot LLM → does statistical accuracy fall?
- Remove repeated/independent analyses → does the result become less stable?
- Remove the **judge/ranker** → does the pipeline spend more experiments on low-value candidates?

This tells us whether each specialised component genuinely improves the system rather than merely adding complexity.

### Benchmark types we would want

#### 1. Retrieval benchmarks
Measure:
- key-paper recall
- citation precision
- hallucinated citation rate
- retrieval of contradictory evidence
- retrieval of non-obvious adjacent-domain evidence

#### 2. Mechanism benchmarks
Measure:
- whether known causal factors are recovered
- whether causal direction is represented correctly
- whether necessary versus contributing causes are distinguished
- whether unsupported mechanisms are introduced
- whether the mechanism map is complete enough to support intervention search

#### 3. Experimental-design benchmarks
Measure:
- testability
- sensitivity of the proposed measure
- whether the measure is actually connected to animal welfare
- feasibility in farm/lab conditions
- robustness to confounding

#### 4. Intervention-discovery benchmarks
Measure:
- recall of known effective interventions
- ability to reject known failures
- ability to identify technically plausible novel transfers from other industries
- patent/product retrieval quality
- novelty without sacrificing plausibility

#### 5. Data-analysis benchmarks
Measure:
- reproduction of accepted statistical results
- correct handling of missing data and outliers
- correct treatment of clustered farm/pen-level data
- calibration of uncertainty
- reproducibility across independent agent runs

#### 6. Ranking benchmarks
Measure agreement with expert pairwise judgments on dimensions such as:
- expected suffering reduction
- technical solvability
- adoption probability
- scalability
- cost
- evidence strength
- neglectedness

Agreement with experts should not be treated as perfect ground truth, but it is useful calibration.

### End-to-end evaluation

The most important evaluation is not whether intermediate text "sounds scientific."

For a full research cycle, ask:

1. Did the system identify a genuinely important welfare mechanism?
2. Did it choose a measurable process that tracks the welfare problem?
3. Did it retrieve an intervention that should plausibly move that process?
4. Did the real experiment show that the intervention changed the process?
5. Did that change improve the animal-welfare outcome?
6. Did the system correctly update its next hypothesis based on the result?
7. Did later iterations outperform earlier ones?

That final sequence is the closest analogue to the **experimental reality check** in Robin.

### Retrospective benchmark dataset

Before running expensive new farm trials, build a historical benchmark from already-published cases.

For each case, freeze the literature at some past date and ask the system to operate only on information available up to that point.

Then test whether it can predict or reconstruct:

- the important mechanism later supported by evidence;
- an intervention later shown to work;
- an intervention later shown not to work;
- the most useful next experiment;
- known adoption or implementation barriers.

This gives us a form of **time-split evaluation**: the system cannot simply retrieve the later answer because those later papers are withheld.

### Prospective validation

Once the retrospective benchmark is credible, move to prospective tests:

**AI proposes intervention → preregister prediction → run trial → compare prediction with outcome.**

Record in advance:
- expected direction of effect;
- expected effect size or range where possible;
- confidence;
- failure conditions;
- which mechanism is supposed to mediate the effect.

This makes it possible to measure calibration rather than judging success after the fact.

### Evaluation principle

Use different kinds of truth at different levels:

**source text** for literature claims  
→ **expert consensus** for mechanism/ranking calibration  
→ **known datasets** for analysis accuracy  
→ **historical outcomes** for retrospective discovery benchmarks  
→ **new experiments and welfare outcomes** for final prospective validation

The closer we get to the end of the pipeline, the less we should rely on LLM judgment and the more we should rely on external empirical evidence.

## Open Questions for v2

- How should candidate welfare problems be selected before entering the loop?
- How should mechanisms be ranked?
- What should count as a sufficiently measurable process?
- How should patents and existing technologies enter the intervention search?
- How should tractability, adoption probability, suffering reduction, and neglectedness affect ranking?
- When should the loop move from biological efficacy to implementation/adoption optimization?

