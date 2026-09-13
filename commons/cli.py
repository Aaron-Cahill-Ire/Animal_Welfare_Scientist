import argparse
import json
import sys
from pathlib import Path
from .registry import specs
from .runner import run_agent


def main():
    parser = argparse.ArgumentParser(description='Run bounded welfare research agents on public/synthetic inputs.')
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('list')
    run = commands.add_parser('run')
    run.add_argument('agent_id')
    run.add_argument('--input', help='JSON path; omit to use the documented synthetic example')
    run.add_argument('--output')
    run.add_argument('--max-input-bytes', type=int, default=1000000)
    run.add_argument('--max-sources', type=int, default=200)
    run.add_argument('--max-runtime-seconds', type=float, default=10)
    commands.add_parser('evaluate')
    commands.add_parser('build-site')
    flow = commands.add_parser('workflow')
    flow.add_argument('name', choices=['discovery','intervention','hardware','research'])
    flow.add_argument('--input')
    flow.add_argument('--resume', help='Saved workflow checkpoint JSON')
    flow.add_argument('--artifact', help='Explicit human decision or externally supplied results JSON')
    flow.add_argument('--output')
    args = parser.parse_args()
    try:
        if args.command == 'list':
            result = {aid: {'name': s['name'], 'task': s['task']} for aid, s in specs().items()}
        elif args.command == 'run':
            payload = json.loads(Path(args.input).read_text()) if args.input else specs()[args.agent_id]['example']
            result = run_agent(args.agent_id, payload, max_input_bytes=args.max_input_bytes, max_sources=args.max_sources, max_runtime_seconds=args.max_runtime_seconds)
        elif args.command == 'evaluate':
            from .evaluation import write_results
            result = write_results()
        elif args.command == 'build-site':
            from .site import build
            result = build()
        else:
            from .workflows import start, resume, example
            if args.resume:
                if not args.artifact:
                    parser.error('--resume requires --artifact')
                checkpoint = json.loads(Path(args.resume).read_text())
                if checkpoint.get('workflow') != args.name:
                    parser.error('Checkpoint belongs to a different workflow')
                result = resume(checkpoint, json.loads(Path(args.artifact).read_text()))
            else:
                result = start(args.name, json.loads(Path(args.input).read_text()) if args.input else example(args.name))
        text = json.dumps(result, indent=2, allow_nan=False)
        if getattr(args, 'output', None):
            Path(args.output).write_text(text + '\n')
        else:
            print(text)
        if args.command == 'evaluate' and any(not r['passed'] for r in result['cases']):
            return 1
        return 0
    except (KeyError, ValueError, OSError) as exc:
        print('Unable to complete: ' + str(exc), file=sys.stderr)
        return 2
