import time
import random
import importlib.util
import os

def load_module_from_path(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

ROOT = os.path.dirname(__file__)
new_mod = load_module_from_path('new_ttt', os.path.join(ROOT, 'ticTacToe.py'))
old_mod = None
old_path = os.path.join(ROOT, 'ticTacToe_old.py')
if os.path.exists(old_path):
    old_mod = load_module_from_path('old_ttt', old_path)
else:
    print('Note: ticTacToe_old.py not found — skipping old implementation benchmark')


def bench_module(mod, n=10, moves=1000, trials=100):
    Tic = getattr(mod, 'TicTacToe')
    total = 0.0
    calls = 0
    for t in range(trials):
        board = Tic(n)
        start = time.perf_counter()
        player = 1
        for m in range(moves):
            r = random.randrange(0, n)
            c = random.randrange(0, n)
            board.move(r, c, player)
            player = 1 if player == 2 else 2
        end = time.perf_counter()
        total += (end - start)
        calls += moves
    return total, calls


def run():
    random.seed(0)
    params = dict(n=50, moves=1000, trials=50)  # ~50k moves per implementation

    t_total_new, calls_new = bench_module(new_mod, **params)

    print('Parameters:', params)
    print('\nNew implementation:')
    print('  Total time: {:.6f}s for {} moves'.format(t_total_new, calls_new))
    print('  Avg per move: {:.9f}s'.format(t_total_new / calls_new))

    if old_mod is not None:
        t_total_old, calls_old = bench_module(old_mod, **params)
        print('\nOld implementation:')
        print('  Total time: {:.6f}s for {} moves'.format(t_total_old, calls_old))
        print('  Avg per move: {:.9f}s'.format(t_total_old / calls_old))

        speedup = (t_total_old / calls_old) / (t_total_new / calls_new)
        print('\nSpeedup (old per-move / new per-move): {:.3f}x'.format(speedup))
    else:
        print('\nOld implementation not available; benchmark skipped for old implementation.')

if __name__ == '__main__':
    run()
