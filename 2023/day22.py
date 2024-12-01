text = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
'''

#text = open('2023/data/input22.txt', 'r').read()
text = text.splitlines()
blocks = []
xsize, ysize = 0, 0
for line in text:
    start, end = line.split('~')
    start, end = start.split(','), end.split(',')
    blocks.append([[int(start[0]), int(end[0])], 
                   [int(start[1]), int(end[1])], 
                   [int(start[2]), int(end[2])]])
    xsize, ysize = max(xsize, end[0]), max(ysize, end[1])
    
blocks.sort(key=lambda block: block[2][0])
zsize = blocks[-1][-1][-1]

stacks = [[] * ysize for x in range(xsize)] 
for block in blocks:
    
    

