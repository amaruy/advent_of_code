import re

def solve(q=1):
    text = open('2024/data/input3.txt', 'r').read()

    muls = [(m.start(), 'mul', int(m.group(1)) * int(m.group(2))) 
            for m in re.finditer(r'mul\((\d+),(\d+)\)', text)]
    
    controls = [(m.start(), 'control', m.group(1)) 
                for m in re.finditer(r"(don't|do)\(\)", text)]
    
    operations = sorted(muls + controls)
    
    total = 0
    active = True
    
    for position, op_type, value in operations:
        if op_type == 'mul' and active:
            total += value
        elif q == 2 and op_type == 'control':
            active = (value == 'do')

    return total

print(solve(1))
print(solve(2))
