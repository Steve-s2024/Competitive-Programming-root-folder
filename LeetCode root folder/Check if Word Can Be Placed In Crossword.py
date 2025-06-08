# interesting brute force, not that brutal brute force: 26%
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        def checkValid(R, C, r, c, board, s):
            nonlocal row, col
            for i in range(len(s)):
                if (
                    r not in range(row) or 
                    c not in range(col) or
                    board[r][c] not in [' ', s[i]]
                ):
                    return False
                r += R
                c += C
            return (
                r not in range(row) or 
                c not in range(col) or
                board[r][c] == '#'
            )

        coors = [(-1, 0),(0, -1),(1, 0),(0, 1)]
        for r in range(row):
            for c in range(col):
                for R, C in coors:
                    # check each directions
                    if (
                        r-R not in range(row) or 
                        c-C not in range(col) or
                        board[r-R][c-C] == '#'
                    ):
                        if checkValid(R, C, r, c, board, word):
                            return True
        return False
