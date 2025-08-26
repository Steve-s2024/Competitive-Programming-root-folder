# 2200 ~ 2300, too hard to get the details right. it is way too many details to do and make it complicated. the code is
# not complete. the code can't handle some edge cases.
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, max(nums) - 1
        while l <= r:
            m = (l + r) // 2
            bound_lo, bound_hi = 0, 0
            sl = SortedList()
            for i in range(n):
                if m <= nums[i]:
                    bound_lo += len(sl) - sl.bisect_right(nums[i] - m)
                    bound_hi += len(sl) - sl.bisect_left(nums[i] - m)
                else:
                    bound_lo += len(sl)
                    bound_hi += len(sl)
                sl.add(nums[i])
            if bound_lo <= k - 1 <= bound_hi:
                return m
            elif k - 1 < bound_lo:
                r = m - 1
            else:
                l = m + 1



