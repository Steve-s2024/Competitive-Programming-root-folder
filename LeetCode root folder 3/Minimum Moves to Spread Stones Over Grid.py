# brute force enumeration: 5%
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        mp = defaultdict(list)
        for rr in range(row):
            for cc in range(col):
                if grid[rr][cc] == 0:
                    q = deque([(rr, cc)])
                    vis = set()
                    vis.add((rr, cc))
                    cnt = 0
                    while q:
                        l = len(q)
                        while l:
                            r, c = q.popleft()
                            if grid[r][c] > 1:
                                mp[(rr, cc)].append((cnt, r, c))
                            for R, C in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                                if (
                                    R in range(row) and
                                    C in range(col) and
                                    (R, C) not in vis
                                ):
                                    vis.add((R, C))
                                    q.append((R, C))
                            l-=1
                        cnt+=1

        def recursive(tot):
            print(tot)
            if len(vis) == len(mp):
                return tot
            res = float('inf')
            for key, val in mp.items():
                if key in vis:
                    continue
                vis.add(key)
                for cost, r, c in val:
                    if grid[r][c] > 1:
                        grid[r][c] -= 1
                        a = recursive(tot+cost)
                        res = min(res, a)
                        grid[r][c] += 1
                vis.remove(key)
            return res
        vis = set()
        return recursive(0)