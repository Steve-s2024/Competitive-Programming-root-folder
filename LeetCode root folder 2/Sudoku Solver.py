# boring ass backtrack solution: 28%
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        rowMp, colMp, blockMp = [set() for i in range(9)], [set() for i in range(9)], [set() for i in range(9)]
        for r in range(row):
            for c in range(col):
                val = board[r][c]
                if val != '.':
                    rowMp[r].add(val)
                    colMp[c].add(val)
                    blockMp[(r // 3) * 3 + c // 3].add(val)

        # print(rowMp, colMp, blockMp)
        def recursive(r, c):
            nonlocal row, col
            if r == row:
                return True
            if board[r][c] == '.':
                for i in range(1, 10):
                    i = str(i)
                    if i not in rowMp[r] and i not in colMp[c] and i not in blockMp[(r // 3) * 3 + c // 3]:
                        rowMp[r].add(i)
                        colMp[c].add(i)
                        blockMp[(r // 3) * 3 + c // 3].add(i)

                        board[r][c] = i
                        R = r
                        C = c + 1
                        if C >= col:
                            R = r + 1
                            C = 0
                        if recursive(R, C):
                            return True
                        board[r][c] = '.'

                        rowMp[r].remove(i)
                        colMp[c].remove(i)
                        blockMp[(r // 3) * 3 + c // 3].remove(i)
            else:
                R = r
                C = c + 1
                if C >= col:
                    R = r + 1
                    C = 0
                if recursive(R, C):
                    return True

        recursive(0, 0)

