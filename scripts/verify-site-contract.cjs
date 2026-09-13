// Dependency-free check of the site data/assets and browser-worker contract.
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const path=require('node:path');
const root=path.resolve(__dirname,'..');
const rows=JSON.parse(fs.readFileSync(path.join(root,'dist/catalogue.json')));
assert.equal(rows.length,33);
assert.equal(rows.filter(r=>r.type==='commons').length,20);
assert.equal(rows.filter(r=>r.type==='external').length,5);
assert.equal(rows.filter(r=>r.type==='gap').length,8);
const bundled=JSON.parse(fs.readFileSync(path.join(root,'dist/runtime.json')));
assert.ok(bundled['commons/runner.py']);
for(const r of rows.filter(r=>r.type==='commons')){
 assert.ok(r.example_input);assert.ok(r.output.data);assert.equal(r.output.configuration_snapshot.id,r.configuration.id);
 assert.equal(r.evidence.configuration_snapshot.id,r.configuration.id);
 assert.ok(r.evidence.n>=4);assert.ok(r.limitations.length);assert.ok(r.agent_card.input_example);
}
// Exercise the exact worker's invalid input path; no received code is evaluated.
let message;
const context={self:{postMessage:x=>message=x},importScripts:url=>assert.equal(url,'https://cdn.jsdelivr.net/pyodide/v0.27.7/full/pyodide.js'),loadPyodide:async()=>({FS:{mkdirTree(){},writeFile(){}},globals:{set(){}},runPython(){throw Error('Must never execute for invalid id');}}),fetch:async()=>({ok:true,json:async()=>bundled})};
vm.createContext(context);vm.runInContext(fs.readFileSync(path.join(root,'web/worker.js'),'utf8'),context);
(async()=>{await context.self.onmessage({data:{agent_id:"__import__('os')"}});assert.ok(message.error.includes('Unknown example'));console.log('33 catalogue records, aligned evidence identities, bundled source and invalid-worker-input contract passed.');})().catch(e=>{console.error(e);process.exit(1);});
