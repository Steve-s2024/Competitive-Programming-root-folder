# sliding window solution:3
# ms
# Beats
# 27.43%
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        l, r = 0, 0
        maxLen = 0
        while r < len(citations):
            while l < len(citations) and (r-l+1) > citations[l]:
                l += 1
            maxLen = max(maxLen, r-l+1)
            r += 1
        return maxLen