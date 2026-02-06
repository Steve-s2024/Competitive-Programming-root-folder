# holy the program run for 17 seconds straight lol.
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)

        @cache
        def fn(i, f, K):
            nonlocal n, m
            if i >= n: return 0 if K == 0 else -inf

            res = fn(i+1, f, K) + (nums[i] if f else 0)
            if f: res = max(res, fn(i, 0, K))
            if not f and K and i+m <= n:
                sm = 0
                for j in range(i, i+m): sm += nums[j]
                res = max(res, fn(i+m, 1, K-1) + sm)
            return res
        res = fn(0, 0, k)
        fn.cache_clear()
        return res



