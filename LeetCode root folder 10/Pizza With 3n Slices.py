# pretty intricate pattern, the problem can be translated into a much simpler version
# solve by hint, the translation of problem can be proved by construction
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        t = n//3
        @cache
        def fn(i, x):
            if i >= n or x >= t: return 0
            return max(fn(i+1, x), fn(i+2, x+1)+slices[i])
        res = fn(1, 0)
        n -= 1
        fn.cache_clear()
        return max(res, fn(0, 0))


