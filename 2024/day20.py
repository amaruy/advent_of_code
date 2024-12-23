text = open('2024/data/input20.txt').read()

grid = {(x, y): c for x, r in enumerate(text.splitlines()) for y, c in enumerate(r)}
x, y = next(pos for pos, v in grid.items() if v == 'S')


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

path = {}
steps = 0

while grid.get((x, y)) != 'E':
    path[(x, y)] = steps
    grid[(x, y)] = 'O'
    x, y = next((x + d[0], y + d[1]) for d in directions
                if grid.get((x + d[0], y + d[1])) in '.E')
    steps += 1
path[(x, y)] = steps


def shortcuts(cheats=2, minimum=100):
    count = 0
    for pos, steps in path.items():
        frontier = {pos}
        seen = {pos}
        
        for i in range(1, cheats + 1):
            frontier = {(x + dx, y + dy)
                       for x, y in frontier
                       for dx, dy in directions
                       if (x + dx, y + dy) in grid and (x + dx, y + dy) not in seen}
            seen |= frontier
            count += sum(p in path and path[p] - steps - i >= minimum for p in frontier) 
            
    return count

print(shortcuts())
print(shortcuts(20))
