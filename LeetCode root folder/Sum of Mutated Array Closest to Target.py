class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # binary search, initially set boundary as 0 to target
        max_ = max(arr)
        l, r = 0, min(target, max_)
        res = float('inf')
        minDiff = float('inf')
        while l <= r:
            m = l + (r - l) // 2
            total = 0
            for num in arr:
                total += min(m, num)
            diff = abs(total - target)
            if diff < minDiff:
                minDiff = diff
                res = m
            elif diff == minDiff:
                res = min(res, m)
            if total > target:
                r = m - 1
            else:
                l = m + 1

        return res