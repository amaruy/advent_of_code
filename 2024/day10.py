text = open('2024/data/input10.txt', 'r').read()

matrix = [list(map(int, list(row)))  for row in text.splitlines()]
m,n = len(matrix), len(matrix[0])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
count = [0]

def is_trail(i, j, current, trails):
    if not (0 <= i < m and 0 <= j < n):
        return
    
    if matrix[i][j] != current:# or (i, j) in trails: # Q1 
        return
    
    if current == 9:
        count[0] += 1
        trails.add((i, j))
        return
    
    for x, y in directions:
        is_trail(i+x, j+y, current+1, trails)


for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            trails = set()
            is_trail(i, j, 0, trails)

print(count[0])

