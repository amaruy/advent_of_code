text = open('2024/data/input22.txt').read()
num = 123

mix = lambda num1, num2: num1 ^ num2
prune = lambda num: num % 16777216

def hash(num, t=2000):
    num = int(num)
    for _ in range(t):
        num = prune(mix(num, num * 64))
        num = prune(mix(num, int(num /32)))
        num = prune(mix(num, num * 2048))

    return num

ans = list(map(hash, text.splitlines()))
print(sum(ans))


text = open('2024/data/input22.txt').read()
num = 123

mix = lambda num1, num2: num1 ^ num2
prune = lambda num: num % 16777216

def hash(num):
    num = prune(mix(num, num * 64))
    num = prune(mix(num, int(num /32)))
    num = prune(mix(num, num * 2048))

    return num

# create a mem of 10 * 4
# iterate over each num updating table
from itertools import product
from collections import deque

d = {tuple(p): 0 for p in product(range(-9, 10), repeat=4)}
for num in text.splitlines():
    num = int(num)
    last4 = deque()
    for _ in range(4):
        nnum = hash(num)
        last4.append(nnum % 10 - num % 10)
        num = nnum

    seen = set()
    for _ in range(2000-4):
        
        if tuple(last4) not in seen:
            d[tuple(last4)] += num % 10

        nnum = hash(num)
        seen.add(tuple(last4))
        diff = nnum % 10 - num % 10
        last4.popleft()
        last4.append(diff)
            
        num = nnum

print(max(d.values()))



        


