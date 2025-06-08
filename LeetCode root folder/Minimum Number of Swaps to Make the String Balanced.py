# I inadvertently discovered this solution... probably the optimal, and it does not use hash map:123
# ms
# Beats
# 98.31%
class Solution:
    def minSwaps(self, s: str) -> int:
        count1 = 0
        for c in s:
            if c == '[':
                count1 += 1
            elif count1:
                count1 -= 1
        return ceil(count1 / 2)