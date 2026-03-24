# I suspected my state complexity is an overestimation
# the fact it passed in 8 seconds just proved that
# pretty genius DP design where start from the two end of palindrome and maintain the two path
# accordingly, where one must be the reverse of the other.
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], lab: str) -> int:

        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        @cache
        def fn(msk, u1, u2):
            if u1 == u2: return -1
            res = 0
            for v1 in g[u1]:
                if 1<<v1 & msk: continue
                for v2 in g[u2]:
                    if 1<<v2 & msk: continue
                    if lab[v1] == lab[v2]:
                        a = fn(msk | 1 << v1 | 1 << v2, v1, v2) + 2
                        res = max(res, a)
            if res == 0: return 0 if u1 in g[u2] else -inf
            return res

        res = 0
        for v1 in range(n):
            for v2 in range(n):
                if lab[v1] == lab[v2]:
                    a = fn(1 << v1 | 1 << v2, v1, v2) + 2
                    res = max(res, a)
        return res

