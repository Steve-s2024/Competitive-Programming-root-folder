# binary search solution, more like brute force because i made r as 10**14 for every testcase:2005
# ms
# Beats
# 5.02%

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        l, r = 0, 10**14
        while l < r:
            m = (l + r) // 2
            total = 0
            for t in time:
                if m < t:
                    break
                total += m // t
            if total >= totalTrips:
                r = m
            else:
                l = m+1
        return l

# a tiny change make a big difference:899
# ms
# Beats
# 44.84%
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        l, r = 0, time[0] * totalTrips
        while l < r:
            m = (l + r) // 2
            total = 0
            for t in time:
                if m < t:
                    break
                total += m // t
            if total >= totalTrips:
                r = m
            else:
                l = m+1
        return l