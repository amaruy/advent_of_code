text = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

#text = open('2023/data/input16.txt', 'r').read()

"""
A* with condition
Heuristic: Manhattan distance
"""
import heapq
from math import inf

matrix = text.splitlines()[1:]
m,n = len(matrix), len(matrix[0])
start, goal = (0, 0), (m-1, n-1)

def heuristic(position):
    # manhattan distance
    return (goal[0] - position[0]) + (goal[1] - position[1])

def get_neighbors(position):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for x, y in directions:
        neighbor = (position[0] + x, position[1] + y)
        if (0 <= neighbor[0] < m) and (0 <= neighbor[1] < n):
            neighbors.append(neighbor)

    return neighbors

def limitation(source, destination):
    # get sum of last 3
    x = source[0] - destination[0]
    y = source[1] - destination[1]
    for i in range(2):
        cf = came_from[source]
        if len(cf) > 1:
            return 0
        cf = cf[0]
        x += cf[0] - source[0]
        y += cf[1] - source[1]
        source = cf
    
    return inf if max(abs(x), abs(y)) > 3 else 0

open_set = []
heapq.heappush(open_set, (0, start))

came_from = {start:[start]}
g_score = [[inf for j in range(n)] for i in range(m)]
g_score[0][0] = 0

f_score = [[inf for j in range(n)] for i in range(m)]
f_score[0][0] = heuristic(start)

while open_set:
    current = heapq.heappop(open_set)[1]
    if current == goal:
        break

    for neighbor in get_neighbors(current):
        possible_g = g_score[current[0]][current[1]] + int(matrix[neighbor[0]][neighbor[1]]) + limitation(current, neighbor)

        if possible_g < g_score[neighbor[0]][neighbor[1]]:
            came_from[neighbor] =  [current]
            g_score[neighbor[0]][neighbor[1]] = possible_g
            f_score[neighbor[0]][neighbor[1]] = possible_g + heuristic(neighbor)

            if neighbor not in [x[1] for x in open_set]:
                heapq.heappush(open_set, (f_score[neighbor[0]][neighbor[1]], neighbor))
        
        elif possible_g < inf and possible_g == g_score[neighbor[0]][neighbor[1]]:
            came_from[neighbor].append(current)

print(g_score[m-1][n-1] - int(matrix[0][0]))



import heapq
from math import inf

# Parse the matrix from the text
text = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
matrix = text.splitlines()[1:]
m, n = len(matrix), len(matrix[0])

# Define start and goal positions
start, goal = (0, 0), (m - 1, n - 1)

# Heuristic function (Manhattan distance)
def heuristic(position):
    return abs(goal[0] - position[0]) + abs(goal[1] - position[1])

# Get valid neighbors
def get_neighbors(position):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for i, (dx, dy) in enumerate(directions):
        new_position = (position[0] + dx, position[1] + dy)
        if 0 <= new_position[0] < m and 0 <= new_position[1] < n:
            neighbors.append((new_position, i))  # Add direction index
    return neighbors

open_set = []
heapq.heappush(open_set, (0, start, -1, 0))  # (f_score, position, last_direction, steps_in_direction)

# Tracking structures
g_score = [[inf for _ in range(n)] for _ in range(m)]
g_score[start[0]][start[1]] = 0
f_score = [[inf for _ in range(n)] for _ in range(m)]
f_score[start[0]][start[1]] = heuristic(start)

while open_set:
    _, current, last_direction, steps_in_direction = heapq.heappop(open_set)
    
    # If we reached the goal, print the score
    if current == goal:
        print("Shortest path cost:", g_score[goal[0]][goal[1]] - int(matrix[start[0]][start[1]]))
        break
    
    for neighbor, direction in get_neighbors(current):
        # Check if the move is valid based on direction and steps in that direction
        if direction == last_direction:
            if steps_in_direction >= 4:
                continue  # Ignore if it exceeds the step limit
            new_steps_in_direction = steps_in_direction + 1
        else:
            new_steps_in_direction = 1

        # Calculate the tentative g_score for this neighbor
        tentative_g = g_score[current[0]][current[1]] + int(matrix[neighbor[0]][neighbor[1]])

        # Update scores if a shorter path is found
        if tentative_g < g_score[neighbor[0]][neighbor[1]]:
            g_score[neighbor[0]][neighbor[1]] = tentative_g
            f_score[neighbor[0]][neighbor[1]] = tentative_g + heuristic(neighbor)
            heapq.heappush(open_set, (f_score[neighbor[0]][neighbor[1]], neighbor, direction, new_steps_in_direction))

# If no path found
if g_score[goal[0]][goal[1]] == inf:
    print("No path found")