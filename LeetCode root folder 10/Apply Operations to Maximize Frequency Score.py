# binary search, took me 2 hours and tried many implementation.
# the final code is actually short

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        pre = [0]*n
        for i in range(n): pre[i] = pre[i-1] + nums[i]
        # print(nums)
        ans = 0
        for i in range(n):
            l, r = i, n-1
            res = -1
            while l <= r:
                m = (l+r)//2
                j = i+(m-i)//2
                a = nums[j]*(j-i+1) - (pre[j]-pre[i]+nums[i])
                b = pre[m]-pre[j]+nums[j] - nums[j]*(m-j+1)
                # print(i, m, a, b)
                if a+b <= k:
                    res = m
                    l = m+1
                else: r = m-1
            # print(i, res)
            ans = max(ans, res-i+1)
        # print(ans)
        return ans