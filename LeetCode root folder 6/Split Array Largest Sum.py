# the standard binary search on answer solution, to get the iteration correct is the hard part: 63%
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sm = sum(nums)
        l, r = 0, sm
        res = sm
        while l <= r:
            m = (l + r) // 2
            cnt = 0
            tot = 0
            i = 0
            while i < n:
                if nums[i] > m:
                    cnt = inf
                    break
                while i < n and tot + nums[i] <= m:
                    tot += nums[i]
                    i += 1
                cnt += 1
                tot = 0
            if cnt <= k:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
