# 反悔贪心第一题： 9%
class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0: return -1
        n = len(nums)
        res = 0
        minheap = []
        tot = 0
        for i in range(n):
            tot += nums[i]
            heappush(minheap, nums[i])
            while minheap and tot < 0:
                tot -= heappop(minheap)
                res += 1

        return res
