# I am a freaking genius holy shit
# new technique acquired, restore the optimal decision from dp with unaffected time complexity
# the data restored represents a unique sequence of decisions that will lead to the optimal result
# same as the restoration technique used in restoring LIS
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pre = []
        t = 0
        for i in range(n):
            t += nums[i]
            pre.append(t)

        mp = {}

        @cache
        def recursive(i, x):
            if i >= n: return 0 if x == 0 else -inf
            res = recursive(i + 1, x)
            mp[(i, x)] = 1
            if x and i + k <= n:
                a = recursive(i + k, x - 1) + pre[i + k - 1] - (pre[i - 1] if i else 0)
                if a >= res:
                    res = a
                    mp[(i, x)] = 2
            return res

        res = recursive(0, 3)
        # print(res)
        # print(mp)
        i = 0
        x = 3
        ar = []
        while i < n and x > 0:
            typ = mp[(i, x)]
            if typ == 1:
                i += 1
            else:
                ar.append(i)
                i += k
                x -= 1

        return ar