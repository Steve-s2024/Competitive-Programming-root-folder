# binary search and simulate solution, i actually
# already knew this approach of binary search back
# in decimal 2024 when I first solved this problem: 41%
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        res = r
        while l <= r:
            m = (l+r)//2
            # pretend m is the target
            totalOp = 0
            for n in nums:
                totalOp += math.ceil(n/m)-1
            if totalOp > maxOperations:
                l = m+1
            else:
                res = m
                r = m-1
        return res