"""Usage: python plot.py results/summary.csv (requires matplotlib)."""
import csv
import sys
from pathlib import Path
import matplotlib.pyplot as plt

source = Path(sys.argv[1] if len(sys.argv) > 1 else 'results/summary.csv')
with source.open(encoding='utf-8', newline='') as file:
    rows = list(csv.DictReader(file))
for kind, cases in [('sort', ['random', 'ascending', 'descending']),
                    ('search', ['found', 'missing'])]:
    for case in cases:
        selected = [r for r in rows if r['kind'] == kind and r['case'] == case]
        if not selected:
            continue
        fig, ax = plt.subplots(figsize=(8, 5))
        for name in dict.fromkeys(r['algorithm'] for r in selected):
            group = sorted((r for r in selected if r['algorithm'] == name), key=lambda r: int(r['n']))
            ax.plot([int(r['n']) for r in group], [float(r['mean_ms']) for r in group], 'o-', label=name)
        ax.set(xscale='log', yscale='log', xlabel='n', ylabel='Mean time per operation (ms)', title=f'{kind}: {case}')
        ax.grid(True, which='both', alpha=0.25)
        ax.legend()
        fig.tight_layout()
        fig.savefig(source.parent / f'{kind}_{case}.png', dpi=180)
        plt.close(fig)
