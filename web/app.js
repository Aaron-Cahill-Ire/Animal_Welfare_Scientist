'use strict';
let catalogue=[],track='';
const $=id=>document.getElementById(id);
const filters=['search','maturity','modality','type','species','maintenance','security','maintainer'];
const escapeHTML=s=>String(s??'Unknown').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const json=x=>escapeHTML(JSON.stringify(x,null,2));
const safeURL=url=>{try{const u=new URL(url,location.href);return ['http:','https:'].includes(u.protocol)?escapeHTML(u.href):'#';}catch{return '#';}};
function render(){
 const query=$('search').value.trim().toLowerCase();
 const selected=filters.filter(f=>f!=='search').map(f=>[f,$(f).value]);
 const rows=catalogue.filter(r=>(!track||r.track===track)&&(!query||JSON.stringify([r.name,r.task,r.limitations,r.id]).toLowerCase().includes(query))&&selected.every(([f,value])=>!value||(Array.isArray(r[f])?r[f].includes(value):r[f]===value)));
 $('count').textContent=`${rows.length} of ${catalogue.length} records`;
 $('results').innerHTML=rows.length?rows.map(r=>`<article class="card" data-track="${escapeHTML(r.track)}" data-type="${escapeHTML(r.type)}"><div class="card-top"><span>${escapeHTML(r.id)} / ${r.type==='commons'?'COMMONS':r.type==='external'?'EXTERNAL TOOL':'PROPOSED GAP'}</span><span class="badge">${escapeHTML(r.maturity)}</span></div><h3>${escapeHTML(r.name)}</h3><p>${escapeHTML(r.task)}</p>${r.evidence?`<span class="score">Starter checks ${r.evidence.passed}/${r.evidence.n} · baseline ${r.evidence.baseline_passed}/${r.evidence.n}</span>`:''}<div class="meta">${escapeHTML(r.maintenance)} · Security: ${escapeHTML(r.security)}</div><button data-id="${escapeHTML(r.id)}">${r.type==='gap'?'Inspect the proposed gap':'Capability & evidence'} <span aria-hidden="true">↗</span></button></article>`).join(''):`<div class="empty"><h3>No matching records in this catalogue.</h3><p>Coverage is incomplete. This does not establish that a capability is missing.</p><button id="reset">Broaden filters</button> <a href="#gaps">Inspect capability gaps</a> · <a href="#contribute">Report a missing tool</a></div>`;
 $('results').querySelectorAll('[data-id]').forEach(b=>b.addEventListener('click',()=>openRecord(b.dataset.id)));
 if($('reset'))$('reset').onclick=()=>{filters.forEach(f=>$(f).value='');setTrack('');};
}
function setTrack(value){track=value;document.querySelectorAll('.tracks button').forEach(b=>{b.classList.toggle('selected',b.dataset.track===track);b.setAttribute('aria-pressed',String(b.dataset.track===track));});render();}
function openRecord(id){
 const r=catalogue.find(x=>x.id===id);if(!r)return;
 const url=new URL(location.href);url.searchParams.set('agent',id);history.replaceState(null,'',url);
 let body=`<p class="eyebrow">${escapeHTML(r.id)} / TRACK ${escapeHTML(r.track)}</p><h2>${escapeHTML(r.name)}</h2><p>${escapeHTML(r.task)}</p><p class="warning">Evidence: ${escapeHTML(r.maturity)} · Maintenance: ${escapeHTML(r.maintenance)} · Security: ${escapeHTML(r.security)}</p>`;
 if(r.type==='commons'){
 body+=`<h3>Implemented capability</h3><p>${escapeHTML(r.task)}</p><ul>${r.limitations.map(t=>`<li>${escapeHTML(t)}</li>`).join('')}</ul><dl><dt>Backend</dt><dd>Deterministic Python; no model or external search calls</dd><dt>Inputs</dt><dd>${escapeHTML(r.required.join(', '))}</dd><dt>Species/context</dt><dd>${escapeHTML(r.species.join(', '))}; no species-wide validation</dd><dt>Costs</dt><dd>$0 provider charges. Uses your device’s CPU. No credentials required.</dd><dt>Local command</dt><dd><code>python -m commons run ${escapeHTML(r.id)}</code></dd><dt>Version</dt><dd><code>${escapeHTML(r.configuration.agent_version)}</code></dd><dt>Configuration</dt><dd><code>${escapeHTML(r.configuration.id)}</code></dd><dt>Source</dt><dd><a href="source.zip">Runnable source archive</a>${r.source?` · <a href="${safeURL(r.source)}">GitHub snapshot</a>`:' · GitHub publication pending'}</dd><dt>Planned extensions</dt><dd>${escapeHTML(r.planned_extensions)}</dd></dl><h3>Preliminary Evidence Card</h3><p>${escapeHTML(r.evidence.baseline)}</p><p>Agent: ${r.evidence.passed}/${r.evidence.n}. Simple baseline: ${r.evidence.baseline_passed}/${r.evidence.n}. Same cases and rubric. ${escapeHTML(r.evidence.uncertainty)}</p><p>Developer-authored automated checks. No independent review or real-study validation. Evaluation: ${escapeHTML(r.evaluated_at)}.</p><details><summary>Failures and full evaluation record</summary><pre>${json(r.evidence)}</pre></details><details><summary>Safe example input</summary><pre>${json(r.example_input)}</pre></details><details><summary>Input and output schemas</summary><pre>${json({input:r.input_schema,output:r.output_schema})}</pre></details><details><summary>Recorded actual example run (synthetic data)</summary><pre>${json(r.output)}</pre></details><div class="trial"><h3>Run this safe example</h3><p>No account, installation or paid provider. Downloads the pinned Pyodide runtime once, then executes the same Python source in your browser. The example is synthetic; no farm data is uploaded. Browser runtime identity differs from the recorded local evaluation.</p><button id="try-example">Run ${escapeHTML(r.id)} example</button> <span id="trial-status" role="status"></span><pre id="trial-output" hidden></pre></div><details><summary>Full Agent Card</summary><pre>${json(r.agent_card)}</pre></details>`;
 }else if(r.type==='external'){
 body+=`<p>${escapeHTML(r.description)}</p><a href="${safeURL(r.source)}">Canonical source at inspected commit →</a><h3>Documentation-level evidence review</h3><p>${escapeHTML(r.evidence_review.method)}</p><p>${escapeHTML(r.evidence_review.finding)}</p><p>${escapeHTML(r.evidence_review.limitation)}</p><p>Licence: ${escapeHTML(r.license)}. Checked ${escapeHTML(r.checked_at)}. Consult upstream installation instructions and licensing before reuse.</p>`;
 }else{body+=`<dl>${['intended_user','current_workaround','inputs','outputs','success_criteria','risks','proposed_benchmark','priority_basis'].map(k=>`<dt>${escapeHTML(k.replaceAll('_',' '))}</dt><dd>${escapeHTML(r[k])}</dd>`).join('')}</dl><p>Proposed gap, not a verified absence of existing tools. <a href="#contribute" id="contribute-gap">Contribute evidence</a>.</p>`;}
 $('detail-body').innerHTML=body;$('detail').showModal();$('close-detail').focus();
 if($('try-example'))$('try-example').onclick=()=>trial(r.id);
 if($('contribute-gap'))$('contribute-gap').onclick=()=> $('detail').close();
}
let trialWorker=null,trialTimer=null;
function stopTrial(){if(trialWorker)trialWorker.terminate();trialWorker=null;clearTimeout(trialTimer);}
function trial(id){
 stopTrial();$('try-example').disabled=true;$('trial-status').textContent='Loading runtime and running the example…';$('trial-output').hidden=true;
 trialWorker=new Worker('worker.js');
 const fail=message=>{stopTrial();if($('trial-status')){$('trial-status').textContent=message;$('try-example').disabled=false;}};
 trialTimer=setTimeout(()=>fail('Runtime limit reached. Retry or use the downloadable local source.'),60000);
 trialWorker.onerror=()=>fail('Runtime could not load. Check network access or use the source archive.');
 trialWorker.onmessage=e=>{if(e.data.error)return fail(e.data.error);clearTimeout(trialTimer);$('trial-status').textContent='Actual execution complete. Review warnings and provenance below.';$('trial-output').textContent=JSON.stringify(e.data.result,null,2);$('trial-output').hidden=false;$('try-example').disabled=false;stopTrial();};
 trialWorker.postMessage({agent_id:id});
}
$('close-detail').onclick=()=>{$('detail').close();stopTrial();};$('detail').addEventListener('close',()=>{stopTrial();const url=new URL(location.href);url.searchParams.delete('agent');history.replaceState(null,'',url);});
filters.forEach(f=>$(f).addEventListener(f==='search'?'input':'change',render));
document.querySelectorAll('.tracks button').forEach(b=>b.onclick=()=>setTrack(b.dataset.track));
$('show-gaps').onclick=()=>{filters.forEach(f=>$(f).value='');$('type').value='gap';setTrack('');$('catalogue').scrollIntoView();};
fetch('catalogue.json').then(r=>{if(!r.ok)throw Error();return r.json();}).then(data=>{catalogue=data;['modality','species','maintainer'].forEach(f=>{const values=[...new Set(data.flatMap(r=>Array.isArray(r[f])?r[f]:[r[f]]))].filter(Boolean).sort();values.forEach(v=>{const o=document.createElement('option');o.value=v;o.textContent=v;$(f).append(o);});});render();const selected=new URL(location.href).searchParams.get('agent');if(selected)openRecord(selected);}).catch(()=>{$('results').textContent='The catalogue could not load. Refresh this page or use the source archive.';});

// Optional browser tool surface shares the visible catalogue state.
if(document.modelContext?.registerTool){
 const lifecycle=new AbortController();
 const tool={name:'search_research_catalogue',title:'Search research tools',description:'Filter the visible curated research catalogue. An empty result does not establish that a capability is missing.',inputSchema:{type:'object',properties:{query:{type:'string'},track:{type:'string',enum:['','A','B','C']},record_type:{type:'string',enum:['','commons','external','gap']}},additionalProperties:false},annotations:{readOnlyHint:false,untrustedContentHint:true},execute(input){
  if(!input||typeof input!=='object'||Object.keys(input).some(k=>!['query','track','record_type'].includes(k))||('query' in input&&typeof input.query!=='string')||('track' in input&&!['','A','B','C'].includes(input.track))||('record_type' in input&&!['','commons','external','gap'].includes(input.record_type)))throw Error('Invalid catalogue filters');
  if(!catalogue.length)throw Error('Catalogue is still loading');
  filters.forEach(f=>$(f).value='');$('search').value=input.query||'';$('type').value=input.record_type||'';setTrack(input.track||'');
  return {count:$('count').textContent,record_ids:[...$('results').querySelectorAll('[data-id]')].map(b=>b.dataset.id),coverage:'Curated and incomplete'};
 }};
 try{Promise.resolve(document.modelContext.registerTool(tool,{signal:lifecycle.signal})).catch(()=>{});}catch{}
 window.addEventListener('pagehide',()=>lifecycle.abort(),{once:true});
}
