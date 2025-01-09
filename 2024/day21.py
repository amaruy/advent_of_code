text = '''179A
029A
980A
456A
379A
'''
text = open('2024/data/input21.txt').read()

"""
Two key points:
1. order : left up down right
2. minimal turns
"""

from functools import cache

numeric_pad = ["789", "456", "123", " 0A"]  
directional_pad = [" ^A", "<v>"] 

def find_path(pad, start, target):
    for y, row in enumerate(pad):
        for x, char in enumerate(row):
            if char == start:
                start_pos = (x, y)
            if char == target:
                target_pos = (x, y)
    
    def explore(x, y, path):
        if (x, y) == target_pos:
            return path + 'A'
            
        paths = [] # order matter!
        if x > target_pos[0] and pad[y][x-1] != ' ':  
            paths.append(explore(x-1, y, path + '<'))
        if y > target_pos[1] and pad[y-1][x] != ' ':  
            paths.append(explore(x, y-1, path + '^'))
        if y < target_pos[1] and pad[y+1][x] != ' ':  
            paths.append(explore(x, y+1, path + 'v'))
        if x < target_pos[0] and pad[y][x+1] != ' ': 
            paths.append(explore(x+1, y, path + '>'))
            
        return min(paths, key=lambda p: sum(a != b for a, b in zip(p, p[1:]))) # minimum directional changes
    
    return explore(start_pos[0], start_pos[1], "")

@cache
def solve(sequence, level):
    if level > 25:
        return len(sequence)
    
    pad = directional_pad if level else numeric_pad
    return sum(solve(find_path(pad, a, b), level + 1) 
              for a, b in zip('A' + sequence, sequence))

print(sum(map(lambda x: solve(x, 0) * int(x[:-1]), text.splitlines())))


