text="""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


rows = text.splitlines()
sol = 0
for row in rows:
    code, count = row.splitt(" ")
    count = [int(x) if x != ',' else -1 for x in count.split("")]
    n, m = len(code), len(count)
    row_sol = [0] * (n+1) 

    curr = 0
    j = 0
    for i in range(n): #???.### 1,1,3
        char = code[i]
        if char in '.?':
            if j == -1:


