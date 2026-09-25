# Welfare problem scanner: continue the fault-tree pipeline design

I'm continuing work on a project from earlier chats. I've attached two files: the dashboard (welfare-scanner-dashboard.html) and the problem database (welfare-problem-mechanism-database.xlsx). Please read both before replying.

## What the project is

A plan for an LLM agent pipeline that takes a farm animal welfare problem and finds technologies from other industries that could fix it. The database lists 33 welfare problems across chickens, pigs, dairy cows, salmon, shrimp and other fish, taken from EFSA welfare opinions and fish and shrimp welfare reports. Nothing is built as agents yet. One scan was run by hand, and its results are used as examples.

## The method so far

1. **Break each problem into a fault tree.** The harm sits at the top. Underneath are the conditions that had to be true for it to happen. Each group of conditions has a gate:
   - ALL: every condition is needed, so breaking any one stops the harm.
   - ANY: these are alternative routes, so every route must be blocked.
   Some conditions are strictly necessary. Others only raise the risk. Mark which is which.
2. **Stopping rule, applied branch by branch.** Keep splitting a branch until the next level would search the same technical field as the level above. Also drop branches that can't be changed, and branches whose removal causes a different harm.
3. **Remove the animal.** Rewrite each node as a physical process with no species named, in a few phrasings, because patents, medical papers and trade press word things differently.
4. **Search every node whose field differs from its parent's**, not just the leaves, across patents, medical research and trade press.
5. **Filter**: does the technology act on the process in the node? Has it already been tried on this animal? Then rank by position in the tree, cost, readiness and new harms.

## The pipeline (10 steps, as on the dashboard)

Picker agent → Evidence agent → Tree builder agent → Vet check (person) → Translator agent → Search agents (one per source, in parallel) → Match judge agent → Validator agent → Triage agent → Expert review (person).

## Worked example: sore feet (footpad dermatitis) in broiler chickens

Top level, ALL gate: ammonia, wet litter, hours sitting, heavy body.
Wet litter, ANY gate: wet droppings, leaking drinkers, condensation.
Ammonia, split one level further:
- Nitrogen going in (feed protein) → animal nutrition. The only genuinely new field.
- Bacteria and the urease enzyme → urease inhibitors from fertiliser chemistry. This was the top finding of the hand scan: used in poultry houses for emissions, but nobody scored the birds' feet.
- Water → overlaps with wet litter, so drying litter hits two branches.
- Acidity → litter acidifiers. I believe these are already used on farms, so the validator should flag it as already transferred. Please verify.
- Warmth and time → warmth can't really change; litter reuse can.
The first three look like ALL conditions. Acidity and warmth look like risk-raisers. The top-level gate is also uncertain: if wet litter alone can cause sores, ammonia belongs under ANY and blocking it is only a partial fix.

## What I want to do in this chat

Help me develop the tree-building step properly. Specifically:
1. Pressure-test the sore feet tree, including the gates, with sources.
2. Build a full tree for one or two more problems from the database, applying the stopping rule branch by branch, and list which nodes would get a search.
3. Work out what each agent's input and output should look like, as concrete handoff formats.
4. Suggest how to test it, starting with the solved rows (in-ovo sexing, ablation-free shrimp maturation, shrimp electrical stunning), which the pipeline should rediscover.
5. Update the dashboard when the design changes.

## Things to watch for

- Don't call something untried or novel without checking. In earlier chats this was the weakest part, and I had to push back several times.
- Say when a gate or a mechanism is a guess. A wrong gate sends every later search the wrong way.
- The hand scan found that most promising technologies were already known but not in use, held back by cost, distribution or regulation. Keep that in view: the pipeline may mostly find deployment gaps rather than discoveries.
- Explain things plainly, with concrete examples. I find dense spreadsheets and abstract descriptions hard to follow.
