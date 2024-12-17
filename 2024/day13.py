import re
import numpy as np

games = re.findall(r'(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)', open('2024/data/input13.txt').read(), re.S)
OFFSET = 10000000000000

def f(game):
    Ax, Ay, Bx, By, Px, Py = map(int, game)
    # Cramer's rule, Both must be integers and nonnegative (did'nt need nonnegative for my input).
    if (det:= Ax*By - Bx*Ay) == 0: return 0

    Px, Py = Px + OFFSET, Py + OFFSET
    A_count = (Px*By - Bx*Py) / det
    B_count = (Ax*Py - Px*Ay) / det

    if any([A_count < 0, B_count < 0, A_count % 1, B_count % 1]): return 0
    
    return int(3*A_count + B_count)

def solve(row):
    ax,ay,bx,by,px,py = map(int, row)
    M = np.array([[ax, bx], [ay, by]])
    P = np.array([px, py]) + 10000000000000
    R = np.round(np.linalg.solve(M, P))
    return R@(3,1) if (P==R@M.T).all() else 0


print(sum(map(solve, games)))




