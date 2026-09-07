# haha...
class Solution:
    def even(self, s, k):
        mp = [0, 0]
        for c in s: mp[int(c)] += 1
        # for even K only
        if mp[0] % 2: return -1
        if mp[0] % k == 0: return mp[0] // k
        res = -1
        l, r = 1, 10 ** 5
        while l <= r:
            m = (l + r) // 2
            m *= 2
            tot = mp[0] * ((m - 1) // 2 * 2) + mp[1] * (m // 2 * 2)
            if tot + mp[0] >= m * k >= mp[0]:
                res = m
                r = m // 2 - 1
            else:
                l = m // 2 + 1
        t = res
        l, r = 1, 10 ** 5
        while l <= r:
            m = (l + r) // 2
            m = 2 * m - 1
            tot = mp[0] * ((m - 1) // 2 * 2) + mp[1] * (m // 2 * 2)
            if tot + mp[0] >= m * k >= mp[0]:
                res = m
                r = (m + 1) // 2 - 1
            else:
                l = (m + 1) // 2 + 1
        # print(res, t)
        return min(res, t)

    def odd(self, s, k):
        mp = [0, 0]
        for c in s: mp[int(c)] += 1
        # for odd K only
        if mp[0] % k == 0: return mp[0] // k

        if mp[0] % 2 == 0:
            res = -1
            l, r = 1, 10 ** 5
            while l <= r:
                m = (l + r) // 2
                m *= 2
                tot = mp[0] * ((m - 1) // 2 * 2) + mp[1] * (m // 2 * 2)
                if tot + mp[0] >= m * k >= mp[0]:
                    res = m
                    r = m // 2 - 1
                else:
                    l = m // 2 + 1
            return res
        else:
            res = -1
            l, r = 1, 10 ** 5
            while l <= r:
                m = (l + r) // 2
                m = 2 * m - 1
                tot = mp[0] * ((m - 1) // 2 * 2) + mp[1] * (m // 2 * 2)
                if tot + mp[0] >= m * k >= mp[0]:
                    res = m
                    r = (m + 1) // 2 - 1
                else:
                    l = (m + 1) // 2 + 1
            return res

    def minOperations(self, s: str, k: int) -> int:
        if k % 2: return self.odd(s, k)
        return self.even(s, k)
