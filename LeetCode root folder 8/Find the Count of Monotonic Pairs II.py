# dp + prefix sum optimization, very hard for me. I first time tried the prefix sum optimization on dp using bottom
# up. especially you need to observe the monotonicity of k to make it work.

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [i+1 for i in range(nums[-1], -1, -1)]
        # print(suf)
        mod = 10**9 + 7
        for i in range(n-2, -1, -1):
            tmp = [0]*(nums[i]+1)
            k = 0
            for j in range(nums[i]+1):
                a, b = j, nums[i]-j
                while k < a or nums[i+1]-k > b: k += 1
                if k <= nums[i+1]: tmp[a] = suf[k]
            suf = [0]*(nums[i]+1)
            for j in range(nums[i], -1, -1): suf[j] = (tmp[j] + suf[(j+1)%(nums[i]+1)])%mod
            # print(suf)
        return suf[0]