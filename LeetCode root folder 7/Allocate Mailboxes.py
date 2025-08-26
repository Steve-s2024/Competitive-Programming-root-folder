# if this is more complicated than the intended solution, then it mean I am able to solve a problem harder than it
# intended to be, and so I've actually solved an above 2180 rating question: 10%

class Solution:
    def minDistance(self, houses: List[int], K: int) -> int:
        houses.sort()
        n = len(houses)
        pre = [0] * n
        tot = 0
        prev = houses[0]
        for i in range(1, n):
            tot += i * (houses[i] - prev)
            pre[i] = tot
            prev = houses[i]

        suf = [0] * n
        tot = 0
        prev = houses[-1]
        for i in range(n - 2, -1, -1):
            tot += (n - i - 1) * (prev - houses[i])
            suf[i] = tot
            prev = houses[i]


        mp = [[[0] * n for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    tot = pre[j] - pre[i] + suf[j] - suf[k]
                    ofs = i * (houses[j] - houses[i]) + (n - 1 - k) * (houses[k] - houses[j])
                    mp[i][j][k] = tot - ofs

        @cache
        def recursive(i, j, k):
            nonlocal n
            if i >= n: return 0 if k == 0 and j == n else inf
            res = recursive(i + 1, j, k)
            if k > 0:
                l, r = j, i
                m = (l + r) // 2
                res = min(res, recursive(i + 1, i + 1, k - 1) + mp[l][m][r])
            return res

        return recursive(0, 0, K)