# crazy low rating problem, you either know it or you don't: 86%
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        res = 0
        row, col = [0]*n, [0]*n
        cnt1, cnt2 = n, n
        for t, i, val in reversed(queries):
            if t == 1:
                if col[i]: continue
                col[i] = 1
                res += cnt1*val
                cnt2 -= 1
            else:
                if row[i]: continue
                row[i] = 1
                res += cnt2*val
                cnt1 -= 1
        return res