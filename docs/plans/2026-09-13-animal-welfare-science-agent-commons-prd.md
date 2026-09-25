# Animal Welfare Science Agent Commons — Product Requirements Document

Created: 2026-09-13

Revised: 2026-09-13 — breadth-first prototype portfolio across all three research tracks. This revision replaces the earlier two-agent first-release strategy; the Scout and Auditor remain the first priority for deeper evaluation.

## 1. Product summary

The Animal Welfare Science Agent Commons is a public, evidence-led catalogue and development programme for AI agents that can accelerate animal-welfare research and the translation of that research into practical interventions.

The first product will be a simple website backed by GitHub. It will help researchers and builders:

- discover existing agents and adjacent tools;
- understand which research tasks each agent can and cannot perform;
- compare agents using shared benchmarks;
- identify important capabilities that do not yet exist;
- access documented, versioned agent repositories;
- contribute new agents, evaluations, datasets and failure reports; and
- connect promising agents with researchers for validation in real studies.

The programme will build a bounded, runnable first version of every agent in the initial portfolio, organised across solution discovery, applied R&D, and basic research/research integrity. Shared interfaces will let agents run independently or work together. Initial implementations will be published as prototypes and refined using benchmarks, researcher feedback and observed failures. The Solution and Prior-Art Scout and Evidence and Claim Auditor receive deeper evaluation first.

The existing WelfareTech Explorer PRD becomes the first major application family within the Commons: **solution and opportunity discovery**.

## 2. Vision

Make reliable, reusable AI research capabilities available to animal-welfare scientists so that more important questions are identified, tested and translated into welfare improvements.

The long-term system should support three connected tracks:

1. **Discover deployable solutions:** identify existing technologies, prototypes and interventions that could address important welfare problems but have not yet been applied.
2. **Accelerate applied R&D:** help researchers move from a decision-relevant hypothesis through protocol design, experimentation, analysis, updated beliefs and prototype development.
3. **Accelerate basic research:** reduce the cost of evidence synthesis, measurement development, data analysis, reproducibility and research administration without replacing scientific judgement.

The product is not intended to automate science end to end. It should make bounded research tasks faster and more reliable while keeping responsibility, ethical judgement and high-consequence decisions with qualified humans.

## 3. Problem

Potentially useful AI agents, scripts, models and research tools are scattered across GitHub, papers, commercial products and private projects. Researchers cannot easily determine:

- whether an agent already exists for a task;
- whether it works on animal-welfare data;
- whether it has been independently tested;
- what evidence supports its outputs;
- what its failure modes are;
- whether it is safe to use in a particular study;
- how to install or configure it; or
- who maintains it.

At the same time, developers lack a prioritised account of the capabilities animal-welfare researchers actually need. This creates duplicated work, poorly validated tools and prototypes that fail to reach real studies.

A conventional directory would improve discoverability but would not solve the trust problem. The Commons must therefore combine a catalogue with standard documentation, evaluation suites, transparent maturity labels and evidence from real use.

## 4. Theory of change

```text
Map research workflows and existing systems
                    ↓
Identify important missing capabilities
                    ↓
Build or adapt reusable agents
                    ↓
Evaluate them on common benchmarks
                    ↓
Publish code, evidence and limitations
                    ↓
Match agents with researchers and datasets
                    ↓
Validate them in real studies
                    ↓
Return results and failures to the Commons
                    ↓
Improve the agents, standards and capability map
```

If researchers can find well-scoped tools with credible evidence, and builders can see validated unmet needs, useful agents should be developed and adopted faster. If field outcomes and failures are returned to a shared evidence base, the ecosystem should improve rather than accumulate unverified demos.

## 5. Goals

### G1. Create a transparent, curated starting catalogue

Identify and document existing agents, models, tools and workflows relevant to animal-welfare research, including tools developed outside the field. Publish the search and inclusion method so absence from the catalogue is never presented as proof that a capability does not exist.

### G2. Make agent quality legible

Give every listed agent a consistent card covering its task, inputs, outputs, dependencies, evidence, limitations, risks, evidence maturity, maintenance state and security status.

### G3. Build important missing agents

Build the initial portfolio across all three research tracks, giving each agent a bounded runnable capability. Use a transparent prioritisation process to decide which prototypes receive deeper development, evaluation and maintenance investment.

### G4. Establish shared evaluation infrastructure

Create versioned benchmark suites that test task performance, scientific reliability, calibration, robustness, safety, usability and cost.

### G5. Generate real-world evidence

Place promising agents with researchers, evaluate their use in real workflows, and publish both successful and unsuccessful results.

### G6. Support cumulative improvement

Make agent code, interfaces, evaluation results, research artefacts and failure reports reusable wherever licensing, privacy and research ethics permit.

## 6. Non-goals for the first release

Version 0.1 will not:

- autonomously conduct or approve animal experiments;
- replace qualified welfare scientists, statisticians, veterinarians or ethics committees;
- certify that an agent is safe for every research context;
- deliver mature implementations of every capability or support every species, modality and deployment configuration;
- provide a general-purpose agent marketplace;
- host arbitrary agent execution for the public;
- store sensitive farm, researcher or animal-level datasets;
- generate engineering-ready hardware or make procurement decisions without human review;
- claim that a generated invention is novel or patentable; or
- rank scientific questions using one opaque master score.

## 7. Primary users

### Animal-welfare researchers

Need reliable tools for literature review, protocol design, data analysis, measurement and reporting.

### Precision-livestock and welfare-technology researchers

Need help working across welfare science, machine learning, sensors, engineering and field deployment.

### Agent and open-source developers

Need well-defined research problems, example datasets, acceptance tests and domain-expert feedback.

### Research organisations, funders and incubators

Need to understand capability gaps and identify tools or projects worth funding, validating or founding.

### Research-methods and ethics reviewers

Need visibility into evidence provenance, limitations, embedded values and appropriate human controls.

## 8. Product principles

1. **Evidence before promotion.** Attractive demonstrations do not justify a high maturity label.
2. **Bounded agents before autonomous scientists.** Each agent should have a clear task boundary and escalation conditions.
3. **Human responsibility remains explicit.** The interface must state which decisions require qualified review.
4. **Welfare outcomes are distinct from productivity outcomes.** An agent must not imply that production improvement is necessarily welfare improvement.
5. **Measurement is not intervention.** Monitoring an animal does not improve welfare unless it leads to effective action.
6. **Uncertainty must survive the interface.** Agents must be able to abstain and expose conflicting evidence.
7. **Failures are publishable results.** Negative evaluations and failed deployments are valuable Commons contributions.
8. **Prototype broadly, deepen using evidence.** Initial agents must have distinct bounded tasks; continued investment should follow demonstrated usefulness against simpler workflows. Shared components should prevent duplicate infrastructure.
9. **Researcher participation begins at design.** Welfare scientists should help define indicators, gold standards, thresholds and appropriate use—not only review finished tools.
10. **Context matters.** Evidence from one species, production system, country or data-collection setup must not be silently generalised to another.

## 9. Product scope

### 9.1 Public website

The website is the discovery and comparison layer. It should include:

- a searchable agent catalogue;
- filters for research task, species, data modality, evidence maturity, maintenance state and security status;
- an agent detail page generated from a versioned Agent Card;
- benchmark and evaluation results;
- a capability map showing existing and missing agents;
- a public backlog of agents worth building;
- study and deployment reports;
- contribution and evaluation guidance; and
- links to canonical GitHub repositories, releases and maintainers.

The website should initially be static or statically generated. User accounts, hosted execution, billing and complex workflow composition are not required.

The homepage should be task-first rather than organised around the programme itself. It should offer three primary routes:

1. find a tool for a research task;
2. build or contribute a missing capability; and
3. inspect evidence or support validation.

Catalogue taxonomy remains available as secondary navigation.

Catalogue pages must also expose the three research tracks and the cross-cutting mapping, development and evaluation activities described in Section 10. Each agent page must state its implemented v0.1 capability, planned extensions, supported input type and available run method. A prototype badge alone is not a description of capability.

### 9.2 GitHub organisation and repositories

GitHub is the source of truth for code and version history.

The proposed canonical repository is [Aaron-Cahill-Ire/Animal_Welfare_Scientist](https://github.com/Aaron-Cahill-Ire/Animal_Welfare_Scientist). Version 0.1 may use this as a monorepo for the website, catalogue data, shared schemas, evaluation harness and reference agents. Individual agents should move to separate repositories only when independent release cycles, maintainers, permissions or dependency requirements justify the additional overhead.

The programme should maintain:

- one core repository for the website, schemas, catalogue records and contribution checks;
- one evaluation repository for shared fixtures, runners, protected-evaluation interfaces and result schemas;
- reference-agent repositories, or clearly separated packages within a monorepo during early development; and
- links to external repositories when the Commons catalogues rather than maintains an agent.

Every open-source agent version must resolve to a specific repository release or commit. Commercial, private, paper-only and discontinued entries must instead identify the most stable available canonical source, the date it was checked and the limits on version verification. The catalogue must never fabricate repository or release metadata.

External repositories are untrusted by default. Listing does not constitute a security review or an endorsement to execute code. The site must show scientific evidence status and security-review status separately.

### 9.3 Agent standard

Every agent built or verified by the Commons must expose a standard conceptual interface:

```text
Agent manifest
  identity and version
  bounded task definition
  accepted input schema
  output and evidence schema
  required tools and permissions
  configuration parameters
  expected cost and runtime
  human-review gates
  known limitations and prohibited uses
  evaluation suite and results
  maintainer and licence
```

The standard should allow different technical implementations. It should not require every agent to use the same model provider or orchestration framework.

### 9.4 Catalogue record, Agent Card and Evidence Card

Record completeness depends on entry type and maturity:

- **Discovery record:** the minimum record for an identified external tool or concept: name, purpose, task, source, access status, evidence status and date checked.
- **Capability-gap record:** the affected workflow, intended user, current workaround, required inputs and outputs, risk level and a proposed evaluation method.
- **Full Agent Card and Evidence Card:** required for a runnable agent at Documented maturity or above.

A full card must provide:

- name and one-sentence purpose;
- problem or research bottleneck addressed;
- intended and prohibited uses;
- target users;
- supported species, production systems and jurisdictions where relevant;
- input and output examples;
- supported data modalities;
- installation and configuration instructions;
- models, tools, datasets and external services required;
- data-governance and privacy considerations;
- estimated cost, latency and compute requirements;
- evidence provenance and citation behaviour;
- benchmark results with uncertainty;
- real-study validation, if any;
- known failure modes and mitigations;
- human oversight requirements;
- evidence maturity, maintenance state and security status;
- repository, release, licence and maintainer; and
- last evaluation date.

Missing fields must be displayed as unknown or not yet evaluated, never silently omitted or inferred.

### 9.5 Capability map and build backlog

The system must distinguish:

- existing and potentially reusable agents;
- agents requiring animal-welfare adaptation;
- prototypes requiring evaluation;
- important missing capabilities; and
- capabilities that should not be agentised because the risk or need for human judgement is too high.

The initial catalogue must follow a versioned search protocol recording sources searched, queries, dates, languages, inclusion/exclusion rules, duplicate handling and known coverage gaps. Until an empirically justified coverage threshold is met, the product must describe the catalogue as curated rather than comprehensive or authoritative.

Missing capabilities should be ranked using:

- expected welfare value enabled;
- number of researchers or workflows affected;
- frequency and cost of the existing task;
- technical tractability;
- availability and quality of evaluation data;
- risk of harmful or misleading outputs;
- neglectedness;
- reusability across species and projects; and
- likelihood of adoption.

## 10. Agent portfolio

The initial Commons portfolio contains 20 agents: six in Track A, eight in Track B and six in Track C. Every agent gets a bounded runnable v0.1. More ambitious capabilities within each agent are later increments, not implied by the agent name.

Two organising dimensions must remain distinct:

| Research track: what the work achieves | Programme activities applied to every track |
|---|---|
| 1 / Track A: map welfare problems and required capabilities to existing solutions; identify opportunities ready for further diligence or adoption | A: discover and document existing agents; B: build or adapt missing agents; C: benchmark and refine those agents |
| 2 / Track B: accelerate applied R&D from hypothesis through analysis, belief update and prototype development | A: discover and document; B: build or adapt; C: benchmark and refine |
| 3 / Track C: accelerate basic research and research integrity | A: discover and document; B: build or adapt; C: benchmark and refine |

Evidence auditing and other integrity agents are reusable across tracks. Their primary catalogue placement does not restrict where a workflow can use them. Benchmarking is shared infrastructure, not a fourth research track or a claim that one agent can certify another.

### 10.1 Track A — solution and opportunity discovery

This track incorporates the WelfareTech Explorer research graph and AIM-inspired funnel.

#### Complementary Track A workflow profiles

Track A preserves two complementary discovery profiles while the product direction
is still being evaluated. Neither profile supersedes the other.

1. **Broad capability mapping — current approach.** Maps a welfare problem across
   causal, measurement and implementation components, then creates separate
   capability-search targets for each component. This remains the general-purpose
   Track A entry point and the implemented v0.1 workflow.
2. **Deep causal scanning — proposed approach.** Selects one causal component,
   constructs and reviews its pathway-specific necessary-condition tree, and
   searches each approved, changeable and technically distinct condition. This is
   an exploratory workflow profile, not a currently implemented capability.

The profiles can be used together:

```text
Broad welfare problem
        ↓
Broad capability mapping
        ├── measurement component → capability search
        ├── implementation component → capability search
        └── selected causal component
                    ↓
             deep causal scanning
                    ↓
             approved condition targets → technology searches
```

Broad mapping may stop at component-level search targets when that is sufficient.
Deep causal scanning is invoked only when recursively decomposing a causal
component is expected to expose meaningfully different intervention targets. A
run must record which profile produced each search target. The proposed deep
profile does not change the bounded A1 or A2 v0.1 implementation contracts until
it receives a separate implementation decision and evaluation plan.

#### A1. Welfare Problem Mapper

Converts a broad welfare problem into a structured causal and functional map. Its central function is to decompose the problem into components, identify the capability required at each intervention point, and produce separate search targets for the Solution and Prior-Art Scout. This is the agent previously called the Welfare Systems Mapper; it is not an additional portfolio agent.

The core Track A workflow is:

```text
Broad welfare problem
        ↓
Problem Mapper: outcome, context and component map
        ↓
Each causal / measurement / implementation component
        → required capability → separate Scout search target
        ↓
Scout: candidate solutions linked to components and capabilities
        ↓
Gap Analyst: requirement coverage, constraints and remaining gaps
        ↓
Claim Auditor → human review and prioritisation
```

The Mapper distinguishes three component types:

1. **Causal:** possible factors or mechanisms producing the welfare problem; searches target prevention or change to those mechanisms.
2. **Measurement:** barriers to detecting or quantifying the problem; searches target observation, detection or valid measurement.
3. **Implementation:** barriers preventing an effective response; searches target routing, adoption, treatment access, incentives or management feedback.

A component may have multiple linked roles, but each role must be explicit. Detecting a problem must not be represented as resolving it: measurement components must identify the downstream action they could enable and any implementation dependency.

The structured output must include:

- welfare outcome, affected animals, production system and context;
- stable component IDs, component types, plausible causes/mechanisms and relationships between components;
- observable indicators and the limits of what they measure;
- intervention points and stable IDs for the required capabilities at each point;
- functional requirements and solution constraints, including user-supplied thresholds or explicit unknowns;
- existing mitigations and evidence for why they may be insufficient;
- source-linked evidence, uncertainty and alternative explanations for each proposed component and causal link; and
- one bounded Scout search target per required capability, carrying its component ID, context, requirements, constraints, evidence and unresolved questions.

Separate observed facts, supported mechanisms and hypotheses. The Mapper must not turn a plausible cause into an established causal finding, invent local farm conditions or force a complete map when evidence is missing. User review can correct or add components before searches run.

For example, the user-provided brief “Lameness is causing poor welfare in dairy cows” could prompt investigation of flooring as a causal component, delayed gait detection as a measurement component, and alerts failing to lead to examination as an implementation component. These are illustrative hypotheses to check against evidence and context, not established findings about a particular herd. They yield different capability searches: reduce slipping/hoof trauma; detect abnormal gait early; and route affected animals for examination.

The Scout must return a coverage record for every search target, including no-result, inaccessible-source and insufficient-evidence outcomes. Candidates may address multiple capabilities, but each match needs its own supporting evidence. The Gap Analyst compares required capabilities and constraints with those matches, distinguishing unmet requirements from unresolved search coverage and recording dependencies between solutions. It must not collapse the output into one undifferentiated “solution to lameness.”

#### A2. Solution and Prior-Art Scout

Searches academic literature, patents, products, startups, standards and adjacent industries to identify existing solutions or prototypes that could address a welfare bottleneck. It accepts the Mapper's component/capability search targets or an equivalent researcher-supplied target. Candidate records retain component and capability IDs, evidence for the match, constraint fit and coverage limitations.

Its output must distinguish:

- commercially available solution;
- research prototype;
- patent only;
- adjacent solution requiring adaptation;
- failed or abandoned attempt;
- apparently missing solution; and
- insufficient evidence.

#### A3. Missing-Capability Analyst

Compares each required capability and its constraints with the Scout's candidate solutions, then converts remaining gaps into explicit research or development briefs. It should state who needs the capability, what decision it supports, what inputs exist, what output would be useful, why current tools fail and how success could be evaluated. Preserve component/capability IDs and distinguish an unmet requirement from insufficient evidence or an incomplete search.

#### A4. Opportunity Prioritisation Orchestrator

Implements a staged research funnel: broad mapping, rapid independent scoring, shallow dives, critical-uncertainty analysis, adversarial review, QA and decision-ready reports. Human review gates remain mandatory at shortlist and deep-research decisions.

#### A5. Agent and Tool Mapper

Discovers existing research agents and adjacent tools, records their actual capabilities, access conditions, canonical sources and evidence, and identifies candidates to reuse or adapt. It maps the agent ecosystem; the Welfare Problem Mapper maps welfare problems.

#### A6. Evidence and Claim Auditor

Checks whether citations support claims, identifies contradictory evidence, flags inappropriate generalisation and produces a traceable evidence table. It serves all three tracks.

### 10.2 Track B — applied R&D

#### B1. Hypothesis and Crucial-Uncertainty Agent

Turns an intervention or measurement concept into falsifiable hypotheses, a theory of change, decision-critical assumptions and explicit belief forecasts.

#### B2. Welfare Protocol Design Agent

Drafts study protocols using user-specified welfare frameworks and validated indicators. It must expose uncertainty about construct validity, gold standards, sampling, species/context transfer and aggregation across indicators or time.

All protocols require qualified researcher and ethics review.

#### B3. Experiment and Analysis Planner

Proposes experiment designs, measurement plans, power-analysis inputs, stopping rules and analysis options. It must separate confirmatory from exploratory analyses and clearly mark assumptions that require a statistician.

#### B4. Multimodal Welfare Analysis Agent

Processes bounded video, image or audio tasks such as annotation assistance, quality checking or protocol-defined classification. Each task requires dataset-specific evaluation against suitable human-labelled gold standards and reporting of subgroup/context performance.

#### B5. Statistical and Causal Analysis Agent

Produces reproducible analysis proposals and code for approved datasets, checks assumptions, distinguishes association from causation, and reports sensitivity and missing-data issues. High-consequence conclusions require independent statistical review.

#### B6. Hardware Concept Agent

Translates measurement or intervention requirements into non-production concept designs, sensor options, environmental constraints and prototype test plans. Optional visual/CAD or Blender integrations may be added after core evaluation exists.

#### B7. Component and Supply-Chain Agent

Identifies candidate components, suppliers, lead times, indicative costs, regional availability and compatibility risks. Procurement facts must be timestamped and independently confirmed before purchase.

#### B8. Prototype Evaluation Agent

Compares prototype results with predefined success thresholds, updates explicit beliefs, records unexpected outcomes and recommends stop, revise, replicate or advance.

### 10.3 Track C — basic research and research integrity

#### C1. Evidence Synthesis Agent

Conducts protocol-bound searches, screening support, structured extraction, risk-of-bias support and evidence synthesis while preserving complete provenance and human inclusion decisions.

#### C2. Dataset and Measurement Auditor

Assesses annotation quality, inter-rater reliability, representativeness, leakage, missingness, sensor validity and likely limits on generalisation.

#### C3. Preregistration Agent

Converts an approved protocol into a preregistration draft, checks internal consistency and identifies unspecified researcher degrees of freedom. Submission always requires researcher approval.

#### C4. Ethical and Welfare-Risk Review Agent

Surfaces potential harms to animals, people and the environment; embedded value choices; intensification or rebound risks; data-governance issues; and required formal review. It is an aid to—not a substitute for—an ethics committee.

#### C5. Reproducibility and Reporting Agent

Packages methods, configurations, code, data lineage, deviations, limitations and results into a reproducible study record and appropriate reporting checklist.

#### C6. Research Question and Knowledge-Gap Agent

Uses bounded evidence syntheses to identify unresolved basic-research questions, conflicting findings and testable directions. It distinguishes gaps in knowledge from gaps in the material searched and preserves the supporting evidence and uncertainty.

## 11. Initial build decision

Version 0.1 follows a breadth-first strategy: implement all 20 portfolio agents at a deliberately narrow prototype scope, connect them through common contracts, then deepen them according to demand and evidence. Reuse or adapt suitable existing tools where they satisfy the task; a separate model or duplicated runtime is not required for every agent.

### 11.1 Minimum runnable capability for each agent

The scopes below are the first-release contract. A documented limitation is acceptable; an empty scaffold, canned answer or prompt file with no working execution path is not a completed prototype.

| ID | Agent | Minimum v0.1 input → output |
|---|---|---|
| A1 | Welfare Problem Mapper | Broad welfare brief and supplied evidence → typed causal/measurement/implementation components, intervention points, required capabilities and constraints, with evidence/uncertainty and one Scout search target per capability. |
| A2 | Solution and Prior-Art Scout | Bounded bottleneck and approved source collection or search tools → sourced candidates classified as available, prototype, patent-only, adjacent, failed or insufficient evidence. |
| A3 | Missing-Capability Analyst | Problem map and candidate evidence → explicit unmet requirements, current limitations and proposed success criteria; incomplete search cannot establish nonexistence. |
| A4 | Opportunity Prioritisation Orchestrator | Candidate set and user-specified criteria → shallow comparison, crucial uncertainties and proposed shortlist; pause for human approval before deeper investigation. |
| A5 | Agent and Tool Mapper | Research task and approved sources → deduplicated tool records, access/version evidence, reuse options and coverage gaps. |
| A6 | Evidence and Claim Auditor | Claims and accessible source passages → claim-by-claim support, contradiction, scope and evidence-strength findings with review flags. |
| B1 | Hypothesis and Crucial-Uncertainty Agent | Gap or intervention brief → falsifiable hypotheses, assumptions, competing explanations and evidence that would change the conclusion. |
| B2 | Welfare Protocol Design Agent | Selected hypothesis and user-supplied welfare framework → protocol draft specifying population, indicators, procedures, missing decisions and review needs. |
| B3 | Experiment and Analysis Planner | Protocol draft and resource constraints → proposed design, comparator, sampling and power-analysis inputs, analysis plan and stopping assumptions. |
| B4 | Multimodal Welfare Analysis Agent | A supported public or synthetic short video → timestamped descriptive observations using a declared backend, with uncertainty and annotation output. Audio and other tasks remain explicitly unsupported until implemented and tested; observations are not validated welfare diagnoses. |
| B5 | Statistical and Causal Analysis Agent | Synthetic/public tabular data and analysis question → actual descriptive statistics, missingness checks, a reproducible analysis script and a separate causal-assumption assessment. Arbitrary generated-code execution is not required. |
| B6 | Hardware Concept Agent | Measurement/intervention requirements → concept specification, component classes, interfaces and bench-test plan. CAD/Blender generation is a later extension. |
| B7 | Component and Supply-Chain Agent | Component requirements and approved supplier records → sourced candidate parts, compatibility gaps and timestamped availability/cost fields; unknown or stale fields remain explicit. |
| B8 | Prototype Evaluation Agent | Bench-test results and predefined criteria → pass/fail/indeterminate by criterion, deviations and a justified stop/revise/advance recommendation for human review. |
| C1 | Evidence Synthesis Agent | Bounded question and accessible document collection → screening decisions, evidence table and qualified synthesis with exclusions and coverage limits. |
| C2 | Dataset and Measurement Auditor | Public/synthetic dataset and data dictionary → missingness, representation and annotation/measurement checks; unassessable validity questions remain unknown. |
| C3 | Preregistration Agent | Human-reviewed protocol and analysis plan → preregistration draft and unresolved-decision checklist; no submission. |
| C4 | Ethical and Welfare-Risk Review Agent | Study/intervention brief → animal, human and environmental risk questions, mitigation options and required formal review; no approval. |
| C5 | Reproducibility and Reporting Agent | Supplied study artefacts and run records → methods/reporting draft, provenance manifest and missing-artifact checklist. |
| C6 | Research Question and Knowledge-Gap Agent | Evidence synthesis and explicit scope → unresolved basic-research questions, conflicting findings and bounded research priorities, distinguishing evidence gaps from search gaps. |

### 11.2 Common implementation and run contract

Every prototype must have a versioned manifest, validated input/output schemas, executable entry point, task-specific logic or tool integration, example input, actual recorded output, failure/abstention behaviour, starter benchmark and complete cards. Models, prompts, tools and supported input types must be declared. Model-backed runs must execute the configured model; fixture or replay mode must be clearly labelled and cannot alone satisfy the runnable-prototype requirement.

Agents must be invocable independently through a documented local command or callable interface. A shared runner must pass structured, versioned artefacts between agents, retain source and claim identifiers, record configuration/cost/runtime, enforce configured limits and stop at required human decisions. Missing mandatory inputs must produce an actionable request or partial result, not fabricated upstream findings. No agent may silently invoke unsupported capabilities.

The initial build includes actual on-demand example runs. Continuous background operation, public arbitrary execution and autonomous experiment or procurement actions are outside v0.1. Each reference agent must provide a safe example trial without local setup, such as a notebook; pages must disclose credentials, provider charges and supported modes before launch. A static recorded example is useful documentation but is not an executable trial.

### 11.3 Connected example workflows

1. **Discover solutions:** Welfare Problem Mapper → component/capability search targets → Scout searches per target → Missing-Capability Analyst compares coverage and constraints → Claim Auditor → human decision. Shared candidates retain all relevant target IDs. The Orchestrator can organise prioritisation with explicit human gates.
2. **Develop an intervention:** selected gap → Hypothesis Agent → Protocol Design → Experiment Planner → Ethics/Welfare-Risk Review → human approval → Preregistration draft. Actual study execution is external; supplied results can subsequently enter Statistical Analysis → Prototype Evaluation → Reporting.
3. **Develop a hardware concept:** approved requirements → Hardware Concept → Supply-Chain Agent → human review. Supplied bench-test results then enter Prototype Evaluation; the workflow cannot invent test results.
4. **Investigate a research question:** supplied literature → Evidence Synthesis → Research Question/Knowledge-Gap Agent → Claim Auditor → Reporting. When data exist, Dataset Auditor → supported Multimodal or Statistical Analysis → Reporting forms an additional branch.

All four workflows need executable public/synthetic examples. A workflow with a human or external-work gate must pause and resume from an explicitly supplied artefact. Preregistration precedes confirmatory data collection; later reporting must preserve deviations.

### 11.4 Evaluation and catalogue priorities

Every agent gets starter tests and benchmarks during its first implementation. The Scout and Auditor are the first pair to receive deeper, prospectively specified scientific evaluation and a matched researcher-workflow comparison. Findings determine subsequent refinement order, not whether the other prototype packages may be built.

Researcher interviews, baseline documentation and design-partner recruitment can proceed alongside common infrastructure and public/synthetic prototypes. A controlled partner evaluation measures usability, correction burden, time and blinded quality before a usefulness claim is published. It is not a real-study pilot and cannot confer Pilot-observed maturity.

The website must list the 20 Commons prototypes plus at least 13 external/proposed/gap records, including at least five runnable external tools with evidence reviews. External catalogue inclusion does not imply execution or verification.

## 12. Agent development lifecycle

Every Commons-built agent follows the same lifecycle, with two delivery milestones: a runnable Prototype release, then progressively stronger evaluated releases. Stages 0–2 begin with a bounded task hypothesis, safe examples and a starter rubric; researcher consultation can run alongside prototype development. Full independent evaluation and real-study validation are gates for stronger claims and maturity, not prerequisites for building the initial portfolio.

### Stage 0 — workflow observation

- Interview or observe researchers performing the task.
- Document inputs, outputs, decisions, failure costs and present workarounds.
- Confirm that an agent is appropriate for the task.

### Stage 1 — task and safety specification

- Define the bounded task and prohibited uses.
- Specify input/output and evidence schemas.
- Identify human-review gates.
- Define the minimum credible baseline and evaluation plan before implementation.

For a starter prototype, these can be provisional and visibly marked as such. They must be frozen before a confirmatory evaluation, with development examples kept separate from the evaluation set.

### Stage 2 — benchmark construction

Begin each prototype with public development cases covering an ordinary task, missing/ambiguous inputs, misleading evidence or adversarial content, and a task-specific failure. This is development coverage, not a statistically sufficient scientific benchmark. For deeper evaluation, apply the following requirements:

- Source representative cases independently of agent development where practical.
- Use at least two blinded annotators, a locked rubric, reported inter-rater reliability and documented adjudication for judgement-based labels.
- Maintain a separately authored external-validation set.
- Include ordinary, ambiguous, adversarial and abstention cases.
- Reserve a protected or rotating subset to reduce benchmark overfitting.

### Stage 3 — prototype

- Build the smallest agent that can be evaluated.
- Preserve prompts, model versions, tool calls, sources, costs and intermediate outputs.
- Compare it with a simple non-agent baseline.

A prototype may be published after the prototype gate in Section 13.5. Continue through Stages 4–8 as evidence and research partnerships become available; this does not delay other agents' initial prototypes.

### Stage 4 — controlled evaluation

- Run component-specific and end-to-end benchmarks.
- Conduct error analysis rather than reporting only an aggregate score.
- Require critical safety and evidence thresholds even when average performance is strong.

### Stage 5 — expert review and red teaming

- Use blinded review where practical.
- Separate welfare-science, technical, statistical and adoption judgements.
- Record disagreement and route it to targeted investigation.

Commons builders cannot independently award a trust label to their own agent. Independently verified status requires a published approval decision from at least one external welfare-domain reviewer and one external methods reviewer, neither of whom built the evaluated version.

### Stage 6 — public release

- Publish the versioned repository, Agent Card, Evidence Card and evaluation results.
- Assign a maturity label based on evidence, not developer judgement.

### Stage 7 — real-study validation

- Agree the agent’s role, comparison condition and success measures with a research partner.
- Preregister the primary outcomes and analysis. Use a matched within-researcher crossover or randomised comparison where feasible, with blinded output-quality assessment.
- Record time saved, correction burden, failures, user trust and effects on research decisions.
- Report effect estimates and uncertainty rather than relying on before/after anecdotes.
- Do not expose sensitive data or unpublished results without permission.

### Stage 8 — maintenance or retirement

- Re-evaluate material changes to models, prompts, dependencies or datasets.
- Mark stale, unsupported or unsafe agents visibly.
- Preserve negative findings and retirement reasons.

## 13. Evaluation system

Version 0.1 includes starter evaluation suites for all 20 agents and handoff tests for the four example workflows. Deeper scientific evaluation begins with the Scout and Auditor individually and as a connected discovery workflow. More elaborate longitudinal evaluation is added when the relevant data and version history exist.

### 13.1 Evaluation dimensions

#### Task correctness

Does the agent perform its bounded task accurately and completely?

#### Evidence quality

Do cited sources textually entail claims and match their population, context and comparator? Is the evidential strength adequate? Are counterevidence, uncertainty, scope limitations and material omissions represented?

#### Scientific validity

Does the output use valid constructs, measurements and methods without making causal or cross-context claims that the evidence cannot support?

#### Calibration and abstention

Do confidence estimates correspond to observed correctness? Does the agent abstain when evidence is insufficient?

#### Robustness

Does performance survive irrelevant rewording, terminology changes, noisy inputs and plausible contextual variation?

#### Welfare and ethical safety

Does the agent avoid conflating productivity with welfare, surface potential harms and preserve required human oversight?

#### Usefulness

Does it reduce researcher time or improve work quality after correction and review costs are included?

#### Efficiency

What are the latency, model/search cost, compute requirements and human-review burden per useful output?

### 13.2 Starter benchmarks and deeper evaluation

Every prototype must ship a versioned starter suite with safe cases, expected behaviours, a task-specific rubric, a defined simple baseline, actual run results and a failure log. Cover schema validation, task usefulness, provenance, abstention, unsupported inputs, tool restrictions and preservation of warnings through handoffs. Automated checks and developer review can support this milestone; label the results preliminary and disclose who graded them. Passing starter tests does not establish scientific effectiveness or automatically promote a configuration beyond Prototype.

Task rubrics must test the implemented capability: candidate recovery for discovery; source support for synthesis/auditing; unresolved assumptions for protocol drafts; actual numeric correctness for statistics; timestamped annotation agreement for the supported video task; requirements and component compatibility for hardware; and criteria application for prototype evaluation. A fluent response or valid JSON alone cannot pass task correctness.

The deeper evaluation programme, first applied to the Scout, Auditor and their combined workflow, must include:

1. **Systematically constructed discovery corpus:** build a stratified corpus from documented searches of patents, literature, registries, products and failed projects; hold out prominent, obscure, negative and discontinued cases. Known-capability recovery is reported as recovery on this corpus, not as recall over an unknowable universe.
2. **Adversarial and abstention cases:** include terminology traps, unsupported claims, productivity-only benefits, measurement-without-action cases and questions whose correct response is insufficient evidence.
3. **Multidimensional citation review:** score entailment, scope match, evidential strength, contradiction and material omission separately using blinded reviewers and reported disagreement.
4. **Matched baseline:** compare each agent and the combined workflow with the current researcher workflow or a simple, fixed non-agent procedure at the same task boundary.
5. **Structured error analysis:** report error types, critical failures, abstentions, correction burden, costs and relevant subgroup/context results rather than only an aggregate score.
6. **Guardrail tests:** treat prompt injection, unsafe tool use, provenance loss, productivity/welfare conflation and unsupported cross-context transfer as release-blocking failures.

There is no universal minimum case count. Each suite must preregister its primary endpoints, baseline, superiority or non-inferiority margin, critical-harm ceilings and decision rule. Sample sizes must follow the required precision or be large enough to detect each release-blocking failure mode with at least 95% probability at its maximum tolerated prevalence. If available cases cannot support that claim, the result must be labelled preliminary rather than Independently verified.

### 13.3 Later evaluation families

The following are required when their prerequisites exist, but are not launch blockers for version 0.1:

1. **Historical time capsules:** reconstruct the contemporaneous candidate universe from sources available at the cutoff, predefine success independently of present prominence, include sampled failures and blind corpus builders to later outcomes where practical.
2. **Calibration ladder:** use precisely defined binary events, resolution dates and authorities; report Brier or log scores, calibration curves and comparisons with base-rate/constant-confidence baselines once there are enough observations.
3. **Rejected-case audit:** send a stratified sample of rejected outputs to the next stage to estimate false-negative rates.
4. **Champion–challenger evaluation:** compare mature versions, prompts and architectures on frozen tasks, including ablations and matched-budget simple baselines.
5. **Handoff replay:** replace an incorrect upstream output with a gold output to locate where errors enter and propagate through a multi-agent workflow.
6. **Human-factors evaluation:** measure comprehension, appropriate reliance, correction burden and whether uncertainty changes user decisions appropriately.
7. **Context-transfer tests:** evaluate performance across species, farms, recording setups, regions and researcher groups before transfer is claimed.

### 13.4 Evaluation result requirements

Every published result must include:

- agent, model, prompt/configuration and dependency versions;
- benchmark and dataset version;
- evaluation date;
- sample size and uncertainty;
- scoring method and reviewer information;
- disaggregated performance where relevant;
- baseline comparison;
- failures and abstentions;
- estimated cost and runtime; and
- a reproducible result artefact or an explanation of access restrictions.

### 13.5 Release gates

**Prototype release:** the implemented capability in Section 11.1 runs on a real example through its declared backend; its schemas, documentation, cards, source/configuration records and starter benchmark results are present; its tests demonstrate failure/abstention behaviour and required human gates. Known critical failures involving disclosure, unauthorised tool actions or fabricated provenance block executable release until addressed. Scientific limitations and other unresolved quality failures remain visible. Security-review status is recorded separately.

**Evaluated release:** publish a frozen task-specific evaluation, baseline comparison, grading method, uncertainty and error analysis. Failed evaluations remain publishable, with failed decision rules clearly displayed; Evaluated does not mean approved or effective. Starter development checks alone do not satisfy this gate.

An agent cannot be labelled **Independently verified** or above unless:

- its task and prohibited uses are explicit;
- its critical outputs are traceable to inputs and evidence;
- it has passed a versioned benchmark suite;
- critical failure modes have been tested;
- its frozen evaluation satisfies its preregistered decision rule and critical-harm ceilings;
- at least one external welfare-domain reviewer and one external methods reviewer have examined failures and approved the label;
- its evidence card is complete and current.

## 14. Maturity model

Scientific-evidence maturity, maintenance state and security status are separate fields.

| Evidence maturity | Meaning |
|---|---|
| Identified | Relevant tool or concept has been found but not assessed. |
| Documented | Agent Card and repository/version information are complete. |
| Prototype | A runnable implementation exists with example cases. |
| Evaluated | Versioned benchmark results and failure analysis are available. |
| Independently verified | Release gates have been met and independent reviewers approved the result. |
| Pilot-observed | The agent has been prospectively assessed in one real research workflow; the validated task, population and context must accompany the label. |
| Research-replicated | Prospectively evaluated use has been replicated by at least two independent research groups in predefined contexts. |

Maintenance state is **Active**, **Unmaintained**, **Stale** or **Retired**. Security status is **Unreviewed**, **Reviewed** or **Revoked**. Reviewed status identifies an immutable release or commit, dependency set, permission manifest, reviewer, scope and review date. Any code, dependency, build, permission, ownership or release-channel change resets the affected artefact to Unreviewed. An agent may be scientifically promising while unmaintained or security-unreviewed; the interface must not collapse these dimensions into one badge.

Evidence maturity applies to an immutable evaluated configuration snapshot, not permanently to an agent name.

Identity follows this hierarchy:

```text
Agent
└── AgentVersion (code, manifest or output-schema release/commit)
    └── ConfigurationSnapshot (model, prompt, tools, parameters and environment)
        └── EvaluationRun / EvidenceCard / evidence-maturity status
```

A code, manifest or output-schema change creates a new AgentVersion. A model, prompt, tool, parameter or environment change creates a new ConfigurationSnapshot. Any material change invalidates inherited evaluation status until the changed snapshot is re-evaluated.

## 15. Functional requirements

### Catalogue and discovery

- **R1:** Visitors can browse and search agents without creating an account.
- **R2:** Visitors can filter by task, species, modality, evidence maturity, maintenance state, security status and maintainer.
- **R3:** Catalogue entries clearly distinguish external listings from Commons-maintained agents and scientific evidence status from maintenance and security status.
- **R4:** Missing capabilities appear alongside existing agents but are visually distinct.
- **R5:** Every open-source agent page links to a canonical, versioned GitHub source; other entry types identify the most stable canonical source available and disclose verification limits.

### Evidence and comparison

- **R6:** Every entry renders the record appropriate to its type and maturity; runnable agents at Documented maturity or above render the full Agent Card and Evidence Card.
- **R7:** Benchmark results identify the exact evaluated configuration and dataset.
- **R8:** Each reference-agent page compares its evaluated configuration with the defined baseline using aligned tasks and benchmark versions, with visible uncertainty, cost, limitations and missing results. Generic agent-to-agent comparison is deferred until two evaluated catalogue agents perform the same bounded task.
- **R9:** Negative, null and failed results remain visible.
- **R10:** Stale results and unsupported agents carry prominent warnings.

### Contribution

- **R11:** Version 0.1 accepts proposed agents and capabilities through one manually reviewed GitHub issue or pull-request template.
- **R12 (Phase 5):** After external submission demand is observed, automated checks validate required metadata, links and result schemas and a non-GitHub submission route feeds the same review queue.
- **R13:** Maintainers can review contributions using documented inclusion and evidence criteria; a contributor cannot approve evidence maturity for their own agent.
- **R14 (Phase 4):** Disputes about evaluation or safety can be recorded without silently overwriting earlier results.

### Reference agents

- **R15:** Each Commons-built reference agent implements the common manifest and input/output contract.
- **R16:** Each reference agent emits evidence provenance, uncertainty and review-required flags.
- **R17:** Agent runs are reproducible enough to identify the exact configuration and inputs used.
- **R18:** High-consequence outputs cannot be presented as approved scientific or ethical decisions.

### Evaluation

- **R19:** Each reference agent has task-specific tests and the version 0.1 evidence, safety and adversarial evaluation minimum defined in Section 13.2.
- **R20:** Evaluation results can be published to the website from machine-readable result files.
- **R21:** Protected benchmark items are not exposed through the public site.
- **R22:** Evaluation supports baselines, version comparisons and structured error analysis.

### Real-study validation (Phase 4)

- **R23:** A study record identifies the agent’s role, researchers, context, success measures and review process.
- **R24:** Study records can report time saved, corrections, failures, decision effects and researcher feedback.
- **R25:** Public records exclude restricted datasets and unpublished study content unless explicitly authorised.

### Accessibility and content integrity

- **R26:** The public site conforms to WCAG 2.2 AA, supports keyboard-only and screen-reader use, does not encode evidence or safety status by colour alone, and keeps catalogue and comparison content usable at mobile widths.
- **R27:** Every displayed agent output states whether it is illustrative or from a real run and retains its configuration identity, provenance, uncertainty/abstention state, applicable context and required human review.
- **R28:** Empty searches, incomplete evidence, unavailable repositories, stale evaluations and multiple versions explain what is unknown and provide a next action; no-result states never imply that no capability exists.

### Security and data governance

- **R29:** External executable agents remain explicitly untrusted until a version-specific review under a published repository trust policy covers maintainer identity, release integrity, dependencies, permissions, isolated evaluation and rapid revocation.
- **R30:** Retrieved material is treated as untrusted data, never as authority. Agents receive minimum necessary permissions; sensitive inputs cannot be sent to destinations selected by retrieved content; state-changing or external-sharing actions require explicit human approval.
- **R31:** Protected evaluation items are accessible only to authorised evaluation custodians, never to the evaluated agent’s developers; access is auditable, outputs must not reveal cases, and suspected leakage invalidates results and triggers rotation. Model and tool providers are explicit data processors and may receive cases only under terms that prohibit training, secondary use and retention beyond the evaluation window.
- **R32:** Every Commons-managed development run, evaluation and pilot follows a product-level handling policy covering classification, minimisation, approval before external processing, authorised access, trace-level redaction, retention/deletion, incident response and publication review. Reproducibility records must not contain raw sensitive inputs, credentials or restricted source content.

### Portfolio implementation and component-level discovery

- **R33:** All 20 agents in Section 11.1 implement their bounded v0.1 capability and pass the Prototype release gate; scaffolds and replay-only demonstrations do not count as completed agents.
- **R34:** Every agent can run independently through the shared contract; the four workflows in Section 11.3 execute examples, preserve provenance and pause/resume at human or external-work gates.
- **R35:** Catalogue navigation supports the three research tracks and cross-cutting discovery, development and benchmarking activities, and distinguishes implemented capabilities from planned extensions.
- **R36:** The Problem Mapper emits the typed component map and capability search targets specified in A1, preserving evidence, uncertainty, context, constraints and stable IDs.
- **R37:** The Scout and Gap Analyst retain component/capability identity, report coverage for every target and distinguish unmet requirements, candidate matches and unresolved evidence/search gaps.

## 16. Information architecture

```text
Home
├── Explore agents
│   ├── Discovery
│   ├── Applied R&D
│   ├── Basic research
│   └── Research integrity
├── Agent page
│   ├── Purpose and appropriate use
│   ├── Repository and installation
│   ├── Inputs and outputs
│   ├── Evidence and limitations
│   ├── Benchmarks
│   └── Real-study validation
├── Capability map
│   ├── Existing
│   ├── Needs adaptation
│   └── Missing
├── Benchmarks
│   ├── Suites
│   ├── Results
│   └── Evaluation methodology
├── Studies and failure reports (Phase 4)
└── Contribute
    └── Open the curated GitHub submission template
```

## 17. Data model

Core entities:

```text
ResearchTask
WelfareProblemMap
ProblemComponent
RequiredCapability
CapabilitySearchTarget
CandidateSolution
CapabilityCoverageAssessment
Agent
AgentVersion
ConfigurationSnapshot
Maintainer
Repository
CapabilityGap
Dataset
BenchmarkSuite
BenchmarkCase
EvaluationRun
EvaluationResult
EvidenceCard
FailureReport
ResearchStudy (Phase 4)
ResearchPartner (Phase 4)
```

Important relationships:

- an Agent addresses one or more ResearchTasks;
- a WelfareProblemMap contains typed ProblemComponents and evidence-qualified relationships;
- each ProblemComponent links to RequiredCapabilities and their intervention points and constraints;
- each CapabilitySearchTarget identifies a required capability, component and map version;
- CandidateSolutions link to one or more capabilities through sourced CapabilityCoverageAssessments; absence of a match is not proof that no solution exists;
- an Agent has one or more AgentVersions, each with one or more immutable ConfigurationSnapshots;
- an EvaluationRun tests one ConfigurationSnapshot against one BenchmarkSuite version;
- an EvidenceCard summarises the evidence for one ConfigurationSnapshot;
- a CapabilityGap may be addressed by multiple agents or remain open;
- a ResearchStudy validates a specified agent configuration in a defined context; and
- a FailureReport may attach to an evaluation, study or agent version.

## 18. Safety, ethics and research-integrity requirements

The product must treat the following as first-class design constraints:

- validity and reliability of welfare indicators;
- quality and diversity of gold-standard annotations;
- accumulation of uncertainty when multiple indicators are combined;
- limited generalisability across farms, species and recording conditions;
- embedded values in welfare definitions and aggregation choices;
- automation bias and inappropriate researcher reliance;
- productivity/welfare conflation;
- rebound effects and reduced human observation;
- privacy, ownership and commercial sensitivity of farm data;
- animal, worker and environmental effects under a One Welfare framing;
- dual-use or intensification risks; and
- reproducibility across changing foundation models and external tools.

Every agent must state when formal ethical approval, statistical review, veterinary judgement or other qualified oversight is still required.

For pilot studies, public metadata must use minimum-necessary disclosure and pseudonymisation by default. Naming researchers, farms, organisations or datasets requires explicit publication consent and a re-identification review for small or distinctive contexts. Partners must have a documented correction or withdrawal route for personal or commercially sensitive metadata.

For tool-using agents, retrieved webpages, repositories, papers and datasets are untrusted content. They cannot change the task, authorise data disclosure or grant permissions. Prompt-injection and tool-confusion cases are part of the release-blocking evaluation suite.

## 19. Success measures

### Programme hypotheses and stop criteria

The prototype release tests whether the portfolio can perform its bounded tasks and exchange useful, traceable outputs. The subsequent evaluation programme tests two causal hypotheses:

1. A curated catalogue with visible evidence and limitations helps researchers or builders make better tool-selection or capability-investment decisions than their current search process.
2. The connected discovery workflow reduces total researcher time or improves output quality after setup, correction and review costs are counted.

Before confirmatory evaluation, document the current comparison workflow and predeclare the primary measures, time horizon and minimum worthwhile improvement. Public/synthetic prototype development can proceed while this work is completed. If partner tests show no meaningful improvement, or review burden and critical failures erase the benefit, pause further expansion beyond the initial portfolio and revisit the affected task, architecture or product premise. Do not claim usefulness based solely on completing the portfolio.

### Version 0.1 launch targets

- 20 Commons agents with bounded runnable prototypes, plus at least 13 external/proposed/gap records;
- at least five runnable external tools documented with evidence reviews;
- all four example workflows runnable with explicit pause/resume gates;
- one versioned starter benchmark suite and actual results for each reference agent;
- a documented simple baseline and preliminary comparison for each agent;
- complete Evidence Cards for all reference agents;
- every agent has a documented executable example trial without local setup, with credentials and cost requirements disclosed.

These are prototype-release targets. The next evidence milestone requires deeper Scout/Auditor benchmark sample sizes justified by preregistered precision and failure-detection requirements, review input from at least five animal-welfare researchers, and at least one representative research team completing the bounded discovery task and comparison condition with setup, correction and review time included. Pending partners or independent reviewers do not prevent an honestly labelled Prototype release.

### Six-month outcome targets

- at least two agents used in real research workflows;
- at least one public validation or failure report;
- measurable reduction in researcher time for a bounded task without a material decline in quality;
- at least two external contributions to agents, datasets or evaluations;
- re-evaluation completed after any material model or agent change; and
- at least one prospectively tracked decision in which the catalogue records the alternative considered, predicted benefit, later outcome and whether the evidence improved the decision against predeclared criteria.

### Metrics to monitor

- qualified monthly users and returning researchers;
- agent-page-to-repository click-through;
- successful installations or completed example runs;
- benchmark coverage and recency;
- correction burden per agent output;
- false-positive, false-negative and abstention rates;
- citation-support rate;
- expert agreement and disagreement;
- cost and researcher time per useful output;
- real-study adoption and retention; and
- number and severity of reported failures.

Traffic alone is not a sufficient success measure.

## 20. Delivery phases

The following phases are dependency-based milestones. Calendar estimates should be set after repository inspection, backend selection and a first working agent; the earlier two-agent schedule does not apply to the 20-agent scope. Shared infrastructure and researcher engagement can proceed concurrently.

### Phase 0 — portfolio and common contracts

- Confirm product name and governance owner.
- Interview 5–8 researchers about high-frequency and high-friction workflows.
- Define the Agent Card, Evidence Card, manifest and evaluation-result schemas.
- Define the catalogue search protocol, repository trust policy, protected-evaluation custody and pilot data-handling policy.
- Create the GitHub organisation/repository structure.
- Record the bounded inputs, outputs, unsupported uses and starter rubric for all 20 agents using Section 11.1.
- Establish shared execution, configuration, provenance, cost limits and human-gate conventions.
- Start priority-workflow baseline documentation, partner recruitment and evaluation-owner assignment alongside prototype development.

### Phase 1 — common runner and first connected example

- Build the common runner, manifest/schema checks, source records and starter evaluation harness.
- Implement the Scout and Auditor first to exercise the shared contracts end to end.
- Verify standalone calls, structured handoffs, budget stops and incomplete-evidence handling.
- Freeze only the interfaces necessary for the next prototype wave; do not wait for independent scientific validation before proceeding.

### Phase 2 — portfolio prototypes and catalogue MVP

- Build the static website and link one curated GitHub submission template.
- Build the remaining Track A agents, then Track B and Track C prototypes using the same common contracts. Reuse existing tools where suitable.
- Populate all 20 Commons records and at least 13 external/proposed/gap records; show unfinished agents as planned until they actually pass the prototype gate.
- Add search, filters, separate evidence/maintenance/security labels, baseline results on agent pages, accessibility and repository/source links.
- Publish the capability map and prioritised refinement backlog.
- Produce a starter suite, baseline comparison, failure log and runnable example for every agent.
- Connect and test all four workflows, including their human and external-result gates.

### Phase 3 — prototype release and priority evaluation

- Release portfolio agents as each passes the prototype gate; the portfolio milestone is complete when all 20 pass.
- Publish versioned agents, documentation, executable example trials and preliminary evaluation results.
- Add warnings, maturity labels and negative findings.
- Invite external replication and benchmark contributions.
- Deepen the Scout/Auditor suites, run matched baselines, expert review and structured error analysis.
- Complete the bounded design-partner evaluation before publishing claims of workflow improvement.

### Phase 4 — research pilots

- Select one or two bounded research workflows with willing partners.
- Add the pilot-partner intake flow, study-record schema, dispute history and publication-consent workflow.
- Agree comparison conditions, data governance and success measures.
- Run pilots with human oversight.
- Publish permitted findings and revise or retire agents based on evidence.

### Phase 5 — refinement and portfolio expansion

- Re-rank capability gaps using pilot evidence.
- Deepen existing multimodal, statistical, hardware and supply-chain prototypes using suitable data, expert ownership and evaluations. Add new modalities, CAD integrations, broader task support or new agents when evidence warrants the work.
- Establish a champion–challenger process for material agent changes.

## 21. Acceptance scenarios

### Version 0.1

#### AS1. Researcher discovers an appropriate agent

Given a researcher needs help checking citations in a welfare review, when they filter for evidence-auditing agents, then they can identify an Active version, see its benchmark performance and limitations, and reach a working example without an account.

The trial must be usable without local setup on a safe example dataset and must not imply that the agent is suitable for the researcher’s private data.

#### AS2. Researcher avoids an unsafe use

Given an agent has only been evaluated on cattle images from one controlled dataset, when a researcher considers using it for pigs under farm conditions, then the page clearly states that this transfer is unvalidated and requires dataset-specific evaluation.

#### AS3. Builder finds a valuable missing capability

Given a developer wants to contribute, when they open a capability-gap page, then they can see the affected workflow, users, current workaround, success criteria, risks, example inputs and proposed benchmark—not merely an agent name.

#### AS4. Agent version changes

Given an agent changes its model or prompt materially, when a new ConfigurationSnapshot is created, then its previous evidence maturity and results do not automatically transfer; the site shows snapshot-specific evaluation status.

#### AS5. Agent performs well on average but fails a guardrail

Given an agent scores highly overall but repeatedly treats productivity improvements as welfare benefits, when results are reviewed, then it cannot receive Independently verified status until that critical failure is addressed.

#### AS6. Researcher interprets a baseline comparison

Given a reference agent has been evaluated against the current workflow or a simple baseline, when a researcher reads its benchmark results, then the page shows aligned task and benchmark versions, configuration, uncertainty, costs, limitations and missing results. It does not imply comparison with unrelated agents.

#### AS7. Search finds no matching agent

Given a researcher’s filters return no results, when the empty state appears, then it says that catalogue coverage is incomplete, offers to broaden the filters, links to relevant capability gaps and provides a route to report a missing tool.

#### AS8. Example output preserves its warnings

Given an agent page displays a polished example, when a researcher reads it, then the example states whether it is illustrative or a real run and keeps its version/configuration, provenance, context, uncertainty or abstention state and required human review attached.

#### AS10. Every track has runnable prototypes

Given the v0.1 portfolio release, when a developer invokes any of the 20 agents with its documented supported example, then its declared backend performs the bounded task and returns schema-valid output with configuration, sources where applicable and limitations. A canned response or empty package fails this scenario.

#### AS11. Workflow pauses for actual research work

Given a hardware workflow has produced a concept, when no bench-test results exist, then it pauses and requests them. On resumption with supplied results, the evaluation agent applies the predefined criteria without claiming that the system built or physically tested the prototype.

#### AS12. Prototype and evaluated versions remain distinguishable

Given a new agent passes its starter suite, when its page is published, then it remains Prototype with preliminary results. A different agent with a frozen scientific evaluation displays its own evidence and decision-rule outcome; neither inherits the other's status.

#### AS13. Unsupported modalities are explicit

Given the initial multimodal prototype supports a bounded video task, when a user submits audio, then it returns an unsupported-input response and the documented next action. It does not invent an analysis or imply that the planned audio capability exists.

#### AS14. A broad welfare problem produces distinct capability searches

Given a dairy-cow lameness brief and example evidence containing causal, measurement and implementation issues, when the Mapper runs, then it produces separately typed components and capability targets, each with context, constraints, stable IDs, evidence and uncertainty. Unsupported causal explanations are labelled hypotheses. The Scout searches each target and returns candidate or coverage-status records; the Gap Analyst reports remaining requirements per capability. A single generic search for “lameness solutions” fails this scenario.

#### AS15. Detection does not imply intervention success

Given a candidate supports abnormal-gait detection but no evidence establishes an effective treatment-routing process, when the Gap Analyst assesses coverage, then it can mark the detection requirement as addressed within the supported context while retaining the implementation gap. It cannot infer that pain or lameness has been reduced.

### Phase 4 — real-study validation

#### AS9. Real study produces a negative outcome

Given a pilot saves no researcher time after correction costs, when the study concludes, then the failure report remains visible and informs the capability map and future agent design.

## 22. Key dependencies

- Access to animal-welfare researchers for task definition, gold cases and review.
- Legally and ethically usable example datasets.
- Maintainers willing to support reference agents.
- Stable provenance for model, prompt and tool configurations.
- Clear open-source licensing and third-party repository attribution.
- A process for protecting sensitive benchmark cases and study data.
- Sufficient evaluation budget for expert review rather than relying exclusively on automated judges.

## 23. Risks and mitigations

| Risk | Mitigation |
|---|---|
| The site becomes a low-quality link directory | Require structured cards, version identity and visible evidence status. |
| Researchers over-trust agent outputs | Use bounded-task language, prominent limitations, abstention and mandatory review gates. |
| Benchmarks reward superficial optimisation | Maintain protected cases, rotate challenges and validate in real workflows. |
| Evaluation depends on one subjective score | Use disaggregated dimensions, pairwise expert review and explicit disagreements. |
| Breadth produces shallow or duplicated agents | Use one common runner, require a distinct runnable task and starter benchmark per agent, and concentrate deeper investment according to researcher evidence. |
| The programme builds infrastructure before proving demand | Keep prototype tasks bounded, recruit researchers alongside development, and use the Scout/Auditor comparison to guide refinement and expansion beyond the initial portfolio. |
| Agent results become stale as models change | Attach results to exact versions and define re-evaluation triggers. |
| Gold standards encode unreliable or narrow judgement | Report annotator agreement, context and uncertainty; include diverse reviewers and datasets. |
| Private research data leaks through tools or logs | Default to public/synthetic data and require documented data controls for pilots. |
| Tool development advances intensification rather than welfare | Require an explicit welfare causal pathway and One Welfare/dual-use review. |
| External repositories disappear or change | Record releases/commits, licence and maintenance state; archive metadata where permitted. |
| Scope expands into a general scientific-agent platform | Prioritise capabilities using animal-welfare value and researcher demand. |

## 24. Open product decisions

These decisions should be resolved during Phase 0 but do not block this PRD:

1. Final public product name; the initial GitHub repository is `Aaron-Cahill-Ire/Animal_Welfare_Scientist`.
2. Which welfare frameworks and reporting standards are supported first.
3. Which research partners and datasets can support the first pilot.
4. Which organisation will act as the independent evaluation custodian and maturity-label authority.
5. Default open-source licences for code, catalogue metadata and benchmark data.

## 25. Relationship to existing work

### WelfareTech Explorer

`INITIAL_PRD.md` supplies the structured opportunity graph, specialist discovery agents, prior-art search, staged prioritisation funnel, provenance model and early evaluation concepts. Within this PRD it becomes Track A rather than the entire product. This revision supersedes both the earlier WelfareTech v0.1 scope and the Commons two-agent launch strategy. Bounded mapping, discovery, gap analysis and prioritisation prototypes are now included alongside the other tracks. A comprehensive ontology, technology library, dedicated analogy engine and full research-table application remain later extensions.

### Learning Evaluation System

`docs/ideation/2026-09-11-learning-evaluation-system-ideation.html` supplies the operational evaluation direction: outcome forecasts, rejected-idea audits, adversarial challenge cases, reviewer calibration, historical time capsules, champion–challenger comparisons and error-cascade analysis.

### Ambitious Impact research process

The AIM process informs broad scoping, idea generation, quick independent prioritisation, shallow dives, critical-uncertainty research, expert input, quality assurance and staged human decision gates. The Commons adapts this funnel to select both welfare interventions and research-agent capabilities.

### AI for One Welfare

The cited Frontiers perspective shapes the requirements for welfare-scientist involvement, valid indicators and gold standards, hardware/software uncertainty, multi-indicator integration, human decision-making, contextual validation, embedded values and attention to animal, human and environmental effects.

## 26. Source links

- [Ambitious Impact Research — Prioritization](https://sites.google.com/charityentrepreneurship.com/ambitious-impact-research/our-research-process/prioritization)
- [AI for One Welfare: the role of animal welfare scientists in developing valid and ethical AI-based welfare assessment tools](https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2025.1645901/full)

## 27. Definition of the first successful release

The v0.1 prototype release is complete when all 20 agents perform their specified bounded capabilities, each has documented inputs/outputs and actual starter benchmark results, all four example workflows run with their required gates, and the catalogue exposes the three research tracks with accurate capability and maturity labels. Researchers can access the code and execute safe examples without local setup, subject to disclosed provider credentials and costs.

The next evidence milestone is a prospectively measured improvement in the Scout/Auditor workflow after correction and review costs are included, followed by evidence-led refinement of the wider portfolio. Completing the prototype release establishes runnable coverage; scientific usefulness and real-study validation remain separately measured outcomes.
