# haven't done hashmap optimized dp too much, still need practice, but overall it is a good and generalizable approach
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(k + 1)]
        for K in range(k + 1): dp[K][nums[-1]] = 1
        mp = [1]*(k+1)

        for i in range(n - 2, -1, -1):
            mx = 0
            ar = []
            for K in range(k + 1):
                mx = dp[K][nums[i]] + 1
                if K:
                    # a = max(dp[K - 1].values()) + 1
                    a = mp[K-1]+1
                    mx = max(a, mx)
                ar.append(mx)
            for K in range(k+1):
                mp[K] = max(mp[K], ar[K])
                dp[K][nums[i]] = ar[K]

        # print(dp)
        # for e in dp: print(e)
        return max(e for mp in dp for e in mp.values())




# a general knap sack, TLE. use this as a base to build the prefix sum optimized dp, or maybe it is hashmap dp.
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def recursive(i, K):
            if K < 0: return -inf
            if i >= n: return 0
            res = -inf
            for j in range(i, n):
                a = recursive(j + 1, K - (1 if i and nums[i - 1] != nums[j] else 0)) + 1
                res = max(res, a)

            return max(res, recursive(n, K))

        res = recursive(0, k)
        print(res)
        return res