text = """Time:        38     67     76     73
Distance:   234   1027   1157   1236"""
# text="""Time:      7  15   30
# Distance:  9  40  200"""
import re
from collections import Counter
from functools import reduce

p = re.compile(r'(\d+)')
times, distances = text.splitlines()
times = map(int, p.findall(times))
distances = map(int, p.findall(distances))


error_space = Counter()
for i, (time, distance) in enumerate(zip(times, distances)):
    speed = 0
    for _ in range(time):
        if speed * (time - speed) > distance:
            error_space[i] += 1
        speed += 1

mult = lambda x, y: x * y
print(reduce(mult, list(error_space.values())))


p = re.compile(r'(\d+)')
time, distance = text.splitlines()
time =  int("".join(p.findall(time)))
distance = int("".join(p.findall(distance)))


error_space = 1

speed = 0
for speed in range(time):
    if speed * (time - speed) > distance:
        break


x = time - 2 * speed + 1
print(x)