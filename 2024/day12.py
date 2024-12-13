from collections import defaultdict

matrix = {(x, y): c for x, row in enumerate(open('2024/data/input12.txt').read().splitlines()) for y, c in enumerate(row)}
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def map_region(spot, ch, dir=None):
    if matrix.get(spot) == f'#{ch}': return 0
    if matrix.get(spot)!= ch:
        edge_map[dir].append(spot)
        return 0
    matrix[spot] = f'#{ch}'
    return sum(map_region((spot[0]+dx, spot[1]+dy), ch, (dx, dy)) for dx, dy in directions) + 1

def count_sides(e_map):
    sides = 0
    for points in e_map.values():
        visited = set()
        for p in points:
            if p in visited: continue
            sides += 1
            stack = [p]
            visited.add(p)
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    neighbor = (x + dx, y + dy)
                    if neighbor in points and neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
    return sides

total=total2=0
for spot, ch in list(matrix.items()):
    if '#' not in ch:
        edge_map = defaultdict(list)
        s = map_region(spot, ch)
        total += sum(len(val) for val in edge_map.values()) * s
        total2 += s * count_sides(edge_map)

print(total, total2)