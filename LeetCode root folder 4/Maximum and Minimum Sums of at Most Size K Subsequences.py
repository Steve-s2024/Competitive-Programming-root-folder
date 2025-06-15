# precompute with pascal's formula: TLE
class Solution:
    def __init__(self):
        MOD = 10 ** 9 + 7
        n, k = 10 ** 5, 70
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1
            for j in range(1, min(i, k) + 1):
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD
                dp[i][j] %= MOD
        self.comb = dp

    def minMaxSums(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        res = 0

        for size in range(1, k + 1):
            for i in range(n):
                x = nums[i]
                cnt = self.comb[n - i - 1][size - 1]
                res += x * cnt
                res %= MOD

            for i in range(n - 1, -1, -1):
                x = nums[i]
                cnt = self.comb[i][size - 1]
                res += x * cnt
                res %= MOD
        return res


# pascal's formula solution: MLE
class Solution:
    # n pick m
    @staticmethod
    @cache
    def getComb(n, m, MOD = 10**9 + 7):
        if n < m: return 0
        if n == m or m == 0: return 1
        if m == 1: return n
        res = 0
        res += Solution.getComb(n-1, m)
        res += Solution.getComb(n-1, m-1)
        res %= MOD
        return res



    def minMaxSums(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        MOD = 10**9 + 7
        for size in range(1, k+1):
            for i in range(n):
                x = nums[i]
                cnt = Solution.getComb(n - i - 1, size - 1)
                res += x * cnt
                res %= MOD

            for i in range(n - 1, -1, -1):
                x = nums[i]
                cnt = Solution.getComb(i, size - 1)
                res += x * cnt
                res %= MOD

        return res

