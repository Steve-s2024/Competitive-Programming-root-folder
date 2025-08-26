# fking hard contest, how the fk everyone is suddenly so smart able to solve this before me trying 100%?
class Solution:

    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if k == n: return 0

        def dfs(node):
            for nxt in graph[node]:
                if nxt in vis: continue
                vis.add(nxt)
                dfs(nxt)

        edges.sort(key=lambda i: i[2])
        size = len(edges)
        res = -1
        l, r = 0, size - 1
        while l <= r:
            m = (l + r) // 2
            graph = defaultdict(list)
            for i in range(m + 1):
                u, v, w = edges[i]
                graph[u].append(v)
                graph[v].append(u)

            cnt = 0
            vis = set()
            for i in range(n):
                if i not in vis:
                    vis.add(i)
                    dfs(i)
                    cnt += 1
            # print(m, cnt)
            if cnt <= k:
                res = edges[m][2]
                r = m - 1
            else:
                l = m + 1
        return res

