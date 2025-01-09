from collections import deque

text = open('2024/data/input9.txt', 'r').read()
def map2desk(text: str) -> deque:
    desk = deque()
    for i, num in enumerate(map(int, text)):
        value = None if i % 2 else i // 2
        desk += [value] * num

    return desk

idx = 0
desk = map2desk(text)
checksum = 0
while desk:
    value = desk.popleft()
    if value is None:
        while not desk[-1]:
            desk.pop()
        value = desk.pop()
    checksum += idx * value
    idx += 1

print(checksum)

def map2desk(text: str) -> deque:
    desk = deque()
    idx = 0
    for i, num in enumerate(map(int, text)):
        if i % 2:
            desk.append([None, idx, num])
        else: 
            desk.append([i // 2, idx, num])
        idx += num

    return desk


desk = map2desk(text)
checksum = 0
while desk:
    spare = 0
    value, start, count = desk.popleft()
    if value is None:
        while desk and desk[-1][2] == 0:
            desk.pop()

        for i in range(len(desk) - 1, -1, -1):
            if desk[i][0] is not None and 0 < desk[i][2] <= count:
                value = desk[i][0]
                count, spare = desk[i][2], count - desk[i][2]
                desk[i][2] = 0
                if spare:
                    desk.appendleft((None, start+count, spare))
                break

    
    if value:
        more = sum(value * j for j in range(start, start + count))
        checksum += more
    

print(checksum)
        



    


