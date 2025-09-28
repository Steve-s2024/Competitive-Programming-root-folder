# converting to bottom up DP is actually nightmarish😭😨😰
# glad made it on time
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7

        dp = [[1] * 3 for _ in range(3)]
        for i in range(n - 1, -1, -1):
            tmp = [[0] * 3 for _ in range(3)]
            for pf in range(3):
                for cf in range(3):
                    tmp[pf][cf] += dp[pf][cf]
                    if nums[i] % 2 == pf and cf < 2:
                        tmp[pf][cf] += dp[pf][cf + 1]
                    elif nums[i] % 2 != pf:
                        tmp[pf][cf] += dp[nums[i] % 2][1]
                    tmp[pf][cf] %= MOD
            dp = tmp
        return dp[2][0] - 1

        # @cache
        # def recursive(i, pf, cf):
        #     if i >= n: return 1
        #     res = recursive(i+1, pf, cf)
        #     if nums[i] % 2 == pf and cf < 2: res += recursive(i+1, pf, cf+1)
        #     elif nums[i] % 2 != pf: res += recursive(i+1, nums[i]%2, 1)
        #     return res%MOD
        # return recursive(0, -1, 0)-1