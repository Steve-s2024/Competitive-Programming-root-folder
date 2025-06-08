# haha, exact same as the skibidi table from codeforces contest,
# maybe a bit easier
class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        n = pow(2, N)
        matrix = [[0] * n for i in range(n)]
        cnt = 0

        def recursive(l, r, t, b):
            nonlocal cnt
            if l == r and t == b:
                matrix[t][l] = cnt
                cnt += 1
                return

            horMid = (l + r) // 2
            verMid = (t + b) // 2

            for L, R, T, B in [
                (horMid + 1, r, t, verMid),
                (horMid + 1, r, verMid + 1, b),
                (l, horMid, verMid + 1, b),
                (l, horMid, t, verMid)
            ]:
                recursive(L, R, T, B)

        recursive(0, n - 1, 0, n - 1)
        # print(matrix)
        return matrix