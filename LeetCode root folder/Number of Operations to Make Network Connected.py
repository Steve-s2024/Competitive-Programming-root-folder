# dfs solution:40
# ms
# Beats
# 69.47%
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)+1 < n:
            return -1
        graph = defaultdict(list)
        for n1, n2 in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = set()
        def dfs(cur):
            visited.add(cur)
            for next_ in graph[cur]:
                if next_ not in visited:
                    dfs(next_)
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res - 1