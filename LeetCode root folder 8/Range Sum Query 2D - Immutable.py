# efficient use of 2D prefix sum: 67%
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        mat = matrix
        for i in range(n):
            for j in range(1, m): mat[i][j] += mat[i][j - 1]

        for j in range(m):
            for i in range(1, n): mat[i][j] += mat[i - 1][j]

        self.mat = mat

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        mat = self.mat
        a = mat[row2][col2]
        b = mat[row1 - 1][col2] if row1 else 0
        c = mat[row2][col1 - 1] if col1 else 0
        d = mat[row1 - 1][col1 - 1] if row1 * col1 else 0
        return a - b - c + d
