# simulation solution:0
# ms
# Beats
# 100.00%

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        row, col = len(board), len(board[0])

        def checkByStep(rStep, cStep, r, c, side):
            count = 0
            if (
                    r + rStep not in range(row) or
                    c + cStep not in range(col) or
                    board[r + rStep][c + cStep] in [side, '.']
            ):
                return False
            r += 2 * rStep
            c += 2 * cStep
            while r in range(row) and c in range(col):
                if board[r][c] == '.':
                    return False
                if board[r][c] == side:
                    return True
                r += rStep
                c += cStep
            return False

        steps = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        for rStep, cStep in steps:
            res = checkByStep(rStep, cStep, rMove, cMove, color)
            # print(rStep, cStep, res)
            if res:
                return res
        return False