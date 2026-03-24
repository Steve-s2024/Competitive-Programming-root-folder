# 2445? not really.
# now I know why it is a medium but not a hard

class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        def helper(a, b):
            x = gcd(a, b)
            return a // x, b // x

        n = len(nums)
        mx = max(nums)
        mp = [[0] * (mx + 1) for _ in range(mx + 1)]
        for i in range(n - 3, 4 - 1, -1):
            for j in range(i + 2, n):
                c, d = helper(nums[i], nums[j])
                mp[d][c] += 1
        res = 0
        for i in range(2, n - 4):
            for j in range(i - 1):
                a, b = helper(nums[j], nums[i])
                res += mp[a][b]
            for j in range(i + 4, n):
                c, d = helper(nums[i + 2], nums[j])
                mp[d][c] -= 1
        return res
