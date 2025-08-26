#
class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda i: i[2])
        size = len(edges)

        def dfs(node):
            for nxt in graph[node]:
                if nxt in vis: continue
                vis.add(nxt)
                dfs(nxt)

        graph = defaultdict(list)
        for i in range(size):
            u, v, _ = edges[i]
            graph[u].append(v)
            graph[v].append(u)
        cnt = 0
        vis = set()
        for i in range(n):
            if i not in vis:
                cnt += 1
                dfs(i)
        if cnt >= k:
            return 0

        # binary search
        res = 0
        l, r = 0, size - 1
        while l <= r:
            m = (l + r) // 2
            i = 0
            graph = defaultdict(list)
            for i in range(m + 1, size):
                u, v, _ = edges[i]
                graph[u].append(v)
                graph[v].append(u)
            cnt = 0
            vis = set()
            for i in range(n):
                if i not in vis:
                    cnt += 1
                    dfs(i)
            if cnt >= k:
                res = edges[m][2]
                r = m - 1
            else:
                l = m + 1
        return res
