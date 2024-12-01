text = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
'''

#text = open('2023/data/input21.txt', 'r').read()

# idea: bfs with stack for 64 steps

text = text.splitlines()
steps = 10 #26501365
m, n = len(text), len(text[0])

for i in range(m):
    for j in range(n):
        if text[i][j] == 'S':
            start = (i, j)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
stack = set([start])
for _ in range(steps):
    next_stack = set()
    for node in stack:
        i, j = node
        for x, y in directions:
            if (0 <= i + x < m) and (0 <= j + y < n) and text[i+x][j+y] != '#':
                next_stack.add((i+x, j+y))

    stack = next_stack

print(len(next_stack))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


stack = set([start])
for _ in range(steps):
    next_stack = set()
    for node in stack:
        i, j = node
        for x, y in directions:
            if text[(i+x)%m][(j+y)%n] != '#':
                next_stack.add((i+x, j+y))

    stack = next_stack

print(len(next_stack))

x = sum([sum([1 if char != '#' else 0 for char in row]) for row in text])

print(4 * steps * 0.5 * (x / (m+n)))