# I didn't cover the case where there's only one column or only one row in the previous
# solution: 31%

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row, col = len(grid), len(grid[0])
        matSm = 0
        suffix = defaultdict(int)
        for r in range(row):
            for c in range(col):
                matSm += grid[r][c]
                suffix[grid[r][c]] += 1
        total = 0
        prefix = set()
        for c in range(col):
            total += grid[0][c]
            prefix.add(grid[0][c])
            suffix[grid[0][c]] -= 1

        for r in range(1, row):
            a, b = total, matSm - total
            if (
                    a - b == 0 or
                    a - b in prefix and ((r != 1 and col != 1) or a - b in [grid[0][0], grid[0][-1], grid[r][0]]) or
                    b - a in suffix and (
                    (r != row - 1 and col != 1) or b - a in [grid[-1][0], grid[-1][-1], grid[r][0]]) and suffix[
                b - a] != 0
            ):
                return True
            for c in range(col):
                total += grid[r][c]
                prefix.add(grid[r][c])
                suffix[grid[r][c]] -= 1

        suffix = defaultdict(int)
        for r in range(row):
            for c in range(col):
                suffix[grid[r][c]] += 1

        prefix = set()
        total = 0
        for r in range(row):
            prefix.add(grid[r][0])
            total += grid[r][0]
            suffix[grid[r][0]] -= 1

        for c in range(1, col):
            a, b = total, matSm - total
            if (
                    a - b == 0 or
                    a - b in prefix and ((c != 1 and col != 1) or a - b in [grid[0][0], grid[-1][0], grid[0][c - 1]]) or
                    b - a in suffix and (
                    (c != col - 1 and col != 1) or b - a in [grid[0][-1], grid[-1][-1], grid[0][c]]) and suffix[
                b - a] != 0
            ):
                return True

            for r in range(row):
                total += grid[r][c]
                prefix.add(grid[r][c])
                suffix[grid[r][c]] -= 1

        return False



# simulation solution: WA on the second last tc
# come on!!
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row, col = len(grid), len(grid[0])
        matSm = 0
        suffix = defaultdict(int)
        for arr in grid:
            for e in arr:
                matSm += e
                suffix[e] += 1

        prefix = set()
        total = 0
        for c in range(col):
            total += grid[0][c]
            prefix.add(grid[0][c])
            suffix[grid[0][c]] -= 1

        for r in range(1, row):
            diff = total - (matSm - total)
            if (
                    diff == 0 or
                    diff in prefix and (
                    r != 1 or diff in [grid[0][0], grid[0][-1]]
            ) or
                    -diff in suffix and (
                    r != row - 1 or -diff in [grid[r][0], grid[r][-1]]
            ) and suffix[-diff] != 0
            ):
                return True
            for c in range(col):
                total += grid[r][c]
                prefix.add(grid[r][c])
                suffix[grid[r][c]] -= 1

        suffix = defaultdict(int)
        for arr in grid:
            for e in arr:
                suffix[e] += 1

        prefix = set()
        total = 0
        for r in range(row):
            total += grid[r][0]
            prefix.add(grid[r][0])
            suffix[grid[r][0]] -= 1

        for c in range(1, col):
            diff = total - (matSm - total)
            if (
                    diff == 0 or
                    diff in prefix and (
                    c != 1 or diff in [grid[0][0], grid[-1][0]]
            ) or
                    -diff in suffix and (
                    c != col - 1 or -diff in [grid[0][c], grid[-1][c]]
            ) and suffix[-diff] != 0
            ):
                return True
            for r in range(row):
                total += grid[r][c]
                prefix.add(grid[r][c])
                suffix[grid[r][c]] -= 1

        return False


# second try, rebuild: WA on 681/682
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row, col = len(grid), len(grid[0])
        matSm = 0
        suffix = defaultdict(int)
        for r in range(row):
            for c in range(col):
                matSm += grid[r][c]
                suffix[grid[r][c]] += 1
        total = 0
        prefix = set()
        for c in range(col):
            total += grid[0][c]
            prefix.add(grid[0][c])
            suffix[grid[0][c]] -= 1

        for r in range(1, row):
            a, b = total, matSm - total
            if (
                    a - b == 0 or
                    a - b in prefix and (r != 1 or a - b in [grid[0][0], grid[0][-1]]) or
                    b - a in suffix and (r != row - 1 or b - a in [grid[-1][0], grid[-1][-1]]) and suffix[b - a] != 0
            ):
                return True
            for c in range(col):
                total += grid[r][c]
                prefix.add(grid[r][c])
                suffix[grid[r][c]] -= 1

        suffix = defaultdict(int)
        for r in range(row):
            for c in range(col):
                suffix[grid[r][c]] += 1

        prefix = set()
        total = 0
        for r in range(row):
            prefix.add(grid[r][0])
            total += grid[r][0]
            suffix[grid[r][0]] -= 1

        for c in range(1, col):
            a, b = total, matSm - total
            if (
                    a - b == 0 or
                    a - b in prefix and (c != 1 or a - b in [grid[0][0], grid[-1][0]]) or
                    b - a in suffix and (c != col - 1 or b - a in [grid[0][-1], grid[-1][-1]]) and suffix[b - a] != 0
            ):
                return True

            for r in range(row):
                total += grid[r][c]
                prefix.add(grid[r][c])
                suffix[grid[r][c]] -= 1

        return False