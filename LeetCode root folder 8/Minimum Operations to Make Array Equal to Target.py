# not very intuitive difference array solution: 57%

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        arr = [0] * n
        arr[0] = nums[0]
        brr = [0] * n
        brr[0] = target[0]
        for i in range(1, n):
            arr[i] = nums[i] - nums[i - 1]
            brr[i] = target[i] - target[i - 1]

        pos, neg = 0, 0
        for i in range(n):
            dif = brr[i] - arr[i]
            if dif >= 0:
                pos += dif
            else:
                neg += dif

        return max(pos, abs(neg))

