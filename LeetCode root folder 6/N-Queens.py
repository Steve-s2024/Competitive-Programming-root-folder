# don't know how i could make this better: 5%

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        vis = []

        def backtrack(r, c, re):
            nonlocal n
            if re == 0:
                board = []
                for i in range(n): board.append(list('.' * n))
                for rQ, cQ in vis: board[rQ][cQ] = 'Q'
                res.append([''.join(row) for row in board])
                return
            if r >= n: return
            # print(r, c)
            backtrack(r + (c+1) // n, (c + 1) % n, re)
            flag = True
            for rQ, cQ in vis:
                if (
                    rQ == r or cQ == c or
                    abs(rQ - r) == abs(cQ - c)
                ):
                    flag = False
                    break
            if flag:
                vis.append((r, c))
                backtrack(r + 1, 0, re - 1)
                vis.pop()

        backtrack(0, 0, n)
        return res