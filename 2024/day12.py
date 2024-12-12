from collections import defaultdict, deque
text = open('2024/data/input12.txt', 'r').read()

matrix = text.splitlines()
m,n = len(matrix), len(matrix[0])
matrix = {(x, y): c for x, row in enumerate(text.splitlines()) for y, c in enumerate(row)}
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
edge_map = defaultdict(list)

def map_region(spot, type, dir=None):
    if matrix.get(spot) == F'#{type}':
        return 0, 0
    if matrix.get(spot) != type:
        edge_map[dir].append(spot)
        return 0, 1
    
    matrix[spot] = F'#{type}'         
    squares, edges = 1, 0
    for x, y in directions:
        s, e = map_region((spot[0] + x, spot[1] + y), type, (x,y))
        edges += e
        squares += s

    return squares, edges

def count_sides(edge_map):
    sides = 0
    
    for dir_key, points in edge_map.items():
        if not points:
            continue
        visited = set()
        points_set = set(points) 
        

        for p in points:
            if p not in visited:

                sides += 1

                q = deque([p])
                visited.add(p)
                while q:
                    cx, cy = q.popleft()
                    for dx, dy in directions:
                        nx, ny = cx + dx, cy + dy
                        if (nx, ny) in points_set and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            q.append((nx, ny))
    
    return sides
    

total = 0  
total2 = 0
for spot in matrix:
    if '#' not in matrix[spot]:
        edge_map = defaultdict(list)
        squares, edges = map_region(spot, matrix[spot])
        total += edges * squares
        total2 += squares * count_sides(edge_map)

print(total, total2)



