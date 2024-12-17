from re import findall
from statistics import variance


robots = [[int(n) for n in findall(r"(-?\d+)", item)] for item in open('2024/data/input14.txt').read().split("\n")]


W, L = 101, 103
T = 100

def step(t):
    return [((x + t*vx) % W, (y + t*vy) % H) for (x, y, vx, vy) in robots]

xt, xvar, yt, yvar = 0, 1000000, 0, 1000000
for t in range(L):
    x, y = zip(*step(t))
    if (xvart := variance(x)) < xvar: xt, xvar = t, xvart
    if (yvart := variance(y)) < yvar: yt, yvar = t, yvart

print(xt +((pow(W, -1, L)*(xt-yt)) % L)*W)




import re
from collections import Counter
import math

robots = [(int(a),int(b),int(c),int(d)) for a,b,c,d in re.findall(r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)',
                                                                  open('2024/data/input14.txt', 'r').read())]



print(math.prod(Counter(
    (x < w//2, y < l//2) for x,y in ((lambda p: ((p[0] + p[2]*100) % W, (p[1] + p[3]*t) % l))(r) for r in robots) 
    if x != w//2 and y != l//2).values()))

from re import findall
data = open("2024/data/input14.txt").read()
W, H = 101, 103

robots = [[int(n) for n in findall(r"(-?\d+)", item)] for item in data.split("\n")]

def simulate(t):
    return [((sx + t*vx) % W, (sy + t*vy) % H) for (sx, sy, vx, vy) in robots]

from statistics import variance
bx, bxvar, by, byvar = 0, 10*100, 0, 10*1000
for t in range(max(W,H)):
    xs, ys = zip(*simulate(t))
    if (xvar := variance(xs)) < bxvar: bx, bxvar = t, xvar
    if (yvar := variance(ys)) < byvar: by, byvar = t, yvar
print("Part 2:", bx+((pow(W, -1, H)*(by-bx)) % H)*W)
