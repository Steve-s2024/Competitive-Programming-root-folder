# a new record for 2500, under 10min


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        n = len(nums)
        mx = max(nums)
        mp = [0]*(mx+1)
        for i in range(n):
            mp[nums[i]] += 1


        res = 0
        for i in range(1, mx+1):
            t = -1
            for j in range(i, mx+1, i):
                if mp[j]:
                    if t == -1: t = j//i
                    else: t = gcd(t, j//i)
                if t == 1:
                    res += 1
                    break
        return res
