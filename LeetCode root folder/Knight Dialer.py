# classic type of dp question: 44%
class Solution:
    def __init__(self):
        
        self.ref = defaultdict(list)
        tmp = []
        for r in range(3):
            for c in range(3):
                tmp.append((r, c))
        tmp.append((3, 1))

        for r, c in tmp:
            for rIncre in [-2, -1, 1, 2]:
                for cIncre in [-2, -1, 1, 2]:
                    if abs(rIncre) == abs(cIncre):
                        continue
                    a, b = r+rIncre, c+cIncre
                    if (
                        (a in range(3) and b in range(3)) or
                        (a == 3 and b == 1)
                    ):
                        self.ref[(r, c)].append((a, b))
        # print(self.ref)

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        matrix = [[1]*3 for i in range(4)]
        for i in range(n-1):
            tmp = [[0]*3 for i in range(4)]
            for r in range(3):
                for c in range(3):
                    for R, C in self.ref[(r, c)]:
                        tmp[r][c] += matrix[R][C]
            for R, C in self.ref[(3, 1)]:
                tmp[3][1] += matrix[R][C]
            matrix = tmp
        # print(matrix)
        res = 0
        for r, c in self.ref:
            res += matrix[r][c]
        return res % 1000000007