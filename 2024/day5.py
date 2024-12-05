text = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

text = open('2024/data/input5.txt', 'r').read()

rules, orders = text.split('\n\n')

from collections import defaultdict

G = defaultdict(list)
for row in rules.splitlines():
    source, target = row.split('|')
    G[source].append(target) # maybe flip


def check(row):
    row = row.split(',')
    n = len(row)
    for i in range(n - 1):
        if not row[i + 1] in G[row[i]]:
            return 0
    
    return int(row[n // 2])

answer = 0
for row in orders.splitlines():
    answer += check(row)

print(answer)

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
