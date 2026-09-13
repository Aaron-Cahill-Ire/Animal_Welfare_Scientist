# Animal Welfare Science Agent Commons

A development portfolio of 20 bounded research tools with common execution,
source/configuration records, four gated workflows, a static catalogue and
actual preliminary benchmarks. All tools use deterministic Python calculations
or rules on supplied evidence. No model call, live search, independent scientific
validation or welfare benefit is implied.

## Run without dependencies

Python 3.9 or later, from this repository:

```sh
python3 -m commons list
python3 -m commons run A1
python3 -m commons run B5 --input examples/B5.input.json
python3 -m commons run A6 --output audit.json
python3 -m commons evaluate
python3 -m unittest discover -s tests -v
python3 -m commons build-site
python3 -m http.server 8080 --directory dist
```

`run ID` executes the documented synthetic example when `--input` is omitted.
Each entry has an input schema in `catalogue/manifests`, a complete Agent Card,
an Evidence Card, and recorded actual input/output under `examples`.
`pip install -e .` optionally installs the `commons` command.
The site’s example buttons execute the same bundled Python in a browser worker
using Pyodide 0.27.7. No credentials or provider charges; the first run downloads
the runtime from jsDelivr. No input is sent to a model service. Browser and native
Python configurations have different snapshot identities.

## What the prototypes support

- A1–A6: typed problem components, searches over an approved annotated source
  collection, per-capability coverage/gaps, criteria-based shortlisting, tool
  deduplication and conservative quotation/annotation auditing.
- B1–B8: structured hypotheses and protocol drafts, limited sample-size planning,
  actual synthetic frame pixel analysis, descriptive statistics and a fixed
  reproducible script, requirement-based hardware concepts, dated supplier
  comparison and predefined bench-criterion evaluation.
- C1–C6: screening support, data/measurement checks (including categorical kappa),
  preregistration consistency, contextual risk questions, artifact provenance
  checks and evidence-versus-search-gap distinctions.

Video input is specifically a timestamped synthetic grayscale frame sequence,
2–120 frames, at most 64×64 pixels and 60 seconds. MP4, audio, animal behaviour
classification and welfare diagnosis are unsupported. Search agents do not
browse the web. Auditor source assertions are caller annotations, not automatic
entailment. Prototype labels apply only to these stated capabilities.

## Workflows and explicit decisions

```sh
python3 -m commons workflow discovery --output checkpoint.json
python3 -m commons workflow discovery --resume checkpoint.json --artifact decision.json
python3 -m commons workflow hardware --output checkpoint.json
python3 -m commons workflow intervention --output checkpoint.json
python3 -m commons workflow research --output checkpoint.json
```

A decision artifact identifies the exact saved checkpoint:

```json
{"checkpoint_id":"COPY_FROM_CHECKPOINT","reviewer":"Named reviewer","approved":true}
```

A negative decision stops the workflow. Checkpoint digests detect accidental
changes; they are not signatures or an authentication system. Updated agent
configurations require restarting and reviewing the workflow.

Hardware freezes input criteria before review and waits for external `results`
and `sources`. Intervention requires a human-reviewed `protocol` and
`analysis_plan`, then an external `registration_reference` before the
study-results stage. Supplied study results include `rows`, `columns`, `results`,
`sources` and any `deviations`. A final review follows evaluation. These are
attestations supplied by humans, not evidence that this software conducted
experiments, obtained ethics permission or registered a study.

`examples/workflows` contains synthetic gate-by-gate transcripts and artifacts.
They demonstrate execution and are explicitly labelled simulated decisions.

## Limits, safety and reproducibility

Public/synthetic data only. No tools, shell commands, generated code, purchases,
external submissions or network access are invoked by the research runner.
Source text is data. Source IDs, configuration hashes, input hashes, warnings,
runtime and zero provider cost accompany every run. Input/source budgets are
validated before execution. Native POSIX main-thread calls are interrupted at the configured runtime limit;
browser workers are forcibly stopped at 60 seconds. Other embedding contexts
can only discard late results, so they must provide their own process timeout.
Inputs must remain bounded.
Outputs remain subject to qualified human review.

The source hash includes implementation, schemas and runner; the configuration
also identifies Python. Changes invalidate the previous snapshot’s evidence.
`python -m commons evaluate` regenerates version-specific results and failure
logs. These are purposive developer-authored cases, not independent validation
or statistical estimates of real-world accuracy. Baseline ties remain visible.

## Contribute and validate

Use the single GitHub contribution template for agents, gaps, evaluations and
failure reports. A maintainer manually checks source/version identity, licence,
input/output contracts, examples, risks, baseline and grading evidence. Listing
an external repository never authorises executing its code. Independent maturity
labels need external welfare and methods reviewers; contributors cannot award
those labels to themselves.

See `docs/implementation/governance.md` for search protocol, repository trust,
data handling and protected-evaluation custody. Research interviews, independent
reviewers, design-partner comparisons and field pilots remain pending.
