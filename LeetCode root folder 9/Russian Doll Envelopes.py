# LIS problem, really hard to spot I only recognized that after seen the editorial

class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        e.sort(key = lambda i : (i[0], -i[1]))
        ar = []
        n = len(e)
        for i in range(n):
            v = e[i]
            res = -1
            l, r = 0, len(ar)-1
            while l <= r:
                m = (l+r)//2
                if ar[m][1] < v[1]:
                    res = m
                    l = m+1
                else: r = m-1
            if res+1 < len(ar): ar[res+1] = v
            else: ar.append(v)

        return len(ar)