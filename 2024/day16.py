text = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
"""
move - 1
rotate - 1000
S -> E

36 steps
7 turns
7036

"""
text = open('2024/data/input16.txt', 'r').read()
import heapq

grid = {(x, y):char for x, row in enumerate(text.splitlines()) for y, char in enumerate(row)}
dx, dy = 0, 1
stack = []
seen = set()
for (x,y), val in grid.items():
    if val == 'S':
        stack.append((0, x, y, dx, dy, set([(x, y)])))
        seen.add((x, y, dx, dy))
        break
best = 100_000
key_tiles = set()
while stack:
    value, x, y, dx, dy, tiles = heapq.heappop(stack)
    if value + 1 > best:
        break
    #print(f'{(x, y), (dx, dy)}', end=" ")
    # step
    if grid.get((x+dx, y+dy)) == 'E':
        if value + 1 > best:
            break
        else: 
            best = value + 1
            key_tiles = key_tiles.union(tiles)

    if grid.get((x+dx, y+dy)) == '.' and (x+dx, y+dy, dx, dy) not in seen:
        tiles = tiles.copy()
        tiles.add(((x+dx, y+dy)))
        heapq.heappush(stack, (value + 1, x+dx, y+dy, dx, dy, tiles))
        seen.add((x+dx, y+dy, dx, dy))
    if (x, y, -dy, dx) not in seen:
        heapq.heappush(stack, (value + 1000, x, y, -dy, dx, tiles))
        seen.add((x, y, -dy, dx))
    if (x, y, dy, -dx) not in seen:
        heapq.heappush(stack, (value + 1000, x, y, dy, -dx, tiles))
        seen.add((x, y, dy, -dx))

print(best)
print(len(key_tiles))

# matrix = [list(row) for row in text.splitlines()]
# for x, y in seen:
#     matrix[x][y] = 'O'

# for row in matrix:
#     print("".join(row))



# Find S and E
start = None
end = None
for (x, y), val in grid.items():
    if val == 'S':
        start = (x, y)
    elif val == 'E':
        end = (x, y)

dx, dy = 0, 1  # initial direction facing right (example)

# Priority queue: elements are (cost, x, y, dx, dy, tiles_visited)
pq = []
heapq.heappush(pq, (0, start[0], start[1], dx, dy, {(start[0], start[1])}))

dist = {}  # dist[(x,y,dx,dy)] = minimal cost to reach this state
dist[(start[0], start[1], dx, dy)] = 0

best = float('inf')
key_tiles = set()

while pq:
    cost, x, y, dx, dy, tiles = heapq.heappop(pq)

    # If we popped a state that is worse than known, skip
    if cost > dist.get((x, y, dx, dy), float('inf')):
        continue

    # Check forward move
    fx, fy = x + dx, y + dy
    forward_cost = cost + 1
    if (fx, fy) == end:
        # Found a path to E
        if forward_cost < best:
            best = forward_cost
            key_tiles = tiles.union({end})
        elif forward_cost == best:
            key_tiles = key_tiles.union(tiles).union({end})
        # Don't stop, continue to find all shortest paths
    elif grid.get((fx, fy)) == '.':
        # Move forward if this is a shortest or equally short route
        old_cost = dist.get((fx, fy, dx, dy), float('inf'))
        if forward_cost < old_cost:
            dist[(fx, fy, dx, dy)] = forward_cost
            new_tiles = tiles.copy()
            new_tiles.add((fx, fy))
            heapq.heappush(pq, (forward_cost, fx, fy, dx, dy, new_tiles))
        elif forward_cost == old_cost:
            # Equal cost: still consider this path to gather all tiles
            new_tiles = tiles.copy()
            new_tiles.add((fx, fy))
            heapq.heappush(pq, (forward_cost, fx, fy, dx, dy, new_tiles))

    # Rotate left
    left_dx, left_dy = -dy, dx
    left_cost = cost + 1000
    old_cost = dist.get((x, y, left_dx, left_dy), float('inf'))
    if left_cost < old_cost:
        dist[(x, y, left_dx, left_dy)] = left_cost
        # same tiles, no new tile visited
        heapq.heappush(pq, (left_cost, x, y, left_dx, left_dy, tiles))
    elif left_cost == old_cost:
        # If equal cost, add to pq as well
        heapq.heappush(pq, (left_cost, x, y, left_dx, left_dy, tiles))

    # Rotate right
    right_dx, right_dy = dy, -dx
    right_cost = cost + 1000
    old_cost = dist.get((x, y, right_dx, right_dy), float('inf'))
    if right_cost < old_cost:
        dist[(x, y, right_dx, right_dy)] = right_cost
        heapq.heappush(pq, (right_cost, x, y, right_dx, right_dy, tiles))
    elif right_cost == old_cost:
        heapq.heappush(pq, (right_cost, x, y, right_dx, right_dy, tiles))


print("Shortest cost:", best)
print(len(key_tiles))
# matrix = [list(row) for row in text.splitlines()]
# for (X, Y) in key_tiles:
#     if matrix[X][Y] == '.':
#         matrix[X][Y] = 'O'

# for row in matrix:
#     print("".join(row))