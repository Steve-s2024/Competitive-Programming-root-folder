# a sorted list implementation, the key is to notice the translation of inversion count between two adjacent size k subarray
# (only take logn time if implemented with a structure like sorted set/list)
class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sl = SortedList()
        cr = 0
        for i in range(k):
            x = sl.bisect_right(nums[i])
            cr += len(sl)-x
            sl.add(nums[i])
        res = cr
        # print(cr)
        for i in range(k, n):
            y = sl.bisect_left(nums[i-k])
            cr -= y
            sl.remove(nums[i-k])
            x = sl.bisect_right(nums[i])
            # print(y, x)
            cr += len(sl)-x
            sl.add(nums[i])
            res = min(res, cr)

        return res