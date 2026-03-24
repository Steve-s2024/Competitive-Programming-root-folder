# developed solution to find the longest increasing pair, similar to "Russian Doll Envelope".
# I can't make sense of the 2D pair LIS algorithm which learned from russian doll, so here I developed
# an approach of the same time complexity but with seg tree and dp
class MaxTree:
    def __init__(self, ar):
        n = len(ar)
        tre = [-(1 << 31)] * ((1 << n.bit_length()) - 1 + n + 1)
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
        for j in ar[::-1]: tre[j] = max(tre[2 * j + 1], tre[2 * j + 2])

    def query(self, L, R):
        tre, n = self.tre, self.n
        res = -(1 << 31)

        def recursive(j, l, r):
            nonlocal L, R, res
            if r < L or l > R or l > r: return
            if L <= l and r <= R:
                res = max(res, tre[j])
                return
            m = (l + r) // 2
            recursive(2 * j + 1, l, m)
            recursive(2 * j + 2, m + 1, r)

        recursive(0, 0, (1 << n.bit_length()) - 1)
        return res


class Solution:
    def maxPathLength(self, ar: List[List[int]], k: int) -> int:
        n = len(ar)
        A, B = [], []
        for v in ar:
            if v[0] == ar[k][0]: continue
            if v < ar[k]: A.append(v)
            if v > ar[k]: B.append(v)

        def LIS(arr, a):
            if not arr: return 1
            tp = []
            prv = arr[0][0]
            ct = 1
            for x, y in sorted(arr):
                if x != prv:
                    prv = x
                    ct += 1
                tp.append((ct, y))

            dp = [-inf] * (ct + 1)
            dp[0] = 1
            mxtre = MaxTree(dp)
            for x, y in sorted(tp, key=lambda i: (i[1], -i[0])):
                if y <= a[1]: continue
                mx = mxtre.query(0, x - 1) if x else 0
                mxtre.update(x, mx + 1)
            return mxtre.query(0, ct)

        return LIS(B, ar[k]) + LIS([[-e[0], -e[1]] for e in A], [-ar[k][0], -ar[k][1]]) - 1

