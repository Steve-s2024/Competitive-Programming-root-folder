# the optimal solution is 1-0 BFS. if you notice that the 'weight of edges' is either 0 or 1. I will not
# write the code though.

# it is actually solvable by Dijkstra, same core idea as one below: 8%
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        minheap = [(0, 0, 0)]
        vis = set()
        while minheap:
            cnt, r, c = heapq.heappop(minheap)
            if (r, c) in vis: continue
            vis.add((r, c))
            if r == row -1 and c == col-1: return cnt
            i = 1
            for R, C in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                if R in range(row) and C in range(col):
                    if i == grid[r][c]: heapq.heappush(minheap, (cnt, R, C))
                    else: heapq.heappush(minheap, (cnt+1, R, C))
                i += 1


# not easy to come done on this solution, it is not very orthodox bfs solution: 6%
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = deque([(0, 0)])
        cands = set()
        vis = set()
        vis.add((0, 0))
        cnt = 0
        while q:
            while q:
                r, c = q.popleft()
                if r == row-1 and c == col-1: return cnt

                if (r, c) in cands: cands.remove((r, c))
                i = 0
                for R, C in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                    if R in range(row) and C in range(col) and (R, C) not in vis:
                        if i+1 == grid[r][c]:
                            q.append((R, C))
                            vis.add((R, C))
                        cands.add((R, C))
                    i += 1
            # print(cands)
            q = deque(cands)
            cands.clear()
            cnt += 1
