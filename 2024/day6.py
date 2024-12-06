"""
lookup table instead of matrix simplifies code significantly!
only search the path for loops.
"""


text = """"""
from tqdm import tqdm

text = open('2024/data/input6.txt', 'r').read()

matrix = {(x, y): c for x, row in enumerate(text.splitlines()) for y, c in enumerate(row)}
start = next(pos for pos, c in matrix.items() if c == '^')
print(start)

def simulate(grid):
    visited = set()
    x, y = start
    dx, dy = -1, 0
    while (x, y) in grid:
        if (x, y, dx, dy) in visited:
            return True, visited
        visited.add((x, y, dx, dy))
        if grid.get((x+dx, y+dy)) == '#':
            dx, dy = dy, -dx
        else: 
            x, y= x+dx, y+dy

    return False, visited

steps = {(x, y) for x, y, _, _, in simulate(matrix)[1]}
print(len(steps))
print(sum(simulate(matrix | {(x, y): '#'})[0] for x,y in tqdm(steps)))

            