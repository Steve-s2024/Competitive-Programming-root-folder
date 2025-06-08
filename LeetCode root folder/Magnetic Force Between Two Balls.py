
# good to see the progress of me than a year ago
# at that time i spent a long time to come up with the 
# brute force JS solution
# binary search and simulation solution: 594
# ms
# Beats
# 13.40%
class Solution:
    def maxDistance(self, position: List[int], ball: int) -> int:
        # binary search??
        position.sort()
        n = len(position)

        def ifValid(minGap):
            nonlocal n
            prev = position[0]
            i = 1
            cnt = 1
            while i < n:
                diff = position[i] - prev
                if diff >= minGap:
                    cnt += 1
                    prev = position[i]
                i += 1
            return cnt >= ball

        l, r = 1, position[-1] - position[0]
        res = r
        while l <= r:
            # print(l, r)
            # consider m as the min distance between any two ball
            m = (l+r)//2
            if ifValid(m):
                res = m
                l = m+1
            else:
                r = m-1
        return res

        
        