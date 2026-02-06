# sparse table is really flexible, I only need to change two word in the min sparse table to turn it into a gcd table
class GCDTable():
    def __init__(self, nums):
        self.sp = self.build(nums)

    def build(self, nums):
        n = len(nums)
        sp = [nums[:]]
        pw = 2
        while pw <= n:
            tmp = []
            for i in range(0, n - pw + 1): tmp.append(gcd(sp[-1][i], sp[-1][i + pw // 2]))
            sp.append(tmp)
            pw *= 2
        return sp

    def query(self, l, r):
        sp = self.sp
        sz = r - l + 1
        ln = sz.bit_length()
        res = gcd(sp[ln - 1][l], sp[ln - 1][r - pow(2, ln - 1) + 1])
        return res


class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        st = GCDTable(nums)
        n = len(nums)
        res = -1
        l, r = 0, n
        while l <= r:
            m = (l + r) // 2
            i = m
            x = 0
            while i < n:
                if st.query(i - m, i) >= 2:
                    x += 1
                    i += m + 1
                else:
                    i += 1

            # print(m, x)
            if x <= maxC:
                r = m - 1
                res = m
            else:
                l = m + 1

        return res

# TLE, maybe sparse table can pass? with its O(1) query time
class SumTree:
    def __init__(self, ar):
        n = len(ar)
        tre = [0] * ((1 << n.bit_length()) - 1 + n)
        self.tre, self.n = tre, n
        for i in range(n): self.update(i, ar[i])

    def update(self, i, v):
        tre, n = self.tre, self.n
        l, r = 0, (1 << n.bit_length()) - 1
        j, ar = 0, []
        while l < r:
            ar.append(j)
            m = (l + r) // 2
            if i <= m:
                j, r = 2 * j + 1, m
            else:
                j, l = 2 * j + 2, m + 1
        tre[j] = v
        for j in ar: tre[j] = gcd(tre[j] if tre[j] else v, v)

    def query(self, L, R):
        tre, n = self.tre, self.n
        res = 0

        def recursive(j, l, r):
            nonlocal L, R, res
            if r < L or l > R or l > r: return
            if L <= l and r <= R:
                res = gcd(res if res else tre[j], tre[j])
                return
            m = (l + r) // 2
            recursive(2 * j + 1, l, m)
            recursive(2 * j + 2, m + 1, r)

        recursive(0, 0, (1 << n.bit_length()) - 1)
        return res


class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        tre = SumTree(nums)
        n = len(nums)
        res = -1
        l, r = 0, n
        while l <= r:
            m = (l + r) // 2
            i = m
            x = 0
            while i < n:
                if tre.query(i - m, i) >= 2:
                    x += 1
                    i += m + 1
                else:
                    i += 1

            # print(m, x)
            if x <= maxC:
                r = m - 1
                res = m
            else:
                l = m + 1

        return res