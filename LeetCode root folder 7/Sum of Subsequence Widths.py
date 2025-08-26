# mathy question, don't enjoy it so much: 34%
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        # efficiently find
        # sums of all nums[i] and nums[i+1]
        # sums of all nums[i] and nums[i+2]
        # ...
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        pre = []
        tot = 0
        for num in nums:
            tot += num
            pre.append(tot)
        res = 0
        for i in range(1, n):
            sm = pre[-1]-pre[i-1] - pre[-i-1]
            res += pow(2, i-1, MOD) * sm
            res %= MOD
        return res



#TLE
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                size = j-i-1
                res += pow(2, size, MOD) * (nums[j]-nums[i])
                res %= MOD
        return res