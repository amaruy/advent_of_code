text = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""

text = open('2024/data/input25.txt').read()

locks, keys = [], []
for x in text.split('\n\n'):
    if x[0] == '#':
        locks.append(x)
    else:
        keys.append(x)

s = len(locks[0].splitlines()) - 2 

def transform(m):
    new = [-1] * len(m[0])
    for row in m:
        for i, char in enumerate(row):
            if char == '#':
                new[i] += 1

    return new

locks = [transform(l.splitlines()) for l in locks]
keys = [transform(k.splitlines()) for k in keys]

def fit(i, j):
    lock = locks[j]
    key = keys[i]
    for l, k in zip(lock, key):
        if l + k > s:
            return False
        
    return True
    

combos = set()
for i in range(len(keys)):
    for j in range(len(locks)):
        if fit(i, j):

            combos.add((i, j))

print(len(combos))