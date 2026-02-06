# I am such an expert in DP ngl
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        n, m = len(arr1), len(arr2)

        @cache
        def recursive(i):
            if i >= n: return 0
            x = arr1[i - 1] if i else -1

            j = bisect_right(arr2, x)
            l = 1
            res = inf
            if not i or arr1[i - 1] < arr1[i]: res = recursive(i + 1)
            while j < m:
                nx = arr1[i + l] if i + l < n else inf
                if nx > arr2[j]:
                    a = recursive(i + l + 1) + l
                    res = min(res, a)
                j += 1
                l += 1
            return res

        res = recursive(0)
        return res if res != inf else -1
