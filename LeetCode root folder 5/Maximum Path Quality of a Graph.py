# DFS solution: 55%
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        res = 0
        vis = defaultdict(int)

        def dfs(node, sm, t):
            nonlocal res, maxTime
            if node == 0: res = max(res, sm)
            vis[node] += 1
            for nxt, w in graph[node]:
                if t + w <= maxTime:
                    dfs(nxt, sm + (values[nxt] if vis[nxt] == 0 else 0), t + w)
            vis[node] -= 1

        vis[0] += 1
        dfs(0, values[0], 0)
        return res

# BFS don't work, use DFS instead
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        res = 0
        q = deque()
        q.append((0, values[0], 0))
        while q:
            node, sm, t = q.popleft()
            if node == 0: res = max(res, sm)
            for nxt, w in graph[node]:
                if t + w <= maxTime:
                    q.append((nxt, sm + values[nxt], t + w))

        return res