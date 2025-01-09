text = open('2024/data/input4.txt', 'r').read()

text = text.splitlines()

def solve(matrix):
    m = len(matrix)
    n = len(matrix[0])
    count = 0
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    def check_word(x, y, dx, dy):
        if not (0 <= x + 3*dx < m and 0 <= y + 3*dy < n):
            return False
        return (matrix[x][y] == 'X' and 
                matrix[x+dx][y+dy] == 'M' and 
                matrix[x+2*dx][y+2*dy] == 'A' and 
                matrix[x+3*dx][y+3*dy] == 'S')
    
    for i in range(m):
        for j in range(n):
            for dx, dy in directions:
                if check_word(i, j, dx, dy):
                    count += 1
    
    return count



print(solve(text))

def q2(matrix):
    m = len(matrix)
    n = len(matrix[0])
    count = 0 
    
    def check_word(x, y):
        if not (1 <= x < m - 1 and 1 <= y < n - 1):
            return False
        
        if matrix[x][y] != 'A':
            return False
        
        return any([
            (matrix[x - 1][y - 1] == 'M' and 
                matrix[x + 1][y - 1] == 'M' and 
                matrix[x - 1][y + 1] == 'S' and 
                matrix[x + 1][y + 1] == 'S'),
                
            (matrix[x - 1][y - 1] == 'M' and 
                matrix[x + 1][y - 1] == 'S' and 
                matrix[x - 1][y + 1] == 'M' and 
                matrix[x + 1][y + 1] == 'S'),

            (matrix[x - 1][y - 1] == 'S' and 
                matrix[x + 1][y - 1] == 'M' and 
                matrix[x - 1][y + 1] == 'S' and 
                matrix[x + 1][y + 1] == 'M'),

            (matrix[x - 1][y - 1] == 'S' and 
                matrix[x + 1][y - 1] == 'S' and 
                matrix[x - 1][y + 1] == 'M' and 
                matrix[x + 1][y + 1] == 'M'),
        ])
    
    for i in range(m):
        for j in range(n):
            if check_word(i, j):
                count += 1

    return count


print(q2(text))