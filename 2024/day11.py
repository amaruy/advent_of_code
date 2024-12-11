text = """125 17"""
text = open('2024/data/input11.txt', 'r').read()

# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
from functools import cache
from tqdm import tqdm
allstones = map(int, text.split(' '))
count = 0

split = lambda x: (int(str(x)[:len(str(x)) // 2]), int(str(x)[len(str(x)) // 2:]))

@cache
def recursive_with_memo(stone, i):
    if i == 0:
        return 1
    
    if stone == 0:
        return recursive_with_memo(1, i - 1)
    
    if len(str(stone)) % 2 == 0:
        x1, x2 = split(stone)
        return recursive_with_memo(x1, i - 1) + recursive_with_memo(x2, i - 1)
    
    return recursive_with_memo(stone * 2024, i -1)

count = 0
for stone in allstones:
    for i in tqdm(range(74)):
        recursive_with_memo(stone, i)
    count += recursive_with_memo(stone, 75)

print(count)
    
