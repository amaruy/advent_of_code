# text="""R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)"""

# text = open('2023/data/input18.txt', 'r').read()

# points = [(0, 0)] # starting from 0, 0
# d = {'D':(1, 0), 'R':(0, 1), 'L':(0, -1), 'U':(-1, 0)}
# d = {'1':(1, 0), '0':(0, 1), '2':(0, -1), '3':(-1, 0)} 
# import re
# p = re.compile(r'\((.*?)\)')
# for i, line in enumerate(text.splitlines()):
#     line = p.findall(line)[0]
#     steps, direction= line[1:-1], line[-1]

#     x, y = points[-1]
#     move = d[direction]
#     if move[0] != 0:
#         for i in range(1, int(steps, 16) + 1):
#             points.append((x + move[0] * i, y))
#     else:
#         for j in range(1, int(steps, 16) + 1):
#             points.append((x, y + move[1] * j))

# min_x, min_y = min(points, key=lambda x: x[0])[0], min(points, key=lambda x: x[1])[1]
# max_x, max_y = max(points, key=lambda x: x[0])[0], max(points, key=lambda x: x[1])[1]

# m, n = max_x - min_x + 1, max_y - min_y + 1
# matrix = [[0 for i in range(n)] for j in range(m)]
# for x, y in points:
#     matrix[x - min_x][y - min_y] = 1

# from collections import deque
# start = (140, 96)
# nodes = deque([start])
# while nodes:
#     x, y = nodes.popleft()
#     for i, j in d.values():
#         if (0 <= x + i < m) and (0 <= y + j < n) and not matrix[x + i][y + j]:
#             matrix[x + i][y + j] = 1
#             nodes.append((x + i, y + j))

# total = 0
# for row in matrix:
#     total += sum(row)

# print(total)

# import numpy as np
# import matplotlib.pyplot as plt


# # Display the matrix as an image
# plt.imshow(matrix, cmap='gray', interpolation='nearest')
# plt.axis('off')  # Turn off the axis
# plt.show()

plan = list(map(str.split, open('2023/data/input18.txt')))

dirs = {'R': (1,0), 'D': (0,1), 'L': (-1,0), 'U': (0,-1),
        '0': (1,0), '1': (0,1), '2': (-1,0), '3': (0,-1)}

def f(steps, pos=0, ans=1):
    for (x,y), n in steps:
        pos += x*n
        ans += y*n * pos + n/2

    return int(ans)

print(f((dirs[d],    int(s))          for d,s,_ in plan),
      f((dirs[c[7]], int(c[2:7], 16)) for _,_,c in plan))