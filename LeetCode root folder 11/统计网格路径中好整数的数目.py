# 卧槽太恶心了， 这是要逼我加练digit DP?
class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        g = [[0] * 4 for _ in range(4)]
        x = 0
        for i in range(4):
            for j in range(4):
                g[i][j] = x
                x += 1

        ar = [0]
        i, j = 0, 0
        for c in directions:
            if c == 'R':
                j += 1
            else:
                i += 1
            ar.append(g[i][j])

        # print(ar)

        l, r = str(l).zfill(16), str(r).zfill(16)

        @cache
        def fn(i, prv, lf, hf):
            if i >= 16: return 1
            lw = 0 if not lf else int(l[i])
            hi = 9 if not hf else int(r[i])
            f = i in ar
            res = 0
            for j in range(max(prv, lw) if f else lw, hi + 1):
                res += fn(i + 1, j if f else prv, lf and j == lw, hf and j == hi)
            return res

        res = fn(0, 0, 1, 1)
        fn.cache_clear()
        return res