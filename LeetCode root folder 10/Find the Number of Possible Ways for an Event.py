# man! just two more testcases...
# i really don't know how to make it better

class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        mod = 10**9 + 7

        mx = x
        mp = [[0]*mx for _ in range(mx)]
        for i in range(mx):
            f = 1
            for j in range(i+1):
                f *= (i-j+1) * pow(j+1, mod-2, mod)
                f %= mod
                mp[i][j] = f

        # print(mp)
        res = 0
        ar = []
        for i in range(1, min(x, n)+1):
            way = pow(i, n, mod)
            for j, v in enumerate(ar): way -= mp[i-1][j] * v
            # print(i, way)
            res += way*mp[x-1][i-1]*pow(y, i, mod)
            res %= mod
            ar.append(way)
        return res