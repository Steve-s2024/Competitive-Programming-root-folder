# before submitting, I thought this could be either MLE or TLE, did not expect to pass at all...: 19%
# but apparently there's a better solution
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def recursive(i, mx, k):
            if i >= n: return 1 if k == 0 else 0
            res = 0
            for j in range(1, m + 1):
                if j > mx:
                    res += recursive(i + 1, j, k - 1)
                else:
                    res += recursive(i + 1, mx, k)
                res %= MOD
            return res

        return recursive(0, 0, k)


