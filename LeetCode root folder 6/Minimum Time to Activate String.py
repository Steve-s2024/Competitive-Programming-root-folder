# my guardian badge is waving~~~~~, let us dance among the star and sing forever mmoooreee~~~
class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(order)
        sl = SortedList()
        sl.add(n)
        sl.add(-1)
        ref = n*(n+1)//2
        tot = n*(n+1)//2
        for i in range(n):
            idx = sl.bisect_left(order[i])
            l, r = sl[idx-1], sl[idx]
            size = r-l-1
            tot -= size*(size+1)//2
            a = (order[i]-l)*(order[i]-l-1)//2
            b = (r-order[i])*(r-order[i]-1)//2
            tot += a + b
            if ref-tot >= k: return i
            sl.add(order[i])
        return -1