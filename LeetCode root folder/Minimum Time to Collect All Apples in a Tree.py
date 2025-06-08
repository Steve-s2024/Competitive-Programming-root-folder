# dfs solution, kinda tricky question:29%
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def dfs(i):
            res = 0
            for j in graph[i]:
                if j not in visited:
                    visited.add(j)
                    res += max(dfs(j), 0)
            # print(i, res)
            if res > 0:
                return res + 1
            if res == 0 and hasApple[i]:
                return 1
            return 0
        visited.add(0)
        res = dfs(0)
        if res > 0:
            return (res-1)*2
        return 0 