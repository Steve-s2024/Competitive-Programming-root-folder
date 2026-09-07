# idea and implementation wise one of the hardest problem in my competitive journey

class Solution:
    def minimumSum(self, g: List[List[int]]) -> int:
        n, m = len(g), len(g[0])
        dp = [[[-1, -1, -1, -1] for _ in range (n*m)] for _ in range(n*m)]
        for i in range(n):
            for j in range(m):
                for I in range(i, n):
                    for J in range(j, m):
                        a, b = i*m+j, I*m+J
                        ar = [-1]*4
                        if I: ar = dp[a][(I-1)*m+J][:]

                        if J:
                            br = dp[a][I*m+J-1]
                            if ar[0] == -1: ar = br[:]
                            elif br[0] != -1:
                                ar[0] = min(ar[0], br[0])
                                ar[1] = max(ar[1], br[1])
                                ar[2] = min(ar[2], br[2])
                                ar[3] = max(ar[3], br[3])

                        if g[I][J]:
                            if ar[0] == -1: ar = [I, I, J, J]
                            else:
                                ar[0] = min(ar[0], I)
                                ar[1] = max(ar[1], I)
                                ar[2] = min(ar[2], J)
                                ar[3] = max(ar[3], J)

                        dp[a][b] = ar[:]

        for r in dp:
            for i in range(len(r)):
                a, b, c, d = r[i]
                if a != -1: r[i] = (b-a+1)*(d-c+1)
                else: r[i] = 0
        # print(dp)


        @cache
        def fn(a, b, c, d, i):
            if i == 2: return dp[a*m+c][b*m+d]
            res = 1<<31
            for j in range(a, b):
                s = fn(a, j, c, d, i+1)
                t = fn(j+1, b, c, d, i+1)
                s += dp[(j+1)*m+c][b*m+d]
                t += dp[a*m+c][j*m+d]
                res = min(res, s, t)
            for j in range(c, d):
                s = fn(a, b, c, j, i+1)
                t = fn(a, b, j+1, d, i+1)
                s += dp[a*m+j+1][b*m+d]
                t += dp[a*m+c][b*m+j]
                res = min(res, s, t)

            return res
        return fn(0, n-1, 0, m-1, 0)

