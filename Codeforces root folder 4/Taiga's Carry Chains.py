# first time ever solved D in div2 codeforces. 2025/12/05
from functools import cache


def solve():
    n, k = [int(e) for e in input().split()]
    s = str(bin(n))[2:]
    l = -1
    mp = [i for i in range(len(s))]
    for i, c in enumerate(s):
        if c != '1': l = i
        if s[i] == '1': mp[i] = l

    mp[len(s)-1] = l

    @cache
    def recursive(i, c, K):
        if i < 0: return K
        res = recursive(i-1, 0, K) # do nothing

        # add 1 to ith position
        if s[i] == '0' and K:
            if c:
                j = mp[i-1] if i else -1 # s[i] is actually '1'
                a = recursive(j, 1, K-1) + (i-j)
                res = max(res, a)
            else:
                a = recursive(i, 1, K-1)
                res = max(res, a)
        elif K:
            j = mp[i]
            a = recursive(j, 1, K-1) + (i-j)
            res = max(res, a)
        return res

    ans = recursive(len(s)-1, 0, k)
    print(ans)



for _ in range(int(input())): solve()


