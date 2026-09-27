# v0.1 implementation and release assessment

Specification examined: Animal Welfare Science Agent Commons PRD, revised 2026-09-13. The original user documents remain untouched. This implementation supplies a bounded development portfolio, not a scientifically validated autonomous research service.

## Implemented software

- Twenty independently callable Python handlers with distinct tasks, schemas, examples, actual outputs, baseline functions, failure/abstention paths and cards (R15–R19, R33).
- Content-addressed implementation/configuration identity including Python and budgets; source/input provenance and zero-provider-cost accounting (R16–R17). Schema validation uses the documented subset in commons/schema.py.
- Four connected workflows retaining all upstream run records and warnings, explicit checkpoint-bound human decisions and external-results gates (R18, R34). Preregistration is drafted before the external study stage; nothing is submitted automatically.
- Typed problem components and stable capability IDs; per-target candidate coverage and bounded gap reports; measurement does not resolve action requirements (R36–R37).
- Static 33-record catalogue with search, all three tracks, task search, modality/species/maturity/maintenance/security/maintainer filters, shareable agent-detail links, baseline counts, real-run examples, negative-result visibility and one contribution template (R1–R11, R20, R27–R28, R35).
- Five external tools with primary-source documentation reviews and inspected immutable commits; eight proposed gap records with requirements, workarounds, risks and starter evaluation ideas. External execution and welfare validation are not claimed.
- Actual on-demand browser examples via a pinned Python WebAssembly runtime. Examples execute the bundled source locally on the visitor’s device. No hosted arbitrary execution or provider credentials.
- Search protocol, trust policy, handling policy, protected-evaluation design and contributor review process (R13, R21, R29–R32) documented. No protected or sensitive cases are supported by this public development harness.

## Deliberately narrow capabilities

These constraints are visible in the catalogue and are not silently described as full scientific capabilities:

- Scout searches a caller-annotated approved collection. Live multi-source retrieval is a proposed extension.
- Auditor checks exact quotations and supplied evidence annotations; automatic semantic entailment is not implemented.
- Mapper uses typed supplied components or bounded clause rules; it cannot infer an entire causal model from a vague brief.
- Video analysis operates on short synthetic grayscale frame sequences. Compressed video decoding, farm animal annotation, audio and welfare diagnosis are unsupported.
- Statistical analysis produces real descriptive summaries, missingness and a reproducible fixed script. It does not estimate an identified causal effect.
- Protocol/hardware/ethics tools produce reviewable drafts and checks, not approvals or production designs.
- Approval artifacts are human attestations, not authenticated signatures or evidence of regulatory permission.

These implementations demonstrate the common contracts and safe bounded tasks. Broader natural-language reasoning, real-farm modalities and independent task validity require further work before stronger product claims.

## External milestones still pending

- Governance/evaluation-owner appointment and interviews with 5–8 researchers.
- Prospectively specified deeper Scout/Auditor evaluation, broader discovery corpus, independently annotated gold cases and sample-size justification.
- Independent welfare/methods review and frozen scientific evaluations. All published Commons evidence remains preliminary.
- Matched design-partner workflow comparison counting setup, corrections and human review.
- Real-study pilots, consent/publication review, observed outcomes and independent replication.
- Full accessibility conformance audit and real-browser/device matrix. Semantic controls, labels, visible focus, non-colour statuses and responsive breakpoints are implemented; WCAG 2.2 AA certification is not claimed.
- WebMCP is feature-detected; interface support depends on the browser. A supported native WebMCP validation context was not available, so registration is not claimed verified.

## Verification approach

Tests check task-specific semantics and exact numeric results, unsupported inputs, no input mutation, warning/provenance retention, rejection of ambiguous results, checkpoint integrity and pause/resume sequencing. Native Python and the pinned WebAssembly Python runtime run the same starter rubric; failures and baseline ties are public evidence, not hidden release scores. UI data/assets and worker input restrictions receive automated contract checks. No claim is made that purposive developer cases estimate real-world accuracy or usefulness.

## Operational validation

Owner: repository owner until a maintainer is assigned. On publication, confirm the catalogue JSON/source archive load, a safe example runs, filters work, and evidence identifies the deployed code. No telemetry is installed. If source/configuration mismatch, broken example execution, fabricated provenance or exposed restricted information is observed, withdraw the executable trial or redeploy the last verified version; preserve the failure record. Scientific limitations alone do not become stronger maturity labels. Re-run all starter cases after material implementation changes.
