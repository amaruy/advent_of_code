from functools import cache

@cache
def r(n, i):
    if i == 0: return 1
    if n == 0: return r(1, i - 1)
    if len(s := str(n)) % 2 == 0: return r(int(s[:len(s) // 2]), i - 1) + r(int(s[len(s) // 2:]), i - 1)
    return r(n * 2024, i - 1)

print(sum(r(int(n), 75) for n in open('2024/data/input11.txt').read().split()))