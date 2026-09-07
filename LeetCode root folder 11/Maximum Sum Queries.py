# nice optimization technique of offline query by segment tree


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
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], qs: List[List[int]]) -> List[int]:
        n = len(nums1)
        q = len(qs)
        cp = sorted(nums2)
        qs = [[qs[i][0], qs[i][1], i] for i in range(q)]
        qs.sort(key=lambda i:i[1])

        j = n-1
        for i in range(q-1, -1, -1):
            y = qs[i][1]
            while j >= 0 and cp[j] >= y: j -= 1
            if j == n-1: qs[i][1] = -1
            else: qs[i][1] = cp[j+1]
        cp = None

        qs.sort(key=lambda i: -i[0])
        ans = [0] * q

        mp = {}
        for i, v in enumerate(sorted(set(nums2))): mp[v] = i

        m = len(mp)
        mt = MaxTree([-1] * m)
        tp = [-1] * m

        ar = [(nums1[i], nums2[i]) for i in range(n)]
        ar.sort()
        j = n - 1
        # print(ar, qs)
        for x, y, i in qs:
            if y == -1:
                ans[i] = -1
                continue

            while j >= 0 and ar[j][0] >= x:
                idx = mp[ar[j][1]]
                tp[idx] = max(tp[idx], ar[j][0] + ar[j][1])
                mt.update(idx, tp[idx])
                j -= 1

            idx = mp[y]
            ans[i] = mt.query(idx, m - 1)

        return ans
