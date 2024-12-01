text="""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
text = open('data/input15.txt', 'r').read()

steps = text.split(",")
"""
Determine the ASCII code for the current character of the string.
Increase the current value by the ASCII code you just determined.
Set the current value to itself multiplied by 17.
Set the current value to the remainder of dividing itself by 256.
"""
def hash_func(seq: str) -> int:
    curr = 0
    for char in seq:
        curr += ord(char)
        curr *= 17
        curr %= 256
    
    return curr

total = 0
for step in steps:
    total += hash_func(step)
print(total)

from collections import defaultdict

box = [defaultdict(list) for _ in range(256)] # box[i] -> {'ab':[index, value]}
i = 0
for step in steps:
    if '=' in step:
        key, val = step.split('=')
        idx = hash_func(key)
        if key in box[idx]:
            box[idx][key][1] = val
        else:
            box[idx][key] = [i, val]

        i += 1
    else:
        key = step[:-1]
        idx = hash_func(key)
        if key in box[idx]:
            del box[idx][key]

total = 0
for i in range(256):
    b = sorted(box[i].values(), key=lambda x: x[0])
    for j in range(len(b)):
        total += (i+1) * (j+1) * int(b[j][1])

print(total)
