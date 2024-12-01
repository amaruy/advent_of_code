from typing import List, Tuple, Dict
import re
from math import lcm

text='''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''.splitlines()

text = open('/Users/yonatanamaru/Documents/advent_of_code/2023/data/data-day8.txt', 'r').readlines()

def parse(lines: List[str]) -> Tuple[str, Dict[str, Dict]]:
    instructions = lines[0].strip()
    p = re.compile(r'(\w\w\w)')
    d = {}
    for line in lines[2:]:
        source, left, right = p.findall(line)
        d[source] = {'L':left, 'R':right}
    
    return (instructions, d)

def navigate(lines: List[str], start, end) -> int:
    instructions, d = parse(text)
    current = start
    count = 0
    while not current.endswith(end):
        i = count % len(instructions)
        current = d[current][instructions[i]]
        count += 1
    return count

print(navigate(text, 'AAA', 'ZZZ'))
#print(navigate(text, 'A', 'Z'))
def sim(text, start, end):
    # calc end points for all starts
    instructions, d = parse(text)
    starts = [x for x in d.keys() if x.endswith(start)]
    counts = []
    for start in starts:
        counts.append(navigate(text, start, end))

    return lcm(*counts)

print(sim(text, 'A', 'Z'))




