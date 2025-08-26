# not too hard 2200 rated, I get the intuition for this one after failing with the iterate through query attempt
# realizing that I must iterating through cell with Dijkstra and maintain the query at the sametime like a sliding window
# kind of thing: 11%
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(grid), len(grid[0])
        size = len(queries)
        arr = [(queries[i], i) for i in range(size)]
        arr.sort(key = lambda i:i[0])
        ans = [0]*size
        i = 0
        minheap = [(grid[0][0], 0, 0)]
        vis = set()
        vis.add((0, 0))
        cnt = 0
        while minheap:
            val, r, c = heapq.heappop(minheap)
            while i < size and arr[i][0] <= val:
                _, idx = arr[i]
                ans[idx] = cnt
                i += 1
            cnt += 1

            for R, C in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if R in range(n) and C in range(m) and (R, C) not in vis:
                    vis.add((R, C))
                    heapq.heappush(minheap, (max(grid[R][C], val), R, C))
        while i < size:
            _, idx = arr[i]
            ans[idx] = m*n
            i += 1
        return ans