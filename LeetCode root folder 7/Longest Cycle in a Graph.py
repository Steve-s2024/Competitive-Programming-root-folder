# uni-cyclic tree, maybe not the simplest solution: 84%
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        deg = [0] * n
        for v in edges:
            if v != -1: deg[v] += 1
        q = deque()
        for i in range(n):
            if deg[i] == 0: q.append(i)

        while q:
            a = q.popleft()
            b = edges[a]
            if b == -1: continue
            deg[b] -= 1
            if deg[b] == 0: q.append(b)

        res = 0
        vis = [0]*n
        for i in range(n):
            if not deg[i] or vis[i]: continue
            x = i
            cnt = 0
            while not vis[x]:
                vis[x] = 1
                x = edges[x]
                cnt += 1
            res = max(res, cnt)
        return res if res else -1
