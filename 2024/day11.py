text = open('2024/data/input11.txt', 'r').read()
from functools import cache

split = lambda x: (int(str(x)[:len(str(x)) // 2]), int(str(x)[len(str(x)) // 2:]))

@cache
def rec_count(stone, i):
    if i == 0: return 1
    if stone == 0: return rec_count(1, i - 1)
    if len(str(stone)) % 2 == 0: x1, x2 = split(stone); return rec_count(x1, i - 1) + rec_count(x2, i - 1)
    
    return rec_count(stone * 2024, i -1)

count = 0
for stone in map(int, text.split(' ')):
    for i in range(74): rec_count(stone, i)
    count += rec_count(stone, 75)

print(count)
    
