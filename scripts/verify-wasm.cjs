// Run with NODE_PATH pointing to an installed pyodide@0.27.7 package.
const fs=require('node:fs');
const path=require('node:path');
const {loadPyodide}=require('pyodide');
(async()=>{
 const py=await loadPyodide();
 const root=path.resolve(__dirname,'..');
 function copy(dir){for(const e of fs.readdirSync(path.join(root,dir),{withFileTypes:true})){
  const rel=dir+'/'+e.name;if(e.isDirectory())copy(rel);else if(e.name.endsWith('.py')){py.FS.mkdirTree('/app/'+path.dirname(rel));py.FS.writeFile('/app/'+rel,fs.readFileSync(path.join(root,rel),'utf8'));}
 }}copy('commons');
 const result=py.runPython(`import sys,json
sys.path.insert(0,'/app')
from commons.registry import specs
from commons.runner import run_agent
from commons.evaluation import evaluate
outputs={aid:run_agent(aid,spec['example']) for aid,spec in specs().items()}
assert len(outputs)==20
assert all(r['status'] not in ('abstained','unsupported_input') for r in outputs.values())
assert outputs['B5']['data']['statistics']['reading']['mean']==2
bench=evaluate()
assert all(c['passed'] for c in bench['cases'])
json.dumps({'runtime':sys.version,'agents':len(outputs),'cases':len(bench['cases']),'passed':sum(c['passed'] for c in bench['cases']),'configurations':{a:r['configuration_snapshot']['id'] for a,r in outputs.items()}})`);
 console.log(result);
})().catch(e=>{console.error(e);process.exit(1);});
