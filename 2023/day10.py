text="""7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S """

# find S
# four each of the 4 directions from S, step, add step to trail. 
# if we've reached the same spot from 2 directions: break



matrix = text.splitlines()
m, n = len(matrix), len(matrix[0])
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 'S':
            trails = []
            direct = []
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= i + x < m and 0 <= j + y < n:
                    trails.append((i + x, j + y))
                    direct.append((x, y))
            break

count = 1
while len(trails) == len(set(trails)):
    # check duplicate for breaking
    next_trail = []
    next_direct = []
    for (i, j), (x, y) in zip(trails, direct):
        pipe = matrix[x][y]
        if pipe == '|' and x != 0:
            next_trail.append(i+x, y)
            next_direct.append(x, y)
        if pipe == '-' and y != 0:
            next_trail.append(i, j+y)
            next_direct.append(x, y)
        if pipe == 'L' and x == -1:
            next_trail.append(i, j+1)
            next_direct.append(0, 1)
        if pipe == 'J' and x == -1:
            next_trail.append(i, j-1)
            next_direct.append(0, -1)
        if pipe == '7' and x == -1:
            next_trail.append(i, j+x)
            next_direct.append(x, y)
            


"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
"""    
def next_step(pipe: str, direction: tuple[int]) -> tuple[int]:
    x, y = direction
    d = {
        '|':(1,0),
        '-':(0, 1),
        ''
    } 
