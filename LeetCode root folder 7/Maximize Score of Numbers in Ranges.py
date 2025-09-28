# binary search question: 20%
class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        l, r = 0, start[-1]+d
        n = len(start)
        res = -1
        while l <= r:
            m = (l+r)//2
            prev = start[0]
            for i in range(1, n):
                if prev+m > start[i]+d: break
                prev = max(prev+m, start[i])
            else:
                res = m
                l = m+1
                continue
            r = m-1
        return res