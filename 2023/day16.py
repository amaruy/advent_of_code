text = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

text = open('2023/data/input16.txt', 'r').read()

matrix = text.splitlines()
m,n = len(matrix), len(matrix[0])
# bfs
def count_light(start=(0, -1), direction=(0, 1)):
    current = [(start, direction)] # spot, direction
    seen = set()
    while current:
        next_batch = []
        for light in current:

            (i, j), (x, y) = light
            i += x
            j += y
            if not ((0 <= i < m) and (0 <= j < n)):
                continue

            if ((i, j), (x, y)) in seen:
                continue

            seen.add(((i, j), (x, y)))

            # if matrix[i][j] == ".":
            #     next_batch.append(((i, j),(x, y)))
            if matrix[i][j] == "-" and x != 0:
                next_batch.append(((i, j),(0, 1)))
                next_batch.append(((i, j),(0, -1)))
            elif matrix[i][j] == "|" and y != 0:
                next_batch.append(((i, j),(1, 0)))
                next_batch.append(((i, j),(-1, 0)))
            elif matrix[i][j] == "\\":
                next_batch.append(((i, j),(y, x)))
            elif matrix[i][j] == "/":
                next_batch.append(((i, j),(-y, -x)))
            else:
                next_batch.append(((i, j),(x, y)))

        current = next_batch

    # filter direction
    sol = set([spot for spot, direction in seen])
    return len(sol)

best = 0
for i in range(m): # check left and right starts
    best = max(best, count_light(start=(i, -1), direction=(0, 1)))
    best = max(best, count_light(start=(i, n), direction=(0, -1)))
for j in range(n): # check left and right starts
    best = max(best, count_light(start=(-1, j), direction=(1, 0)))
    best = max(best, count_light(start=(m, j), direction=(-1, 0)))



print(count_light())
print(best)