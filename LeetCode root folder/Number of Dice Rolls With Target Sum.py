# standard 2D dynamic programming solution:351
# ms
# Beats
# 39.10%
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        def recursive(nCount, tar):
            nonlocal k
            if nCount == 0 and tar == 0:
                return 1
            if nCount <= 0 or tar < 0:
                return 0
            if (nCount, tar) in dp:
                return dp[(nCount, tar)]
            total = 0
            for i in range(1, k+1):
                total += recursive(nCount-1, tar-i)
            dp[(nCount, tar)] = total
            return total
        return recursive(n, target) % (pow(10, 9) + 7)
