# dfs solution: 174
# ms
# Beats
# 81.32%
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        h1, h2 = defaultdict(list), defaultdict(list)
        for src, dst in connections:
            h1[src].append(dst)
            h2[dst].append(src)

        visited = set()
        res = 0

        def dfs(cur):
            nonlocal res
            for dst in h1[cur]:
                if dst not in visited:
                    res += 1
                    visited.add(dst)
                    dfs(dst)
            for src in h2[cur]:
                if src not in visited:
                    visited.add(src)
                    dfs(src)

        visited.add(0)
        dfs(0)
        return res
