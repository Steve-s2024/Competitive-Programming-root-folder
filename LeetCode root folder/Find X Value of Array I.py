# brute force:TLE

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0]*k
        res = 0
        n = len(nums)
        for i in range(n):
            cur = 1
            for j in range(i, n):
                cur *= nums[j]
                ans[cur%k] += 1
        return ans


# dp solution, under stress is not the best motivator...:
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [0] * k
        dp = [[0] * k for i in range(n)]
        for i in range(n):
            cur = nums[i]
            dp[i][cur % k] += 1

            if i > 0:
                for remain in range(k):
                    newRemain = (remain * cur) % k
                    dp[i][newRemain] += dp[i - 1][remain]
            for j in range(k):
                ans[j] += dp[i][j]
        # print(dp)
        return ans©leetcode