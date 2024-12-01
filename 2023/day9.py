text="""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

import re
from typing import List, Tuple
text = open('/Users/yonatanamaru/Documents/advent_of_code/2023/data/data-day9.txt', 'r').read()

def parse(text: str) -> List[int]:
    lines = text.splitlines()
    return[[int(x) for x in line.split()] for line in lines]

def sum_calc(sequences: List[List[int]]) -> Tuple:
    r1 = 0
    r2 = 0
    for sequence in sequences:
        trail = [sequence]
        while any(x != 0 for x in trail[-1]):
            trail.append([trail[-1][i+1] - trail[-1][i] for i in range(len(trail[-1])-1)])
            
        r1 += sum([trail[i][-1] for i in range(len(trail))])
        r2 += sum([trail[i][0] * (1 - 2 * (i % 2)) for i in range(len(trail))])
    return (r1, r2)

print(sum_calc(parse(text)))
   



