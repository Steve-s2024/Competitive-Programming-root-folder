# nice solution, but looks like not the intended one, the hint give the same approach but with better state definition: 5%
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        dp = [[[-1] * (k + 1) for _ in range(n + 1)] for _ in range(n + 1)]

        def recursive(i, s, k):
            nonlocal n, MOD
            if dp[i][s][k] != -1: return dp[i][s][k]
            if k == 0: return 1 if s == 0 else 0
            if i >= n: return 0
            res = recursive(i + 1, s, k)
            if k - nums[i] >= 0:
                res += recursive(i + 1, s - 1, k - nums[i])
            res %= MOD
            dp[i][s][k] = res
            return res

        res = 0
        for i in range(1, n + 1):
            res += recursive(0, i, k) * pow(2, n - i, MOD)
            res %= MOD
        return res