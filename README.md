# Animal Welfare Scientist — LLM Pipeline Design Workspace

> **Current status:** This repository is being used to compare possible LLM
> research pipelines. No final pipeline or agent architecture has been selected.

The main goal is to decide **which end-to-end LLM pipeline should be built for
discovering and evaluating possible animal-welfare interventions**. Custom agents
should be designed only after that pipeline and its handoffs are clear.

## Start here: candidate pipelines

The core design work is collected in [`docs/approaches`](docs/approaches/README.md).
There are currently three candidate approaches:

| Candidate | Central idea | Best current entry point |
|---|---|---|
| **Welfare Technology Scanner** | Decompose a welfare harm into supported causal pathways and searchable technical requirements, then search across patents, research and products. | [Approach overview](docs/approaches/welfare-technology-scanner.md) and [process map](prototypes/welfare-scanner/PROCESS_MAP.md) |
| **Animal Welfare Research Loop — Baseline v1** | Move from welfare problem to mechanism, measurable process, intervention, experiment and updated hypothesis. | [Read the baseline](docs/approaches/animal-welfare-research-loop-baseline-v1.md) |
| **Jev Welfare-Case Analogy Pipeline** | Represent problem cases on shared welfare dimensions, retrieve similar known cases and transfer their linked solutions as unverified hypotheses. | [Read the analogy pipeline](docs/approaches/jev-welfare-case-analogy-pipeline.md) |

These are exploratory proposals. They may turn out to be alternatives,
complementary stages, or unsuitable. The repository does not yet claim that one
is the preferred architecture.

## The decision this repository should support

The immediate work is to compare the candidate pipelines and answer:

1. What exact research problem does each pipeline solve?
2. What information enters and leaves each stage?
3. Which stages genuinely need an LLM, ordinary code, search, or human review?
4. How does the pipeline preserve evidence, uncertainty and provenance?
5. Can it search biological, engineering, material, sensing and operational
   interventions without producing unmanageable noise?
6. How would useful output be distinguished from a plausible but unsafe or
   unsupported suggestion?
7. What small test would show whether the pipeline is worth building?

After a pipeline is selected, the intended sequence is:

```text
compare candidate pipelines
        -> select or deliberately combine a pipeline
        -> define stage and handoff contracts
        -> design the required custom agents
        -> build a small end-to-end version
        -> evaluate it on known welfare problems
```

## What is supporting material

Everything outside the approach documents is currently secondary to the
pipeline decision. It has been preserved because it may supply useful building
blocks, examples or historical context.

- `prototypes/welfare-scanner` contains the Welfare Scanner's detailed design
  artefacts, workbook and interface snapshots. It is not evidence that the
  pipeline has been implemented or selected.
- `commons`, `catalogue`, `examples`, `schemas`, `tests` and `benchmarks` contain
  20 small deterministic research-tool prototypes and their supporting data.
  They are possible building blocks, not the chosen LLM architecture.
- `web` and `dist` contain the catalogue website and generated browser assets.
- `docs/plans` records earlier product planning.
- `docs/implementation` documents the current deterministic prototype suite.
- `INITIAL_PRD.md` preserves the broader original WelfareTech proposal.

No material has to be discarded to make the project clear. A supporting
artefact should be promoted into the main pipeline only when the pipeline design
shows why it is needed.

## Supporting implementation: Agent Commons

Animal Welfare Science Agent Commons is an existing collection of small
research tools for people working on animal-welfare questions. It was designed
to make early research work easier to inspect, repeat and review.

[Explore the public catalogue](https://animal-welfare-agent-commons.aaronmcahill.chatgpt.site/)

The collection currently contains 20 prototypes. Each handles a narrow task,
such as mapping a research question, checking a dataset, drafting a protocol or
auditing whether a quotation matches supplied evidence. Four sample workflows
show how several tools can be combined while keeping important decisions with a
human reviewer.

These prototypes use deterministic Python rules and calculations on supplied
data. They do not call an AI model, search the live web, conduct experiments or
diagnose animal welfare. Their outputs are starting points for qualified human
review, not scientific findings or a finished LLM pipeline.

## Who this is for

- Researchers can inspect each tool's inputs, outputs, assumptions and limits.
- Animal-welfare organisations can explore where bounded software may help
  their research process.
- Developers can reproduce the examples, compare results and contribute better
  implementations or evaluations.

You do not need to install anything to browse the catalogue or run its examples
in a browser. The first browser run downloads Pyodide 0.27.7 from jsDelivr. The
example data stays in the browser and is not sent to a model service.

## Try it locally

You need Python 3.9 or later. Clone the repository, open it in a terminal and run:

```sh
python3 -m commons list
python3 -m commons run A1
python3 -m commons run B5 --input examples/B5.input.json
python3 -m commons evaluate
python3 -m unittest discover -s tests -v
```

`python3 -m commons list` shows the available tools. `python3 -m commons run A1`
runs one with its included synthetic example. Pass `--input` to use a JSON file
of your own that matches the tool's schema.

Every tool includes:

- an input schema in `catalogue/manifests`;
- an Agent Card explaining its intended use and limits;
- an Evidence Card recording what has been tested;
- an example input and actual recorded output in `examples`.

To build and preview the catalogue locally:

```sh
python3 -m commons build-site
python3 -m http.server 8080 --directory dist
```

Installing the package with `pip install -e .` also provides the `commons`
command.

## What the 20 prototypes cover

The tools are grouped into three tracks:

- **A1-A6: Discover and assess tools.** Break down a research problem, search an
  approved annotated source collection, find capability gaps, shortlist tools,
  remove duplicates and audit quotations or source annotations.
- **B1-B8: Design and run studies.** Draft hypotheses and protocols, plan a
  limited sample size, analyse synthetic image frames, calculate descriptive
  statistics, produce a fixed reproducible script, compare hardware concepts
  and assess supplied bench-test results.
- **C1-C6: Check evidence and research quality.** Support screening, check data
  and measurements, compare work with a preregistration, surface contextual
  risks, verify artifact provenance and distinguish evidence gaps from search
  gaps.

The catalogue also records five established external projects and eight proposed
capability gaps. Those entries document possible options; this project has not
executed or security-reviewed the external tools.

## Run a guided workflow

The four workflows connect tools into longer examples for discovery, hardware
assessment, intervention studies and general research:

```sh
python3 -m commons workflow discovery --output checkpoint.json
python3 -m commons workflow hardware --output checkpoint.json
python3 -m commons workflow intervention --output checkpoint.json
python3 -m commons workflow research --output checkpoint.json
```

Each workflow pauses at decisions that need a person. To continue, create a
decision artifact that refers to the exact checkpoint:

```json
{"checkpoint_id":"COPY_FROM_CHECKPOINT","reviewer":"Named reviewer","approved":true}
```

Then resume the workflow, for example:

```sh
python3 -m commons workflow discovery --resume checkpoint.json --artifact decision.json
```

A rejection stops the workflow. The checkpoint digest detects accidental
changes, but it is not a signature or an authentication system. The transcripts
in `examples/workflows` use synthetic inputs and simulated human decisions.

## Current limits

- The search tools inspect only the approved source collection supplied by the
  caller. They do not browse the web.
- Citation auditing checks exact quotations and caller-provided annotations. It
  does not prove that a source supports a claim in context.
- Image analysis accepts 2-120 timestamped synthetic grayscale frames, each at
  most 64x64 pixels, covering no more than 60 seconds. MP4, audio, animal
  behaviour classification and welfare diagnosis are unsupported.
- Workflow approvals are human-supplied attestations. They do not prove that an
  experiment happened, received ethics permission or was preregistered.
- The included benchmarks are developer-authored checks. They are not
  independent validation or estimates of real-world accuracy.

The runner accepts public or synthetic data only. It does not invoke shell
commands, generated code, purchases, external submissions or network access.
Every run records its source, configuration and input hashes, warnings, runtime
and provider cost. The native runner enforces its deadline on POSIX main-thread
calls; the browser stops its worker after 60 seconds. Other embedding contexts
must provide their own process timeout.

## Licence and contribution

Implementation code uses the MIT licence. Original synthetic benchmark cases
and catalogue metadata use CC0-1.0. Third-party projects retain their own
licences; this repository publishes only metadata and links for those projects.

Use the project's GitHub contribution form to propose a tool, report a gap,
submit evaluation evidence or document a failure. A maintainer checks the
source and version, licence, input/output contract, example, risks, baseline and
grading evidence before accepting a contribution.

Independent maturity labels require external animal-welfare and research-methods
reviewers. Contributors cannot assign those labels to their own work. The
detailed policy is in `docs/implementation/governance.md`. Research interviews,
independent reviews, comparisons with design partners and field pilots remain
future work.
