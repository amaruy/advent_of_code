text = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

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





