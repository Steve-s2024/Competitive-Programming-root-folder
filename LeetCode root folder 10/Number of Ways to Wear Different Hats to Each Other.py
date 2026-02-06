# ingenious shift of focus on the subject of being bitmasked
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(hats)
        mp = []
        for i in range(n): mp.append(set(hats[i]))
        @cache
        def fn(i, msk):
            nonlocal mod, n
            if i > 40: return 1 if msk == (1<<n)-1 else 0
            res = fn(i+1, msk)
            for j in range(n):
                if msk & 1 << j: continue
                if i not in mp[j]: continue
                res += fn(i + 1, msk | 1 << j)
                res %= mod
            return res

        return fn(1, 0)
