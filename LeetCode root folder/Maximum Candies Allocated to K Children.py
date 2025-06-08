# typical binary search solution, as boring as usual:345
# ms
# Beats
# 64.64%
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def binarySearch(l, r):
            nonlocal res
            if l > r:
                return
            m = (l + r) // 2
            total = 0
            for c in candies:
                total += c // m
            if total >= k:
                res = m
                binarySearch(m+1, r)
            else:
                binarySearch(l, m-1)
        res = 0
        binarySearch(1, max(candies))
        return res