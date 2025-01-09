text = open('2024/data/input2.txt', 'r').read()

matrix = text.splitlines()
m,n = len(matrix), len(matrix[0])

def check_row(row):
    diffs = [row[i+1] - row[i] for i in range(len(row) - 1)]
    big = max(diffs)
    small = min(diffs)
    if big * small > 0 and 1 <= max(big, abs(small)) <= 3:
        return True
    return False

def solve(extra=False):
    ans = 0 
    for row in matrix:
        row = list(map(int, row.split()))
        safe = check_row(row)
        if not safe and extra:
            for i in range(len(row)):
                temp = row[:i] + row[i + 1:]
                safe = check_row(temp)
                if safe:
                    break
        ans += 1 if safe else 0
        
    return ans

print(solve())
print(solve(extra=True))