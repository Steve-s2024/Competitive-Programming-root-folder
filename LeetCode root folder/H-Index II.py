# binary search solution:0
# ms
# Beats
# 100.00%

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hIndex = 0
        length = len(citations)

        def binarySearch(l, r):
            nonlocal hIndex, length
            if l > r:
                return
            m = l + (r - l) // 2
            hIndexCand = min(citations[m], length - m)
            if hIndexCand == citations[m]:
                hIndex = max(hIndexCand, hIndex)
                binarySearch(m + 1, r)
            elif hIndexCand == length - m:
                hIndex = max(hIndexCand, hIndex)
                binarySearch(l, m - 1)

        binarySearch(0, len(citations) - 1)
        return hIndex