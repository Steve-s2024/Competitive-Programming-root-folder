# Dyjikstra's algorithm with modification, the hard part of 
# Dyjikstra is not to understand the standard implementation
# but instead understanding the nature of it and be able
# to modify it to achieve more like I did here...: 37%
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        minHeap = [(0, 0, 0)]
        heapq.heapify(minHeap)
        visited = set()
        res = 0
        while minHeap:
            [i, r, c] = heapq.heappop(minHeap)
            visited.add((r, c))
            res = max(res, i)
            if r == row-1 and c == col-1:
                return res
            for R, C in [(r+1, c),(r-1, c),(r, c+1),(r, c-1)]:
                if (
                    R in range(row) and
                    C in range(col) and
                    (R, C) not in visited
                ):
                    a, b = heights[r][c], heights[R][C]
                    heapq.heappush(minHeap, (abs(a-b), R, C))
            

# dfs and dp solution, failed
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        dp = {}
        dp[(row-1, col-1)] = 0
        visited = set()
        visited.add((0, 0))
        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]

            res = float('inf')
            for R, C in [(r+1, c),(r-1, c),(r, c+1),(r, c-1)]:
                if (
                    R in range(row) and
                    C in range(col) and
                    (R, C) not in visited
                ):
                    visited.add((R, C))
                    res = min(res, max(dfs(R, C), abs(heights[r][c] - heights[R][C])))
                    visited.remove((R, C))
            dp[(r, c)] = res
            return res

        dfs(0, 0)
        tmp = [[0]*col for i in range(row)]
        for key, val in dp.items():
            [r, c] = key
            tmp[r][c] = val
        for row in tmp:
            print(row)
        return dp[(0, 0)]
