# trying the bit contribution approach, couldn't get the formula at the end work.
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [[-1, -1] for _ in range(n)]
        # def recursive(i, f):
        #     if i >= n: return f
        #     if dp[i][f] != -1: return dp[i][f]
        #     res = (
        #         recursive(i+1, (f+1)%2) +
        #         recursive(i+1, f)
        #     )
        #     dp[i][f] = res
        #     return res
        # recursive(0, 0)
        # print(dp)

        # initially i thought the DP has issue, but then after trying by hand, it is proven that
        # the number of subset with odd size of n sized array, is exactly 2**n//2. In another word,
        # half of the number of all subsets of that array

        mp = [0] * 5
        for i in range(n):
            num = nums[i]
            j = 0
            while num:
                mp[j] += num % 2
                num >>= 1
                j += 1
        res = 0
        for i in range(5):
            if mp[i]:
                f = 2 ** (n - mp[i])
                # print(f, 2**max(mp[i]-2, 0) * f * (1<<i) * mp[i])
                res += 2 ** max(mp[i] - 2, 0) * f * (1 << i) * mp[i] # formula not yielding right output

        return res


