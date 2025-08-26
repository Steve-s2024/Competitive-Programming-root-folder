# 10%
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        arr = nums[:]
        sm = sum(arr)
        res = sm
        for i in range(1, n):
            for j in range(n):
                sm -= arr[j]
                arr[j] = min(arr[j], nums[(j+i)%n])
                sm += arr[j]
            res = min(res, sm+(i*x))
        return res