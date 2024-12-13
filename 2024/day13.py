import re

games = open('2024/data/input13.txt', 'r').read().split('\n\n')
OFFSET = 10000000000000

def solve_machine(Ax, Ay, Bx, By, Px, Py):
    # Cramer's rule, Both must be integers and nonnegative (did'nt need nonnegative for my input).
    if (det:= Ax*By - Bx*Ay) == 0: return 0

    A_count = (Px*By - Bx*Py) / det
    B_count = (Ax*Py - Px*Ay) / det

    if A_count < 0 or B_count < 0 or not (A_count.is_integer() and B_count.is_integer()): return 0
    
    return int(3*A_count + B_count)

def solve(offset=0, total=0):
    for game in games:
        (Ax, Ay), (Bx, By), (Px, Py) = [tuple(map(int, re.findall(r'\d+', line))) for line in game.splitlines()]
        Px, Py = Px + offset, Py + offset
        total += solve_machine(Ax, Ay, Bx, By, Px, Py)

    print(total)

solve()
solve(OFFSET)


