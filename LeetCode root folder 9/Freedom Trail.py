# a bit challenging, but pretty standard dp
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(key)
        mp = defaultdict(list)
        for i, c in enumerate(ring): mp[c].append(i)
        m = len(ring)
        @cache
        def recursive(i, j):
            nonlocal n, m
            if i >= n: return 0
            res = inf
            for k in mp[key[i]]:
                dst = abs(j-k)
                a = recursive(i+1, k) + min(dst, m-dst) + 1
                res = min(res, a)
            return res
        return recursive(0, 0)