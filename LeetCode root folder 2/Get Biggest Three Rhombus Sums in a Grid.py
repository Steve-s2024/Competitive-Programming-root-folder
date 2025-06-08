# brute force calculating the rhombus sums: 30%
# boring problem
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        def getTotal(R, C, n):
            rMid, cMid = (R + R + n - 1) // 2, (C + C + n - 1) // 2
            # print(rMid, cMid)
            total = 0
            for r in range(R, R + n):
                if r <= rMid:
                    tmp = r - R
                    total += grid[r][cMid - tmp] + grid[r][cMid + tmp]
                else:
                    tmp = R+n-1 - r
                    total += grid[r][cMid - tmp] + grid[r][cMid + tmp]
            if n == 1:
                total -= grid[R][cMid]
            else:
                total -= grid[R][cMid] + grid[R + n - 1][cMid]
            return total
        row, col = len(grid), len(grid[0])

        hashSet = set()
        for r in range(row):
            for c in range(col):
                for i in range(1, min(row-r, col-c)+1, 2):
                    total = getTotal(r, c, i)
                    # print(r, c, i, total)
                    hashSet.add(total)
        totals = list(hashSet)
        totals.sort(reverse = True)
        return totals[:3]