from collections import defaultdict
from itertools import combinations
text = open('2024/data/input8.txt', 'r').read()
m, n = len(text.splitlines()), len(text.splitlines()[0])
points = defaultdict(list)
for x, row in enumerate(text.splitlines()): 
    for y, value in enumerate(row):
        if value != '.': points[value].append((x, y))

antidotes = set()
for point_list in points.values():
    for (x1, y1), (x2, y2) in combinations(point_list, 2):
        x, y = (x1 + (x1 - x2), y1 + (y1 - y2))
        if (0 <= x < m and 0 <= y < n):
            antidotes.add((x, y))
        x, y = (x2 + (x2 - x1), y2 + (y2 - y1))
        if (0 <= x < m and 0 <= y < n): 
            antidotes.add((x, y))

print(len(antidotes))

antidotes = set()
for point_list in points.values():
    for (x1, y1), (x2, y2) in combinations(point_list, 2):
        x, y = x1, y1
        while 0 <= x < m and 0 <= y < n:
            antidotes.add((x, y))
            x, y = (x + (x1 - x2), y + (y1 - y2))
        x, y = x2, y2
        while 0 <= x < m and 0 <= y < n:
            antidotes.add((x, y))
            x, y = (x + (x2 - x1), y + (y2 - y1))

    
print(len(antidotes))

        

