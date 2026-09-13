from importlib import import_module


def modules():
    return [import_module('commons.agents.track_' + t) for t in ('a', 'b', 'c')]


def specs():
    return {agent: spec for module in modules() for agent, spec in module.SPECS.items()}


def resolve(agent_id):
    if agent_id not in [f'{t}{i}' for t, n in [('A', 6), ('B', 8), ('C', 6)] for i in range(1, n+1)]:
        raise ValueError('Unknown agent: ' + str(agent_id))
    module = import_module('commons.agents.track_' + agent_id[0].lower())
    return module, module.SPECS[agent_id]
