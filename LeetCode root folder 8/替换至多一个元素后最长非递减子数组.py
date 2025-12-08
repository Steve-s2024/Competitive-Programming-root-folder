# 比较新颖的一个解法， 我的滑窗该练了。


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        pre = [1] * n
        suf = [1] * n
        for i in range(n):
            j = max(j, i + 1)
            while j < n and nums[j - 1] <= nums[j]:
                l = j - i + 1
                suf[j] = max(suf[j], l)
                j += 1
            pre[i] = j - i

        # print(pre, suf)

        ans = 1
        for i in range(n):
            a = 0
            b = 0
            if i: a = suf[i - 1]
            if i < n - 1: b = pre[i + 1]

            if i and i < n - 1:
                if nums[i - 1] <= nums[i + 1]:
                    res = a + b + 1
                else:
                    res = max(a, b) + 1
            else:
                res = a + b + 1
            ans = max(res, ans)
        return ans

        return 0
