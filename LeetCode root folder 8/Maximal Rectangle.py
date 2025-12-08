# once viewed unsolvable, now it seems just a variation of a recent medium POTD (almost exactly the same solution O(n^3))
class Solution:
    def maximalRectangle(self, g: List[List[str]]) -> int:
        n, m = len(g), len(g[0])

        res = 0
        prev = [0]*m
        for i in range(n - 1, -1, -1):
            tmp = [0] * m
            for j in range(m - 1, -1, -1):
                tmp[j] = 0 if g[i][j] == '0' else (1 + prev[j])
                x = inf
                for k in range(j, m):
                    x = min(x, tmp[k])
                    res = max(res, x * (k - j + 1))
            prev = tmp
            # print(tmp)

        return res



# O(n^2) solution
class Solution:
    def maximalRectangle(self, g: List[List[str]]) -> int:
        n, m = len(g), len(g[0])

        arr = [0] * m
        res = 0
        for i in range(n):
            for j in range(m): arr[j] = 0 if g[i][j] == '0' else (1 + arr[j])
            ri = [0] * m
            stk = []
            for j in range(m):
                while stk and stk[-1][0] > arr[j]: ri[stk.pop()[1]] = j
                stk.append((arr[j], j))
            while stk: ri[stk.pop()[1]] = m
            le = [0] * m
            stk = []
            for j in range(m - 1, -1, -1):
                while stk and stk[-1][0] > arr[j]: le[stk.pop()[1]] = j
                stk.append((arr[j], j))
            while stk: le[stk.pop()[1]] = -1

            # print(arr)
            for j in range(m):
                l, r = le[j], ri[j]
                # print(j, l, r)
                res = max((r - l - 1) * arr[j], res)
        return res
