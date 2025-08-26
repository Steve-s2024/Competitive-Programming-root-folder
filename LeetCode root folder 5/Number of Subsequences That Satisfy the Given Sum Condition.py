# not hard for the rating of 2270, just need to do the power trick, get high power of 2 mod 10**9+7 efficiently.
# the rest is just subsequence counting: 41%
class Solution:
    @staticmethod
    def getPow(b, p):
        MOD = 10**9 + 7
        res = 1
        tmp = b
        while p:
            if p&1:
                res *= tmp
                res %= MOD
            tmp *= tmp
            tmp %= MOD
            p >>= 1
        return res

    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n-1, -1, -1):
            l, r = 0, i-1
            res = -1
            while l <= r:
                m = (l+r)//2
                if nums[m]+nums[i] <= target:
                    res = m
                    l = m+1
                else: r = m-1
            if res != -1:
                # ans += (pow(2, res+1)-1) * pow(2, i-res-1)
                ans += (Solution.getPow(2, res+1)-1) * Solution.getPow(2, i-res-1)
                ans %= MOD
            if nums[i] + nums[i] <= target: ans += 1
        return ans