# almost the same idea as "757. Set Intersection Size At Least Two"

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        mx = max(e[1] for e in tasks)
        ar = [0] * (mx + 1)
        tasks.sort(key=lambda i: i[1])
        for l, r, d in tasks:
            t = d - sum(ar[l:r + 1])
            for i in range(r, l - 1, -1):
                if t <= 0: break
                if ar[i]: continue
                ar[i] = 1
                t -= 1
            # print(ar)

        return sum(ar)
