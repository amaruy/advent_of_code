text = """"""

text = open('2024/data/input5.txt', 'r').read()

rules, orders = text.split('\n\n')

from functools import cmp_to_key
from operator import eq

cmp =  cmp_to_key(lambda x, y: 1 - 2*(f'{x}|{y}' in rules))
ans1=ans2=0

for row in orders.splitlines():
    row = row.split(',')
    sorted_row = sorted(row, key=cmp)
    if eq(sorted_row, row):
        ans1 += int(row[len(row) // 2])
    else:
        ans2 += int(sorted_row[len(sorted_row) // 2])

print(ans1)
print(ans2)
