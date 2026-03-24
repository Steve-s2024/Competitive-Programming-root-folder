# I cannot believe a 2460 question can be so easy...
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, pos: List[int], time: List[int]) -> int:
        @cache
        def fn(i, k, t):
            if i >= n - 1: return 0 if k == 0 else inf

            sm, j, res = 0, 0, inf
            while i + j + 1 <= n - 1 and j <= k:
                sm += time[i + j + 1]
                a = fn(i + j + 1, k - j, sm) + (pos[i + j + 1] - pos[i]) * t
                res = min(res, a)
                j += 1
            return res

        return fn(0, k, time[0])


