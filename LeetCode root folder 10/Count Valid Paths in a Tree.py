# very boring re-root DP

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        P = [1] * (n+1)
        P[0], P[1] = 0 ,0
        for i in range(int(sqrt(n))+1):
            if P[i] == 0: continue
            for j in range(i * i, n+1, i): P[j] = 0
        # print(P)


        g = [[] for _ in range(n+1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        mp = [None for _ in range(n+1)]

        def dfs(u, p):
            x, y = 0, 0
            for v in g[u]:
                if v == p: continue
                X, Y = dfs(v, u)
                x, y = x + X, y + Y
            mp[u] = [y+1 if P[u] else x, y+1 if not P[u] else 0]
            return mp[u]

        dfs(1, -1)

        # print(mp)
        res = 0
        def fn(u, p):
            nonlocal res
            res += mp[u][0]
            if P[u]: res -= 1
            for v in g[u]:
                if v == p: continue
                if P[v]: mp[v][0] += mp[u][1] if not P[u] else 0
                else:
                    mp[v][0] = mp[u][0] if not P[u] else mp[u][0]-mp[v][1]+mp[v][0]
                    mp[v][1] = mp[u][1] if not P[u] else mp[v][1]

                fn(v, u)
        fn(1, -1)
        return res//2