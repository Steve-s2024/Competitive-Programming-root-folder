# optimized solution: 8%
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for r, c in walls:
            grid[r][c] = 1

        for r, c in guards:
            grid[r][c] = 1

        for r, c, in guards:
            for rStep, cStep in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                R, C = r, c
                while True:
                    if (R, C) == (r, c):
                        R += rStep
                        C += cStep
                        continue
                    if (
                            R not in range(m) or
                            C not in range(n) or
                            (grid[R][C] == 1)
                    ):
                        break
                    grid[R][C] = 2
                    R += rStep
                    C += cStep

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    res += 1
        return res

# hash map and set solution: 5%
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for r, c in walls:
            grid[r][c] = 1

        mp = defaultdict(set)
        for r, c, in guards:
            for rStep, cStep in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                R, C = r, c
                while True:
                    if (
                            R not in range(m) or
                            C not in range(n) or
                            grid[R][C] == 1 or
                            (R, C) in mp and (rStep, cStep) in mp[(R, C)]
                    ):
                        break
                    mp[(R, C)].add((rStep, cStep))
                    grid[R][C] = 2
                    R += rStep
                    C += cStep

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    res += 1
        return res