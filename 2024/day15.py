text = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

#text = open('2024/data/input15.txt', 'r').read()

grid, moves = text.split('\n\n')
directions = {'>':(0, 1), 'v':(1, 0), '<':(0, -1), '^':(-1, 0)}
grid = grid.splitlines()
moves = moves.replace('\n', '')

"""
If the tile is #, the new map contains ## instead.
If the tile is O, the new map contains [] instead.
If the tile is ., the new map contains .. instead.
If the tile is @, the new map contains @. instead.
"""
from collections import defaultdict
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
grid, moves = text.split('\n\n')
directions = {'>':(0, 1), 'v':(1, 0), '<':(0, -1), '^':(-1, 0)}
grid = grid.splitlines()
moves = moves.replace('\n', '')

"""
If the tile is #, the new map contains ## instead.
If the tile is O, the new map contains [] instead.
If the tile is ., the new map contains .. instead.
If the tile is @, the new map contains @. instead.
"""
extension = {'#':'##', '.':'..', '@':'@.', 'O':'[]'}
grid = [list("".join(map(lambda x: extension[x], row))) for row in grid]


from collections import defaultdict
pos = defaultdict(set)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            start = (i, j)
            break

def check(x, y, m):
    dx, dy = m
    if grid[x][y] == '#': return False
    if grid[x][y] == '.': return True

    if m in '<>': return check(x+dx, y+dy, m)

    side = -1 if grid[x][y] == ']' else 1
    return check(x+dx, y+dy, m) and check(x+side, y+side, m)



def move(x, y, m, current):
    dx, dy = m
    if grid[x][y] == '.':
        grid[x][y] = current
        return
    
    next_val = grid[x][y]
    grid[x][y] = current

    if m in '<>':
        move(x+dx, y+dy, m, next_val)
        return 
    
    side = -1 if grid[x][y] == ']' else 1
    move(x+dx, y+dy, m, next_val)
    
    if grid[x][y] == ']':
         return check

    side = 1 if grid[x][y] == '[' else -1
    if move(x+dx, y+dy, m, grid[x][y]) and move(x, y+side, m, grid[x][y+side]):
        grid[x+dx][y+dy] = grid[x][y]
        grid[x][y] = last
        return True
        
        



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
        if m == '>':
            while (x+dx, y+dy) in pos['[']: 
                    x, y = x+dx, y+dy
                    x, y = x+dx, y+dy
            if (x+dx, y+dy) in pos['#']:
                continue
            elif (x+dx, y+dy) in pos['.']:
                pos['.'].remove((x+dx, y+dy))
                pos[']'].add((x+dx, y+dy))
                pos['['].add((x, y))
                x, y = pos[robot]
                pos['['].remove((x+dx, y+dy))
                pos[']'].remove((x + 2*dx, y + 2*dy))
                pos[robot] = (x+dx, y+dy)
                pos['.'].add((x, y))
        elif m == '<':
            while (x+dx, y+dy) in pos[']']: 
                    x, y = x+dx, y+dy
                    x, y = x+dx, y+dy
            if (x+dx, y+dy) in pos['#']:
                continue
            elif (x+dx, y+dy) in pos['.']:
                pos['.'].remove((x+dx, y+dy))
                pos['['].add((x+dx, y+dy))
                pos[']'].add((x, y))
                x, y = pos[robot]
                pos[']'].remove((x+dx, y+dy))
                pos['['].remove((x + 2*dx, y + 2*dy))
                pos[robot] = (x+dx, y+dy)
                pos['.'].add((x, y)) 
  


f = lambda x: x[0] * 100 + x[1]
print(sum(map(f, list(pos['O']))))

