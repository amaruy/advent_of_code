text = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


text = open('data/input11.txt', 'r').read()

# expand and find star locations
matrix = text.splitlines()
m,n = len(matrix), len(matrix[0])

expand = 1000000 -1
rows = [expand] * m
cols = [expand] * n
stars = []

from tqdm import tqdm
print('finding stars')
for i in range(m):
    for j in range(n):
        if matrix[i][j] == '#':
            rows[i] = 0
            cols[j] = 0
            stars.append((i, j))


def distance(point1, point2, d):
    if point1 == point2:
        return 0
    
    x1, y1 = point1
    x2, y2 = point2

    extra_x = sum(rows[x1:x2]) if x1 < x2 else sum(rows[x2:x1])
    extra_y = sum(cols[y1:y2]) if y1 < y2 else sum(cols[y2:y1])

    total = abs(x1-x2) + abs(y1-y2) + extra_x + extra_y

    return total

k = len(stars)
sol = 0

print('calculating distances')
for i in tqdm(range(k-1)):
    for j in range(i+1, k):
        # left or right?
        if stars[i][1] < stars[j][1]:
            direction = 1 # go right
        elif stars[i][1] > stars[j][1]:
            direction = -1
        else: 
            direction = 0
        sol += distance(stars[i], stars[j], direction)

print(sol)





