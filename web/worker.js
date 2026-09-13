/* Executes only allowlisted bundled Python examples, never received code. */
self.onmessage=async event=>{
 try{
  importScripts('https://cdn.jsdelivr.net/pyodide/v0.27.7/full/pyodide.js');
  const pyodide=await loadPyodide({indexURL:'https://cdn.jsdelivr.net/pyodide/v0.27.7/full/'});
  const response=await fetch('runtime.json');if(!response.ok)throw Error('Unable to load bundled source');
  const files=await response.json();
  for(const [path,content] of Object.entries(files)){
   if(!/^commons\/[a-z_\/]+\.py$/.test(path))throw Error('Invalid bundled module path');
   const parts=path.split('/');parts.pop();pyodide.FS.mkdirTree('/app/'+parts.join('/'));
   pyodide.FS.writeFile('/app/'+path,content);
  }
  if(!/^(A[1-6]|B[1-8]|C[1-6])$/.test(event.data.agent_id))throw Error('Unknown example');
  pyodide.globals.set('selected_agent',event.data.agent_id);
  const value=pyodide.runPython(`import sys, json
sys.path.insert(0, '/app')
from commons.registry import specs
from commons.runner import run_agent
json.dumps(run_agent(selected_agent, specs()[selected_agent]['example']), allow_nan=False)`);
  self.postMessage({result:JSON.parse(value)});
 }catch(error){self.postMessage({error:'Example unavailable: '+String(error.message||error)});}
};
