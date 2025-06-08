class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.matrix = [[0] * col for r in range(row)]
        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                sum_ = matrix[r][c]
                if c < col-1:
                    sum_ += self.matrix[r][c+1]
                if r < row-1:
                    sum_ += self.matrix[r+1][c]
                if c < col-1 and r < row-1:
                    sum_ -= self.matrix[r+1][c+1]
                self.matrix[r][c] = sum_
        # print(self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = self.matrix[row1][col1]
        if row2+1 < len(self.matrix):
            sum_ -= self.matrix[row2+1][col1]
        if col2+1 < len(self.matrix[0]):
            sum_ -= self.matrix[row1][col2+1]
        if row2+1 < len(self.matrix) and col2+1 < len(self.matrix[0]):
            sum_ += self.matrix[row2+1][col2+1]
        return sum_