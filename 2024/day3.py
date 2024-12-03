def solve():
    text = r"""xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
    text = open('2024/data/input3.txt', 'r').read()
    i = 0
    n = len(text)
    do = True
    ans = 0
    nums = '1234567890'
    while i < len(text) - 7:
        if do and text[i:i+4] == 'mul(':
            if text[i+4] in nums:
                j = i + 5
                while j < n and text[j] in nums:
                    j += 1
                if j < n  and text[j] == ',':
                    k = j + 1
                    while k < n and text[k] in nums:
                        k += 1
                    if j + 1 < k < n and text[k] == ')':
                        ans += int(text[i+4:j]) * int(text[j+1:k]) 
        elif text[i] == 'd':
            if text[i:i+7] == "don't()":
                do = False
            elif text[i:i+4] == 'do()':
                do = True
        i += 1

    return ans  

print(solve())
