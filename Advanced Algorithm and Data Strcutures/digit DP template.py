# template for left and right bound (tested by LC testcases)
def dp(l, r) -> int:
    r = str(r)
    n = len(r)
    l = str(l).zfill(n)
    @cache
    def fn(i, lf, hf):
        lw = 0 if not lf else int(l[i])
        hi = 9 if not hf else int(r[i])
        res = 0
        for j in range(lw, hi + 1):
            res += fn(i + 1, lf and j == lw, hf and j == hi)
        return res

    res = fn(0,1, 1)
    fn.cache_clear()
    return res


    # not very generic digit DP template, modify it if can
def digitDP(self, n: int) -> int:
    s = str(n)
    @cache
    def recursive(i, lim):
        if i >= len(s): return 1
        res = 0
        mx = int(s[i]) if lim else 9
        res += recursive(i+1, lim and mx == int(s[i]))
        for j in range(10):
            if j <= mx: res += recursive(i+1, lim)
        return res
    return recursive(0, 1)




# with bitmask, didn't test it
def digitDPWithMask(self, n: int) -> int:
    s = str(n)
    @cache
    def recursive(i, mask, lim):
        if i >= len(s): return 1
        res = 0
        mx = int(s[i]) if lim else 9
        if mask == 0: res += recursive(i+1, mask, 0)
        for j in range(10):
            if j <= mx and (1<<j)&mask == 0: res += recursive(i+1, mask|(1<<j), lim)
        return res
    return recursive(0, 0, 1)
