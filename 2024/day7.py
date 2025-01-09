text = open('2024/data/input7.txt', 'r').read()

equations = [(int(num), [int(x) for x in vals.split()]) for num, _, vals in (line.partition(': ') for line in text.splitlines())]

def solve(value, curr, numbers):
    if not numbers and curr == value: return True 
    if curr > value or not numbers: return False 
    return solve(value, curr * numbers[0], numbers[1:]) or solve(value, curr + numbers[0], numbers[1:])

ans1 = 0
for val, equation in equations:
    if solve(val, equation[0], equation[1:]):
        ans1 += val
print(ans1)

def solve(value, curr, numbers):
    if not numbers and curr == value: return True 
    if curr > value or not numbers: return False 
    return solve(value, curr * numbers[0], numbers[1:]) or solve(value, curr + numbers[0], numbers[1:]) or solve(value, int(str(curr) + str(numbers[0])), numbers[1:]) 

ans2 = 0 
for val, equation in equations:
    if solve(val, equation[0], equation[1:]):
        ans2 += val
print(ans2)





