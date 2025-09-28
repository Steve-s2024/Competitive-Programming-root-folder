# first time enjoyed the benefit bring by the amazing python bit int system, no other language can do this: 90%
# digit DP solution with lower and upper bound
class Solution:
    def convertToBase(self, s, b):
        num = int(s)
        res = []
        while num:
            res.append(num%b)
            num //= b
        return ''.join(str(e) for e in res)[::-1]


    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7
        l, r = self.convertToBase(l, b), self.convertToBase(r, b)
        n = len(r)
        l = l.zfill(n)
        @cache
        def recursive(i, mif, mxf, prv):
            nonlocal MOD, n
            if i >= n: return 1
            mi, mx = max(int(l[i]), prv) if mif else prv, int(r[i]) if mxf else b-1
            res = 0
            for j in range(mi, mx+1):
                res += recursive(i+1, mif and j == int(l[i]), mxf and j == int(r[i]), j)
                res %= MOD
            return res
        return recursive(0, 1, 1, 0)


