# these tree questions really require a lot of recursion 
# and black box thinking, and I kind of like it
# the solution is usually clean but not easy for linear
# brain, it must be sovled with recursive mindset: 31%
class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def dfs(i):
            total = 0
            minTotal = 0
            for j in graph[i]:
                if j not in visited:
                    visited.add(j)
                    res = dfs(j)
                    total += res[0]
                    minTotal += res[1]
            # print(i, total + values[i], minTotal)
            return (total + values[i], min(values[i], minTotal if minTotal > 0 else values[i]))

        visited.add(0)
        res = dfs(0)
        return res[0] - res[1] 