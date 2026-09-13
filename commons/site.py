"""Static catalogue generated only from explicit public assets and actual run records."""
import html
import json
import shutil
import zipfile
from pathlib import Path
from .evaluation import write_results
from .registry import specs
from .runner import run_agent

ROOT = Path(__file__).resolve().parent.parent


def _write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')


def gap_records():
    gaps = [
        ('G1','A','Live multi-source discovery','Approved-collection search cannot discover new sources.','Librarian-led literature, patent and product searches.','Capability targets, approved query scope, budget.','Timestamped search log, source records, candidates and coverage.','Recover held-out known cases without inventing citations.','Prompt injection, retrieval bias, inaccessible sources.','Stratified known-case recovery and inaccessible-source cases.'),
        ('G2','A','Semantic citation support','The deterministic auditor checks quotations and caller annotations.','Expert claim-by-claim reading.','Claims, complete passages, context and comparator.','Entailment, contradiction, scope and strength judgements.','Match blinded experts on frozen contextual citation cases.','Fluent unsupported entailment and cross-species transfer.','Independent dual-annotated citation benchmark.'),
        ('G3','B','Real-farm video annotation','The current video tool measures pixel changes in synthetic frame sequences.','Human time-coded annotation.','Permitted farm video and a validated ethogram.','Timestamped descriptive labels with subgroup error rates.','Match qualified annotation on held-out farms and cameras.','Privacy, occlusion, background motion and invalid welfare inference.','Blinded timestamp agreement by farm and lighting condition.'),
        ('G4','B','Cluster-aware study planning','The initial power approximation excludes clustered designs.','Statistician-led design and simulation.','Cluster counts, intraclass correlation and cost constraints.','Auditable power/sensitivity simulations.','Reproduce independently specified reference simulations.','Underpowered or mis-specified animal studies.','Reference designs with unequal clusters and missing data.'),
        ('G5','B','Verified component compatibility','Supplier records need engineering and current availability checks.','Datasheet comparison and supplier confirmation.','Electrical, mechanical and environmental requirements.','Versioned compatible options and explicit conflicts.','Recover known incompatibilities without recommending unsafe parts.','Stale stock, interface mismatch and unsafe actuation.','Dated datasheet pairs with planted compatibility failures.'),
        ('G6','C','Validated measurement transfer','Observed data summaries cannot validate a welfare indicator.','Domain review and prospective validation.','Indicators, gold standards and source/target populations.','Transfer limits, validation needs and study plan.','Identify invalid transfer on independently reviewed cases.','Confusing productivity, activity or proxies with welfare.','Cross-context cases with expert construct-validity judgements.'),
        ('G7','C','Protected independent evaluation','Development benchmarks are authored alongside implementations.','Independent custodian-run assessments.','Frozen configuration, rubric and restricted benchmark access.','Auditable scores, uncertainty and failures without case disclosure.','Prevent developer access while enabling reproducible adjudication.','Leakage, overfitting and false independence claims.','Access audits and deliberately leaked challenge cases.'),
        ('G8','C','Research workflow field evaluation','Runnable code has not shown a researcher benefit.','Observed comparison with researchers’ existing process.','Consented task, matched comparator and prespecified measures.','Setup, review, correction time and blinded quality results.','Meet a prospectively declared useful improvement with no critical harms.','Automation bias, selection bias and hidden correction burden.','Consented prospective crossover or randomised comparison.')]
    return [{'id': i,'name': name,'track': track,'type':'gap','task': task,'maturity':'Identified','maintenance':'Unknown','security':'Unreviewed','modality':['structured-json'],'species':['Context-specific'],'maintainer':'Unassigned','intended_user':'Animal-welfare researchers and collaborating developers','current_workaround':workaround,'inputs':inputs,'outputs':outputs,'success_criteria':success,'risks':risk,'proposed_benchmark':bench,'priority_basis':'Provisional order: first close discovery/audit gaps, then broaden modalities and independent evaluation. Not a measured welfare-value ranking.'} for i,track,name,task,workaround,inputs,outputs,success,risk,bench in gaps]


def build():
    out=ROOT/'dist'
    out.mkdir(exist_ok=True)
    result=write_results(ROOT/'benchmarks/results')
    rows=[]
    publication_path=ROOT/'catalogue/publication.json'
    publication=json.loads(publication_path.read_text()) if publication_path.exists() else {}
    source_commit=publication.get('agent_source_commit')
    for aid,spec in specs().items():
        sample=run_agent(aid,spec['example'])
        evidence=result['summaries'][aid]
        config=sample['configuration_snapshot']
        _write(ROOT/'examples'/f'{aid}.input.json',spec['example'])
        _write(ROOT/'examples'/f'{aid}.output.json',sample)
        manifest={k:v for k,v in spec.items() if k!='example'}
        manifest.update(id=aid,configuration_snapshot=config,run_method=f'python -m commons run {aid}',permissions=[],human_review_required=True)
        _write(ROOT/'catalogue/manifests'/f'{aid}.json',manifest)
        card={'name':spec['name'],'purpose':spec['task'],'intended_users':['Welfare researchers','Methods reviewers','Developers'],
              'intended_uses':[spec['task']],'prohibited_uses':['Autonomous animal study approval or execution','Veterinary diagnosis','Autonomous procurement','Claims of independent scientific validation'],
              'species':'Synthetic examples only; no general species validation','production_systems':'Context supplied by researcher; unvalidated','jurisdictions':'Not assessed',
              'data_governance':'Public/synthetic only. Local computation, no external model processing; see handling policy.',
              'dependencies':['Python >=3.9 (stdlib); browser trial uses pinned Pyodide 0.27.7'], 'models':[], 'tools':[],
              'cost_usd':0,'runtime_seconds_example':sample['runtime_seconds'],'human_review_required':True,
              'limitations':spec['limitations'],'failure_and_abstention':'Invalid/missing input requests correction. Unsupported evidence/context is partial or abstained.',
              'repository':'https://github.com/Aaron-Cahill-Ire/Animal_Welfare_Scientist','release':'0.1.0 development; configuration content hash in manifest',
              'maintainer':'Repository owner; scientific maintainer assignment pending','license':'MIT (implementation)','real_study_validation':'Not performed','input_example':spec['example'],'output_example':sample,
              'evidence_maturity':evidence['maturity'],'maintenance':'Active','security':'Unreviewed','last_evaluation':result['evaluated_at']}
        _write(ROOT/'catalogue/cards'/f'{aid}.json',card)
        _write(ROOT/'catalogue/evidence'/f'{aid}.json',evidence)
        rows.append({'id':aid,'name':spec['name'],'task':spec['task'],'track':aid[0],'type':'commons','maturity':evidence['maturity'],'maintenance':'Active','security':'Unreviewed',
                     'modality':spec['modalities'],'species':['Synthetic examples'],'maintainer':'Commons','required':spec['required'],'limitations':spec['limitations'],
                     'example_input':spec['example'],'input_schema':spec['input_schema'],'output_schema':spec['output_schema'],'configuration':config,'output':sample,'evidence':evidence,'agent_card':card,
                     'evaluated_at':result['evaluated_at'],'planned_extensions':'Broader evidence interpretation, externally reviewed cases, additional contexts and modalities; not implemented by this version.',
                     'source':f'https://github.com/Aaron-Cahill-Ire/Animal_Welfare_Scientist/blob/{source_commit}/commons/agents/track_{aid[0].lower()}.py' if source_commit else None})
    external=json.loads((ROOT/'catalogue/external.json').read_text())
    for item in external:
        item['modality']=item['modalities'];item['species']=['Context-specific'];item['maintainer']=item['repository'].split('/')[-2]
    rows+=external+gap_records()
    _write(out/'catalogue.json',rows)
    _write(out/'benchmarks.json',result)
    runtime={str(p.relative_to(ROOT)):p.read_text() for p in (ROOT/'commons').rglob('*.py')}
    _write(out/'runtime.json',runtime)
    for path in (ROOT/'web').iterdir():
        if path.is_file():shutil.copy2(path,out/path.name)
    guide='\n\n'.join(p.read_text() for p in [ROOT/'README.md',ROOT/'docs/implementation/governance.md'] if p.exists())
    (out/'guide.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Run guide and governance · Commons</title><link rel="stylesheet" href="styles.css"><main class="guide"><a href="index.html">← Research tools</a><h1>Run guide &amp; governance</h1><pre>'+html.escape(guide)+'</pre></main></html>')
    with zipfile.ZipFile(out/'source.zip','w',zipfile.ZIP_DEFLATED) as archive:
        for path in [ROOT/'pyproject.toml',ROOT/'README.md',ROOT/'LICENSE']+list((ROOT/'commons').rglob('*.py'))+list((ROOT/'examples').glob('*.json')):
            if path.exists():archive.write(path,str(path.relative_to(ROOT)))
    return {'output':str(out),'records':len(rows),'agents':20,'benchmark_cases':len(result['cases']),'passing':sum(r['passed'] for r in result['cases'])}
