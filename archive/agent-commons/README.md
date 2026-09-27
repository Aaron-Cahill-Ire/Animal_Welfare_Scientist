# Animal Welfare Science Agent Commons — Archived Supporting Implementation

> **Repository role:** Preserved experiment and possible source of future
> building blocks. It is not the selected Animal Welfare Scientist LLM pipeline.

Animal Welfare Science Agent Commons is a collection of 20 small deterministic
research utilities. Each handles a narrow task, such as mapping a research
question, checking a dataset, drafting a protocol or auditing whether a supplied
quotation matches supplied evidence.

The utilities use Python rules and calculations on supplied data. They do not
call an AI model, search the live web, conduct experiments or diagnose animal
welfare. Their outputs are starting points for qualified human review, not
scientific findings.

[Explore the previously published catalogue](https://animal-welfare-agent-commons.aaronmcahill.chatgpt.site/)

## What is preserved here

- `commons` — the Python implementation;
- `catalogue` — manifests, Agent Cards and Evidence Cards;
- `examples` — synthetic inputs, recorded outputs and four sample workflows;
- `schemas` — the structured data contracts;
- `tests` and `benchmarks` — developer-authored checks;
- `web` — the static catalogue source;
- `docs` — implementation notes, governance and the earlier Agent Commons PRD;
- `.github` and `.openai` — the earlier automation and hosting configuration.

## Run the archived implementation

From this directory, using Python 3.9 or later:

```sh
python3 -m commons list
python3 -m commons run A1
python3 -m commons run B5 --input examples/B5.input.json
python3 -m commons evaluate
python3 -m unittest discover -s tests -v
```

The tools are grouped into three tracks:

- **A1-A6: Discover and assess tools.** Break down a research problem, search an
  approved annotated source collection, identify capability gaps, shortlist
  tools and audit source annotations.
- **B1-B8: Design and run studies.** Draft hypotheses and protocols, plan a
  limited sample size, analyse bounded synthetic inputs, calculate summaries,
  compare hardware concepts and assess supplied bench-test results.
- **C1-C6: Check evidence and research quality.** Support screening, inspect
  datasets and measurements, draft preregistrations, surface contextual risks,
  check artefact provenance and classify evidence gaps.

## Limits

- Search is limited to an approved source collection supplied by the caller.
- Citation checks do not prove that a source supports a claim in context.
- Demonstrations use bounded synthetic inputs rather than real animal studies.
- Human-supplied approvals do not prove that an experiment happened or received
  ethical permission.
- The benchmarks are developer-authored and do not estimate real-world
  scientific accuracy.

See `docs/implementation` for the preserved contracts, governance and
verification notes.
