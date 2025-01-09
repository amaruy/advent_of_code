text = open('2024/data/input17.txt', 'r').read()
import re
a, b, c, *p = map(int, re.findall(r'\d+', text))

def machine(a, b, c, i=0, out=[]):
    while i < len(p):
        C = {0:0, 1:1, 2:2, 3:3, 4:a, 5:b, 6:c}
        op = p[i+1]
        match p[i]:
            case 0: a >>= C[op]
            case 1: b ^= op
            case 2: b  = 7 & C[op]
            case 3: i  = op-2 if a else i
            case 4: b ^= c
            case 5: out = out + [C[op] & 7]
            case 6: b  = a >> C[op]
            case 7: c  = a >> C[op]
        i += 2
    return out

print(*machine(a, b, c), sep=',')

def find(a, i):
    if machine(a, b, c) == p: print(a)
    if machine(a, b, c) == p[-i:] or not i:
        for n in range(8): find(8*a+n, i+1)

find(0, 0)
