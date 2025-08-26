# no other way, even this simple DP, my last resort, failed
class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        inf = math.inf
        n = len(nums)
        dp = nums[:]

        for i in range(n - 1, -1, -1):
            xor = 0
            for j in range(i, n):
                xor ^= nums[j]
                dp[i] = min(dp[i], max(xor, dp[j + 1] if j < n - 1 else 0))
        return dp[0]

# TLE
class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        inf = math.inf
        n = len(nums)
        arr = [[-1]*k for _ in range(n)]
        def recursive(i, k):
            nonlocal inf, n
            if k < 0: return inf
            if i >= n: return 0 if k == 0 else inf
            if arr[i][k-1] != -1: return arr[i][k-1]
            res = inf
            xor = 0
            for j in range(i, n):
                xor ^= nums[j]
                a = recursive(j+1, k-1)
                res = min(res, max(a, xor))
            arr[i][k-1] = res
            return res
        return recursive(0, k)
