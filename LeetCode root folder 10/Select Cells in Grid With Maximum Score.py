# pretty easy bitmask dp

class Solution:
    def maxScore(self, g: List[List[int]]) -> int:
        n, m = len(g), len(g[0])

        mp = defaultdict(set)
        for i in range(n):
            for j in range(m): mp[g[i][j]].add(i)

        ar = list(mp.keys())
        ar.sort(reverse=True)

        # print(ar, mp)
        @cache
        def fn(i, msk):
            if i >= len(ar): return 0
            res = fn(i + 1, msk)
            for j in mp[ar[i]]:
                if 1 << j & msk: continue
                res = max(res, fn(i + 1, msk | 1 << j) + ar[i])

            return res

        return fn(0, 0)