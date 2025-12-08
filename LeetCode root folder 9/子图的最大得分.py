# 写的不简单， 没想到那么多人比我先写出来 (2200~2300)
# 本质上是re-root dp
class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        mp = [{} for _ in range(n)]
        vs = set()

        def dfs(u):
            res = 0
            for v in g[u]:
                if v in vs: continue
                vs.add(v)
                a = dfs(v)
                res += a
                mp[u][v] = a
            return max(res + (1 if good[u] == 1 else -1), 0)

        vs.add(0)
        dfs(0)
        # print(res)
        # print(mp)
        ans = [0] * n
        vs = set()

        def recursive(u, pscore, brchscore):
            sm = 0
            for v in g[u]:
                if v in vs: continue
                if mp[u][v] > 0: sm += mp[u][v]
            sm += (1 if good[u] == 1 else -1)

            ans[u] = max(0, pscore - max(0, brchscore)) + sm
            for v in g[u]:
                if v in vs: continue
                vs.add(v)
                recursive(v, ans[u], mp[u][v])

        vs.add(0)
        recursive(0, 0, 0)
        return ans