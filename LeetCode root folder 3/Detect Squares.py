# simulation and brute force with hashing: 81%
class DetectSquares:

    def __init__(self):
        self.rowMp = {}
        self.colMp = {}

    def add(self, point: List[int]) -> None:
        r, c = point
        rowMp = self.rowMp
        colMp = self.colMp
        if r not in rowMp:
            rowMp[r] = defaultdict(int)
        if c not in colMp:
            colMp[c] = defaultdict(int)
        rowMp[r][c] += 1
        colMp[c][r] += 1

    def count(self, point: List[int]) -> int:
        rowMp = self.rowMp
        colMp = self.colMp
        r, c = point
        if r not in rowMp or c not in colMp:
            return 0

        res = 0
        for C in rowMp[r]:
            for R in colMp[c]:
                a, b = abs(r - R), abs(c - C)
                if (
                        a == b and a != 0 and
                        R in rowMp and C in rowMp[R]
                ):
                    res += rowMp[R][C] * rowMp[r][C] * rowMp[R][c]

        return res