text = r"""3   4
4   3
2   5
1   3
3   9
3   3"""

text = open('2024/data/input1.txt', 'r').read()

from collections import Counter

def solve():
    rows = text.splitlines()
    first, second = [], []
    for row in rows:
        f, s = row.split('   ')
        first.append(int(f))
        second.append(int(s))
    first.sort()
    second.sort()

    sol1 = 0
    for f, s in zip(first, second):
        sol1 += abs(f - s)

    # part 2
    second = Counter(second)

    sol2 = 0
    for val in first:
        sol2 += val * second.get(val, 0)
    
    
    return sol1, sol2
print(solve())
