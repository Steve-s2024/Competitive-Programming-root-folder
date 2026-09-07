# what a nasty Digit DP question



def solve():
    M = 998244353
    s = input()
    n = len(s)


    @cache
    def fn(i, msk, re, hf, bf, tf):
        if i >= n:
            if bf: return 0
            if msk.bit_count() != 3 and not tf and re == 0: return 1
            if msk.bit_count() != 3 and tf and re != 0: return 1
            if msk.bit_count() == 3 and not tf and re != 0: return 1
            return 0
        res = 0
        hi = 9 if not hf else int(s[i])
        for j in range(hi + 1):
            if not bf or j:
                nmsk = msk | 1 << j
                if nmsk.bit_count() == 4: nmsk = (1<<10)-1
            else: nmsk = msk
            res += fn(i + 1, nmsk, (re + j) % 3, hf and j == hi, bf and j == 0, tf or j==3)
        return res % M

    res = fn(0, 0,0, 1, 1, 0)
    print(res)

solve()