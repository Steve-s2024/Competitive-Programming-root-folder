# three pass, building each in/decreasing interval separately by linear DP
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ar = [-inf] * n
        for i in range(n - 2, -1, -1):
            if nums[i] >= nums[i + 1]: continue
            ar[i] = max(nums[i] + ar[i + 1], nums[i] + nums[i + 1])
        br = [-inf] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]: continue
            if ar[i + 1] > -inf:
                br[i] = nums[i] + ar[i + 1]
            elif br[i + 1] > -inf:
                br[i] = nums[i] + br[i + 1]

        # print(ar, br)
        cr = [-inf] * n
        for i in range(n - 2, -1, -1):
            if nums[i] >= nums[i + 1]: continue
            if br[i + 1] > -inf:
                cr[i] = nums[i] + br[i + 1]
            elif cr[i + 1] > -inf:
                cr[i] = nums[i] + cr[i + 1]
        # print(cr)
        return max(cr)