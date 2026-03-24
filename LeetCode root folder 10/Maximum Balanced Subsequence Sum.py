# 8 seconds, 😅

class MaxTree:
    def __init__(self, ar):
        n = len(ar)
        tre = [-(1<<31)] * ((1 << n.bit_length()) - 1 + n + 1)
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
        res = -(1<<31)

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
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        mxtre = MaxTree([-(1<<31)] * n)
        ar = [(nums[i] - i, i) for i in range(n)]
        ar.sort(key=lambda i: (-i[0], -i[1]))
        res = -inf
        for _, i in ar:
            mx = mxtre.query(i + 1, n - 1) if i < n - 1 else 0
            x = nums[i] + max(0, mx)
            res = max(res, x)
            mxtre.update(i, x)
        return res
