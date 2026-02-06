# weak testcases let the n^4 solution passed, I was thinking if this hit TLE I would do prefix optimize to n^3
# weak!

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = [n] * n
        stk = []
        for i in range(n):
            while stk and stk[-1][0] <= nums[i]: mp[stk.pop()[1]] = i
            stk.append((nums[i], i))

        # print(mp)

        @cache
        def recursive(i, cr, K):
            nonlocal n
            if i >= n: return 0
            res = inf
            if nums[i] <= cr: res = recursive(i + 1, cr, K) + cr - nums[i]
            if K:
                j = i
                while j < n:
                    a = recursive(i + 1, nums[j], K - 1) + nums[j] - nums[i]
                    j = mp[j]
                    res = min(res, a)
            return res

        res = inf
        j = 0
        while j < n:
            a = recursive(0, nums[j], k)
            res = min(res, a)
            j = mp[j]
        return res