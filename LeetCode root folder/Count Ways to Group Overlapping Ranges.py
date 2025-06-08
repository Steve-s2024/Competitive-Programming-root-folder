# merging overlapping interval solution:41
# ms
# Beats
# 29.24%
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key = lambda i : i[0])
        [prevL, prevR] = ranges[0]
        merged = []
        for l, r in ranges[1:]:
            if prevR >= l:
                # overlap:
                prevR = max(prevR, r)
            else:
                # not overlap
                merged.append((prevL, prevR))
                prevL, prevR = l, r
        merged.append((prevL, prevR))
        # print(merged)
        res = 1
        l = len(merged)
        return pow(2, l) % (pow(10, 9)+7)