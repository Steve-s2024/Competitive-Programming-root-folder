# Bellman Ford solution, very inefficient: 5%
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        arr = [[inf]*2 for _ in range(n)]
        tmp = [[inf]*2 for _ in range(n)]
        arr[0] = [0, 0]
        tmp[0] = [0, 0]
        for i in range(n):
            for u, v in redEdges:
                tmp[v][0] = min(tmp[v][0], arr[u][1]+1)
            for u, v in blueEdges:
                tmp[v][1] = min(tmp[v][1], arr[u][0]+1)
            arr = tmp[:]
        res = []
        for r, b in arr:
            mi = min(r, b)
            res.append(-1 if mi == inf else mi)
        return res