# Tarjan algorithm solution: 80%
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
        vis = [0] * n
        arr = [0] * n
        low = [0] * n
        cnt = 0

        def dfs(u, p):
            nonlocal cnt
            vis[u] = 1
            arr[u] = cnt
            low[u] = arr[u]
            cnt += 1
            for v in g[u]:
                if v == p: continue
                if vis[v]:
                    low[u] = min(low[u], arr[v])
                    continue

                a = dfs(v, u)
                low[u] = min(low[u], a)
            return low[u]

        dfs(0, -1)

        # print(low)
        ans = []
        for u, v in connections:
            if low[u] > arr[v] or low[v] > arr[u]: ans.append((u, v))
        return ans