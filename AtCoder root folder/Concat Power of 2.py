# i need to figure out is it me, or is it the bich ass atcoder problem setter.
# what a fking stupid way to solve. frustrating, could have got to 1200 with a better set of problem

def solve():
    n = int(input())
    ref = [(1<<i, len(str(1<<i))) for i in range(30)]
    @cache
    def fn(i, f, bf, prv):
        if i >= len(s): return 1 if not bf else 0
        res = 0
        if bf: res += fn(i+1, 0, 1, 0)
        for v, l in ref:
            if v == 128: continue
            if prv and v == 64: continue
            if i+l <= len(s) and (not f or v <= mp[i, i+l]):
                res += fn(i+l, f and v == mp[i, i+l], 0, v == 1)
        return res
    res = -1
    l, r = 1, 10**9
    while l <= r:
        m = (l+r)//2
        s = str(m)
        mp = {}
        for i in range(len(s)):
            for j in range(i, len(s)): mp[(i, j+1)] = int(s[i:j+1])
        x = fn(0, 1, 1, 0)
        fn.cache_clear()
        # print(m, x)
        if x >= n:
            res = m
            r = m-1
        else: l = m+1
    print(res)



solve()