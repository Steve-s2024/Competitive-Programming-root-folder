# my opinion this rating should be increased by 100, super-duper hard

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        n, m = len(board), len(board[0])

        abv = [[-inf] * m for _ in range(n)]
        abv[0] = board[0]
        for i in range(1, n):
            for j in range(m): abv[i][j] = max(abv[i - 1][j], board[i][j])

        blw = [[-inf] * m for _ in range(n)]
        blw[-1] = board[-1]
        for i in range(n - 2, -1, -1):
            for j in range(m): blw[i][j] = max(blw[i + 1][j], board[i][j])

        res = -inf
        for i in range(1, n - 1):
            for j in range(m):
                PRE = [-inf] * m
                SUF = [-inf] * m
                for k in range(m):
                    if k == j:
                        PRE[k] = PRE[k-1]
                        continue
                    PRE[k] = max(PRE[k - 1], abv[i-1][k])
                for k in range(m - 1, -1, -1):
                    if k == j:
                        SUF[k] = SUF[(k+1)%m]
                        continue
                    SUF[k] = max(SUF[(k+1)%m], abv[i-1][k])
                # print(PRE, SUF)
                for k in range(m):
                    if k == j: continue
                    l, r = PRE[k - 1] if k else -inf, SUF[k + 1] if k < m - 1 else -inf
                    # max(l, r) -> top rook
                    # suf[i+1][k] -> bottom rook
                    # board[i][j] -> middle rook
                    x = max(l, r) + blw[i + 1][k] + board[i][j]
                    res = max(res, x)
        return res