# i questioned my solution for a moment, but than realize it is impeccable lol

class Solution:
    def maxBuilding(self, m: int, rstr: List[List[int]]) -> int:
        if not rstr: return m - 1
        rstr.append([1, 0])
        rstr.sort()
        n = len(rstr)
        ls = []
        for i in range(n):
            dst = rstr[i][0] - (rstr[i - 1][0] if i else 1)
            ls.append(min((ls[-1] if i else 0) + dst, rstr[i][1]))

        rs = [0] * n
        rs[-1] = rstr[-1][1]
        for i in range(n - 2, -1, -1):
            dst = rstr[i + 1][0] - rstr[i][0]
            rs[i] = min(rs[i + 1] + dst, rstr[i][1])
        # print(ls)
        # print(rs)
        ar = [min(ls[i], rs[i]) for i in range(n)]
        res = max(ar)

        for i in range(1, n):
            a, b = ar[i - 1], ar[i]
            l, r = rstr[i - 1][0], rstr[i][0]
            x = r - l - 1
            dif = abs(a - b)
            if dif < x:
                x -= dif
                mx = max(a, b) + ceil(x / 2)
                res = max(mx, res)

        # print(ar[-1] + m-rstr[-1][0])
        return max(res, ar[-1] + m - rstr[-1][0])