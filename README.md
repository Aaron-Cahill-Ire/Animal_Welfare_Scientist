# Animal Welfare Science Agent Commons

Animal Welfare Science Agent Commons is an open collection of small research
tools for people working on animal-welfare questions. It is designed to make
early research work easier to inspect, repeat and review.

[Explore the public catalogue](https://animal-welfare-agent-commons.aaronmcahill.chatgpt.site/)

The project currently contains 20 prototypes. Each one handles a narrow task,
such as mapping a research question, checking a dataset, drafting a protocol or
auditing whether a quotation matches the evidence supplied with it. Four sample
workflows show how several tools can be combined while keeping important
decisions with a human reviewer.

This is an early development portfolio. The tools use deterministic Python
rules and calculations on data you provide. They do not call an AI model,
search the live web, conduct experiments or diagnose animal welfare. Their
outputs are starting points for qualified human review, not scientific findings.

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
