text = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

text = open('2024/data/input18.txt', 'r').read()
n = 71
matrix= [['.'] * n for _ in range(n)]

points = [(int(row.split(',')[1]), int(row.split(',')[0])) for row in text.splitlines()]
# for x, y in points[:12]:
#     matrix[x][y] = '#'

# for row in matrix:
#     print("".join(row))
import heapq

def bfs(b):
    blocked = set(points[:b])
    stack = [(0, 0, 0)] # cost, x, y
    blocked.add((0, 0))
    goal = (n-1, n-1)

    

    while stack:
        cost, x, y = heapq.heappop(stack)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (x+dx, y + dy) == goal:
                return True, cost + 1
            if 0 <= x + dx < n and 0 <= y + dy < n and (x+dx, y + dy) not in blocked:
                heapq.heappush(stack, (cost+1, x+dx, y + dy))
                blocked.add((x+dx, y + dy))
    
    return False, points[b-1]

from tqdm import tqdm
for b in range(1024, 3451):
    complete, val = bfs(b)
    if not complete:
        print(complete, val)
        break



