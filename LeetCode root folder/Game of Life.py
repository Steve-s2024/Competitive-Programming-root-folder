class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        ROW, COL = len(board), len(board[0])
        copy = [[cell for cell in row] for row in board]
        def countNeighbor(r, c):
            total = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if (
                        i not in range(ROW) or
                        j not in range(COL)
                    ):
                        continue
                    total += copy[i][j]
            return total - copy[r][c]

        for r in range(ROW):
            for c in range(COL):
                total = countNeighbor(r, c)
                if total < 2:
                    board[r][c] = 0
                elif total == 3:
                    board[r][c] = 1
                elif total > 3:
                    board[r][c] = 0