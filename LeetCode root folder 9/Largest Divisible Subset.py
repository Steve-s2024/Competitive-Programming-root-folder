


# MLE, but is close, change to iterative bottom up it should pass
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        mp = {}

        @cache
        def recursive(i, prv):
            if i < 0: return 0
            res = recursive(i - 1, prv)
            nxt = 1
            if prv % nums[i] == 0:
                a = recursive(i - 1, nums[i]) + 1
                if a > res:
                    nxt = 2
                    res = a
            mp[(i, prv)] = nxt
            return res

        res = 0
        cr = None
        for i in range(n - 1, -1, -1):
            a = recursive(i - 1, nums[i]) + 1
            if a > res:
                res = a
                cr = (i - 1, nums[i])
        ar = [cr[1]]
        while cr in mp:
            i, prv = cr
            if mp[cr] == 1:
                cr = (i - 1, prv)
            else:
                ar.append(nums[i])
                cr = (i - 1, nums[i])
                # print(res)
        # print(ar)
        return ar


# MLE
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        mp = {}
        @cache
        def recursive(i, LCM):
            nonlocal n
            if i >= n: return 0
            res = recursive(i+1, LCM)
            nxt = 1
            if gcd(LCM, nums[i]) == LCM:
                a = recursive(i+1, lcm(LCM, nums[i]))
                if a+1 > res:
                    nxt = 2
                    res = a+1
            mp[(i, LCM)] = nxt
            return res

        res = recursive(0, 1)
        cr = (0, 1)
        ar = []
        while cr in mp:
            i, LCM = cr
            if mp[cr] == 1: cr = (i+1, LCM)
            else:
                ar.append(nums[i])
                cr = (i+1, lcm(LCM, nums[i]))
        return ar




