# 卧槽早上起来直接干四题 不到三十分钟 （估计会是有史以来最高分） 2025/10/25
# Q4
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        mp = [0]*151
        mod = 10**9 + 7
        for j in range(m): mp[mat[-1][j]] += 1
        for i in range(n-2, -1,  -1):
            tmp = [0]*151
            for j in range(m):
                for key, val in enumerate(mp):
                    if key == 0: continue
                    d = gcd(mat[i][j], key)
                    tmp[d] += val
                    tmp[d] %= mod
            mp = tmp
        return mp[1] % mod
