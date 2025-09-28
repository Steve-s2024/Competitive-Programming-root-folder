#  这样也超时， 正常的n^2 complexity， 开可恶了

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10 ** 9 + 7

        m = r - l + 1
        arr = [[1, 1] for _ in range(m)]
        for i in range(n-1):
            tmp = [[0, 0] for _ in range(m)]
            lw = 0
            hi = sum(e[0] for e in arr) % mod
            for j in range(m):
                tmp[j][0] += lw
                tmp[j][0] %= mod
                lw += arr[j][1]
                lw %= mod
                hi -= arr[j][0]
                tmp[j][1] += hi
                tmp[j][1] %= mod
            arr = tmp

        res = sum(e[0] for e in arr) - arr[-1][1] + sum(e[1] for e in arr) - arr[0][0]
        return res % mod
