# tricky observation, but not complicated at all.

def solve():
    n = int(input())
    s = str(n)
    if '7' in s:
        print(0)
    else:
        minCnt = 9
        for i in range(1, len(s)+1):
            cnt = 0
            val = int('9'*i)
            tmp = n
            while cnt < 10 and '7' not in str(tmp):
                tmp += val
                cnt += 1
            minCnt = min(minCnt, cnt)

        print(minCnt)


t = int(input())
for i in range(t):
    solve()


# brute force TLE

def solve():
    n = int(input())
    size = len(str(n))+1
    def recursive(num, cnt):
        print(num)
        nonlocal size
        if '7' in str(num):
            return cnt
        res = float('inf')
        for i in range(1, size+1):
            cur = int('9'*i)
            res = min(res, recursive(num+cur, cnt+1))
        return res

    res = recursive(n, 0)
    print(res)




t = int(input())
for i in range(t):
    solve()