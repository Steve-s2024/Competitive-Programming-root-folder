# I'm decently smart and adequate to this 2300 rated problem: 59%
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        mp = [0]*32
        for num in nums:
            i = 0
            while num:
                mp[i] += num%2
                num >>= 1
                i += 1
        # print(mp)
        res = 0
        for i in range(k):
            tot = 0
            for j in range(32):
                if mp[j]:
                    tot += 1<<j
                    mp[j] -= 1
            res += tot**2
            res %= MOD
        return res
