# optimized based on brute force: 77%
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mp1, mp2 = defaultdict(int), defaultdict(int)
        for r in range(n):
            for c in range(n):
                cur = grid[r][c]
                if (
                        (r <= n // 2 and (r == c or r == n - 1 - c)) or
                        (r > n // 2 and c == n // 2)
                ):
                    mp1[cur] += 1
                else:
                    mp2[cur] += 1

        res = n * n
        for i in range(3):
            for j in range(3):
                if j != i:
                    # i for constructing Y
                    # j for non Y cells
                    # total1 --> the total amount of cell that belongs to Y
                    # total2 --> the cell that doesn't belong to the Y
                    total1 = 2 * n - (n + 1) / 2
                    total2 = n * n - total1

                    fixCnt = 0
                    fixCnt += total1 - mp1[i]
                    fixCnt += total2 - mp2[j]
                    res = min(res, fixCnt)

        return int(res)


# brute force: 18%
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def countFix(n1, n2):
            res = 0
            for r in range(n):
                for c in range(n):
                    if (
                        (r <= n // 2 and (r == c or r == n - 1 - c)) or
                        (r > n // 2 and c == n // 2)
                    ):
                        if grid[r][c] != n1:
                            res += 1
                    elif grid[r][c] != n2:
                        res += 1
            return res

        minOp = n * n
        for i in range(0, 3):
            for j in range(0, 3):
                if j == i:
                    continue
                minOp = min(minOp, countFix(i, j))
        return minOp