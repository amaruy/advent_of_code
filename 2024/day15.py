from collections import defaultdict
from functools import cache

text = open('2024/data/input15.txt', 'r').read()

grid, moves = text.split('\n\n')
directions = {'>':(0, 1), 'v':(1, 0), '<':(0, -1), '^':(-1, 0)}
grid = grid.splitlines()
moves = moves.replace('\n', '')


pos = defaultdict(set)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        pos[grid[i][j]].add((i, j))

robot = '@'
pos[robot] = list(pos[robot])[0]


for m in moves:
    x, y = pos[robot]
    dx, dy = directions[m]
    if (x+dx, y+dy) in pos['#']:
        continue
    elif (x+dx, y+dy) in pos['.']:
        pos[robot] = (x+dx, y+dy)
        pos['.'].remove((x+dx, y+dy))
        pos['.'].add((x, y))
    else:
        while (x+dx, y+dy) in pos['O']:
            x, y = x+dx, y+dy
        if (x+dx, y+dy) in pos['#']:
            continue
        elif (x+dx, y+dy) in pos['.']:
            pos['.'].remove((x+dx, y+dy))
            pos['O'].add((x+dx, y+dy))
            x, y = pos[robot]
            pos['O'].remove((x+dx, y+dy))
            pos[robot] = (x+dx, y+dy)
            pos['.'].add((x, y))

f = lambda x: x[0] * 100 + x[1]
print(sum(map(f, list(pos['O']))))


"""
Q2
"""

extension = {'#':'##', '.':'..', '@':'@.', 'O':'[]'}
grid = [list("".join(map(lambda x: extension[x], row))) for row in grid]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            x, y = (i, j)
            break



@cache
def check(x, y, m):
    dx, dy = directions[m]
    if grid[x][y] == '@': return check(x+dx, y+dy, m)
    if grid[x][y] == '#': return False
    if grid[x][y] == '.': return True

    if m in '<>': return check(x+dx, y+dy, m)

    side = -1 if grid[x][y] == ']' else 1
    return check(x+dx, y+dy, m) and check(x+dx, y+side+dy, m)


def move(x, y, m, moved, carry='.'):
    if grid[x][y] != '.': 
        dx, dy = directions[m]
        moved.add((x, y))
        move(x+dx, y+dy, m, moved, carry=grid[x][y])
        if m in '^v':
            side = -1 if grid[x][y] == ']' else 1
            if grid[x][y] != '@' and (x, y+side) not in moved:
                    moved.add((x, y+side))
                    move(x, y+side, m, moved, carry='.')
            if carry == '@':
                grid[x][y+side] = '.'


    grid[x][y] = carry

for m in moves:
    check.cache_clear()
    if check(x, y, m):
        move(x, y, m, set())
        dx, dy = directions[m]
        x, y = x+dx, y+dy


pos = defaultdict(set)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        pos[grid[i][j]].add((i, j))
f = lambda x: x[0] * 100 + x[1]
print(sum(map(f, list(pos['[']))))
         
    

