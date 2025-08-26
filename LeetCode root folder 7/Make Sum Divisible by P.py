# 39%
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        re = sum(nums)%p
        if re == 0: return 0
        n = len(nums)
        mp = {}
        mp[0] = -1
        cur = 0
        res = inf
        for i in range(n):
            cur += nums[i]
            a = (cur%p+p-re)%p
            if a in mp: res = min(res, i-mp[a])
            mp[cur%p] = i
        return res if res != n else -1