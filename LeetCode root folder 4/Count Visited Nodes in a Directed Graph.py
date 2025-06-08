# : 16%
class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        mp = defaultdict(int)
        for u in edges: mp[u] += 1
        n = len(edges)
        q = deque(u for u in range(n) if mp[u] == 0)

        while q:
            for _ in range(len(q)):
                u = q.popleft()
                v = edges[u]
                mp[v] -= 1
                if mp[v] == 0:
                    q.append(v)

        cnt = defaultdict(int)
        vis = set()

        for u in range(n):
            if mp[u] != 0:
                if u in vis:
                    continue

                cycle = []
                t = u
                while t not in vis:
                    cycle.append(t)
                    vis.add(t)
                    t = edges[t]

                for t in cycle: cnt[t] = len(cycle)

        @cache
        def dfs(u):
            if u in cnt: return cnt[u]
            return dfs(edges[u]) + 1

        return [dfs(i) for i in range(n)]