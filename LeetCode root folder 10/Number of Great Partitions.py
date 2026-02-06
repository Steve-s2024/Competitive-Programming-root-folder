# ehh... okay there is a simpler complementary relationship. (by the hint)
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        sm = sum(nums)
        if 2*k > sm: return 0
        res = pow(2, n, mod)

        @cache
        def dp(i, x):
            nonlocal n
            if i >= n: return 1 if x < k else 0
            return (dp(i+1, x) + dp(i+1, min(k, x+nums[i])))%mod
        res = res+mod - 2*dp(0, 0)
        return res%mod


# I am just a freaking genius, how can someone just know this complementary relationship without talent?
# need to remove the @cache for fn() to avoid MLE
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        sm = sum(nums)
        if 2*k > sm: return 0
        mp = [[-1]*(k+1) for i in range(n)]
        def fn(i, x):
            nonlocal n
            if i >= n: return 1 if x >= k else 0
            if mp[i][x] != -1: return mp[i][x]
            mp[i][x] = (fn(i+1, x) + fn(i+1, min(k, x+nums[i])))%mod
            return mp[i][x]
        res = fn(0, 0)

        @cache
        def dp(i, x):
            nonlocal n
            if i >= n: return 1 if x < k else 0
            return (dp(i+1, x) + dp(i+1, min(k, x+nums[i])))%mod
        res = res+mod - dp(0, 0)
        return res%mod