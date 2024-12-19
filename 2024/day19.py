from functools import cache

text = open('2024/data/input19.txt', 'r').read()
towels, designs = text.split('\n\n')
towels = towels.split(', ')
designs =  designs.splitlines()

c = 0

@cache
def check(design: str):
    if not design: return True
    return any([check(design[len(t):]) for t in towels if design.startswith(t)])

@cache
def check(design: str):
    if not design: return True
    return sum([check(design[len(t):]) for t in towels if design.startswith(t)])



for design in designs:
    c += check(design)

print(c)
