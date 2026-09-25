# Continue refining the Welfare Technology Scanner PRD

I am designing a tool that takes one documented farm-animal welfare problem,
builds an evidence-backed tree of causal pathways and necessary conditions, and
then searches patents, research, products, and trade sources for existing
technologies that could remove one of those conditions.

Please begin by reading these files in order:

1. `prototypes/welfare-scanner/PROCESS_MAP.md` — the clearest current end-to-end
   process and worked example.
2. `prototypes/welfare-scanner/PROCESS_SPEC.md` — the more detailed design rules
   and agent responsibilities.
3. `prototypes/welfare-scanner/README.md` — provenance and authority notes.
4. `prototypes/welfare-scanner/welfare-problem-mechanism-database.xlsx` — the
   33-problem MVP input register.

The imported dashboard and imported historical chat prompt are earlier
snapshots. Use them only as context. Where they conflict with `PROCESS_MAP.md`
or `PROCESS_SPEC.md`, the two newer documents take precedence. In particular,
do not assume that ammonia is a necessary cause of broiler footpad dermatitis.

## Decisions already made

- The output we are refining is a very clear PRD/process artifact, not
  implementation code yet.
- One run handles one user-selected welfare problem and explores it deeply.
- The 33-row workbook is the controlled MVP problem inventory. Underlying
  scientific sources remain authoritative for causal claims.
- The system has 10 LLM roles, one deterministic Workflow Orchestrator, and two
  human review points.
- The MVP focuses on necessary conditions. Contributory risk factors are
  deferred rather than incorrectly labelled necessary.
- “Necessary” is scoped to a parent process or one causal pathway; it does not
  automatically mean globally necessary for every case of the ailment.
- Ailments, causal pathways, necessary conditions, and technology-search
  targets are different node types and must remain visually distinct.
- The Welfare Evidence Agent owns literature retrieval. The Fault-Tree Builder
  owns tree structure and branch-depth decisions. They exchange structured
  requests and evidence cards through the orchestrator.
- Accepted conditions get a simple Strong or Plausible evidence marker.
  Anything below Plausible remains unresolved.
- For the MVP, the Tree Builder uses LLM judgement to decide whether deeper
  decomposition would expose a different intervention target. It records a
  rationale and confidence marker. There is no extra probe search.
- The entire tree is built and approved before the full technology searches
  begin.
- Technology scouts search approved, changeable, technically distinct
  necessary-condition nodes. They do not indiscriminately search every box.
- Intermediate and terminal necessary-condition nodes may both be eligible.
- Every candidate remains attached to the exact condition and pathway it acts
  on.
- “Apparently untested” is a dated search result, never proof of novelty.
- Broiler footpad dermatitis is the worked example. Wet-litter contact has the
  strongest support. Ammonia-related chemical irritation is retained as an
  unresolved hypothesis, not an approved necessary pathway.

## What I want from this chat

Help me turn the current material into one exceptionally clear and internally
consistent PRD. Start by checking whether the mental model and terminology are
coherent. Then refine three diagrams:

1. the abstract agent and orchestration flow;
2. the structured artifact/data flow between roles; and
3. the broiler-footpad worked example, starting at the ailment, separating
   alternative causal pathways from necessary conditions, and showing exactly
   which nodes become technology-search targets.

Be especially alert to the distinction between:

- an ailment;
- an alternative causal pathway;
- a necessary condition within that pathway;
- an unresolved hypothesis; and
- an approved technology-search target.

Challenge any causal claim that is scientifically weak or logically circular.
Do not make the diagrams tidy by pretending a contributory factor is necessary.
Explain changes in plain language and keep the MVP simple. Ask me one focused
question at a time only when the answer would materially change the design.
