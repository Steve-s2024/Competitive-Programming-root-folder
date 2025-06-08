# brute force: TLE
'''class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # brute force
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums) - 1, i - 1, -1):
                if nums[j] >= nums[i]:
                    res = max(j - i, res)
        return res'''

# greedy solution, sorting with tuple: (idx, val) | linear:126
# ms
# Beats
# 18.37%
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        arr = [(idx, num) for idx, num in enumerate(nums)]
        arr.sort(key=lambda i : i[1], reverse=True)
        # print(arr)

        maxWid = 0
        for i in range(len(nums) - 1, -1, -1):
            while arr and nums[i] >= arr[-1][1]:
                maxWid = max(maxWid, i - arr[-1][0])
                arr.pop()

        return maxWid