"""Generate real executions with clearly labelled synthetic approval/result artifacts."""
import json
from copy import deepcopy
from pathlib import Path
from .registry import specs
from .workflows import start, resume, example


def generate(root='examples/workflows'):
    root=Path(root);root.mkdir(parents=True,exist_ok=True)
    for name in ('discovery','intervention','hardware','research'):
        payload=example(name)
        state=start(name,payload)
        steps=[{'input':payload,'checkpoint':deepcopy(state)}]
        for _ in range(8):
            if state['status'] not in ('awaiting_human','awaiting_external'):break
            artifact={'checkpoint_id':state['checkpoint_id'],'data_classification':'synthetic','example_label':'SIMULATED decision/results; no actual approval, study or physical test', 'reviewer':'Synthetic demonstration reviewer','approved':True}
            if state['gate']=='protocol_review':
                protocol=deepcopy(specs()['C3']['example'])
                protocol['protocol'].update(population=payload['brief']['population'],outcomes=[payload['brief']['outcome']],research_question='Synthetic environmental noise comparison',hypothesis=payload['brief'])
                artifact.update(protocol)
            elif state['gate']=='registration':
                artifact['registration_reference']='Synthetic registration placeholder; no submission occurred'
            elif state['gate'] in ('bench_results','study_results'):
                artifact.update(results=deepcopy(specs()['B8']['example']['results']),sources=[{'id':'synthetic-test-results','passage':'Synthetic example error: 0.2 C. No physical test was conducted.'}],rows=[{'reading':1},{'reading':3}],columns=['reading'],deviations=[])
            state=resume(state,artifact)
            steps.append({'artifact':artifact,'checkpoint':deepcopy(state)})
        if state['status']!='completed':raise ValueError(name+' example did not complete')
        (root/(name+'.json')).write_text(json.dumps({'label':'Actual software execution on synthetic inputs with simulated human/external artifacts. No real approval or experiment.', 'steps':steps},indent=2)+'\n')
    return {'workflows':4,'output':str(root)}

if __name__=='__main__':print(json.dumps(generate()))
