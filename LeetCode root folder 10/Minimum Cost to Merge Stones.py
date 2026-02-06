# brain melting multidimensional DP, don't felt joyful even after solving it

class Solution:
    def mergeStones(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if (n - 1) % (k - 1): return -1
        pre = [0]*n
        for i in range(n): pre[i] = pre[i-1]+nums[i]

        @cache
        def fn(l, r, i, x):
            # print(l, r, i, x)
            nonlocal k, n
            if l == r: return 0
            if x == 0 and i <= r: return inf
            if i > r: return 0 if x == 0 else inf

            res = inf
            for j in range(i, r + 1):
                if i == l and j == r: continue
                sm = pre[j] - pre[i] + nums[i]
                a = fn(l, r, j + 1, x - 1)
                b = fn(i, j, i, k) + a + sm
                # if l == 0 and r == n-1: print(i, j, x, b)
                res = min(res, b)
            return res

        res = fn(0, n - 1, 0, k)
        return res