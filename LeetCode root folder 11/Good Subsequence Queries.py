# 😓 why test ramsey theorem?


class GCDTree:
    def __init__(self, ar):
        n = len(ar)
        tre = [-1] * ((1 << n.bit_length()) - 1 + n + 1)
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
        for j in ar[::-1]:
            a, b = tre[2 * j + 1], tre[2 * j + 2]
            if a == -1 or b == -1: tre[j] = max(a, b)
            else: tre[j] = gcd(a, b)

    def query(self, L, R):
        tre, n = self.tre, self.n
        res = -1

        def recursive(j, l, r):
            nonlocal L, R, res
            if r < L or l > R or l > r: return
            if L <= l and r <= R:
                if tre[j] != -1:
                    if res != -1: res = gcd(res, tre[j])
                    else: res = tre[j]
                return
            m = (l + r) // 2
            recursive(2 * j + 1, l, m)
            recursive(2 * j + 2, m + 1, r)

        recursive(0, 0, (1 << n.bit_length()) - 1)
        return res


class Solution:
    def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:

        n = len(nums)
        ar = [-1]*n
        for i in range(n):
            if nums[i]%p == 0: ar[i] = nums[i]//p
        gcdt = GCDTree(ar)

        res = 0

        for i, v in queries:
            v = (v//p) if v%p == 0 else -1
            gcdt.update(i, v)
            ar[i] = v
            # print(ar)

            t = gcdt.query(0, n-1)
            if t == 1: res += 1
        return res
