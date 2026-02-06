# celebrate! this is the first dp on tree hard problem I solved, I cracked
# a few basic points and trick to do dp on tree (which is not very similar to the
# usual dp strategy)
class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        @cache
        def dfs(u, x, p):
            nonlocal k
            if 1<<x > 10**4: return 0
            sc = coins[u]>>x
            a, b = sc-k, sc//2
            for v in g[u]:
                if v == p: continue
                a += dfs(v, x, u)
                b += dfs(v, x+1, u)
            return max(a, b)
        return dfs(0, 0, -1)
