import json
from pathlib import Path

def validate(path):
    data = json.loads(path.read_text(encoding='utf-8'))
    nodes = {n['id']: n for n in data['nodes']}
    assert len(nodes) == len(data['nodes']), 'Duplicate node IDs'
    links = {l[0]: l for l in data['links']}
    assert len(links) == len(data['links']), 'Duplicate link IDs'
    for lid, source, source_slot, target, target_slot, kind in links.values():
        output = nodes[source]['outputs'][source_slot]
        inp = nodes[target]['inputs'][target_slot]
        assert lid in (output.get('links') or []), f'Missing output reference: {lid}'
        assert inp.get('link') == lid, f'Missing input reference: {lid}'
        assert output['type'] in (kind, '*') and inp['type'] in (kind, '*'), f'Type mismatch: {lid}'
    for node in nodes.values():
        for slot, inp in enumerate(node.get('inputs', [])):
            if inp.get('link') is not None:
                link = links[inp['link']]
                assert link[3:5] == [node['id'], slot], 'Wrong input endpoint'
        for slot, output in enumerate(node.get('outputs', [])):
            for lid in output.get('links') or []:
                assert links[lid][1:3] == [node['id'], slot], 'Wrong output endpoint'
        if node['type'] == 'LoadImage':
            assert node['widgets_values'][0] == '', 'Source image must start blank'
        if node['type'] == 'SelectPromptPairHistory':
            assert node['widgets_values'][1:3] == ['', ''], 'Prompts must start blank'
        if node['type'] == 'CleanSlateImageMode':
            assert len(node['inputs']) == 2 and all(i['type'] == 'IMAGE' for i in node['inputs'])
    pending = set(nodes)
    while pending:
        ready = {n for n in pending if all(l[1] not in pending for l in links.values() if l[3] == n)}
        assert ready, 'Cycle found'
        pending -= ready
    for node in nodes.values():
        if node['type'] != 'SaveImage':
            continue
        seen, queue = set(), [node['id']]
        while queue:
            current = queue.pop()
            if current in seen:
                continue
            seen.add(current)
            queue.extend(l[1] for l in links.values() if l[3] == current)
        assert any(nodes[n]['type'] == 'KSampler' for n in seen), 'SaveImage bypasses generation'
        assert any(nodes[n]['type'] == 'CleanSlateImageMode' for n in seen), 'SaveImage bypasses mode selection'
    print(f'PASS: {path.name}: {len(nodes)} nodes, {len(links)} valid links, blank defaults, generation connected.')

if __name__ == '__main__':
    import sys
    validate(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / 'workflow.json')
