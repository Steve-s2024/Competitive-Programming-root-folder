# sweat a bit, a decent brain workout (considering optimize the segtree implementation though it is causing TLE a bit)


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
        dif = v - tre[j]
        tre[j] = v
        for j in ar: tre[j] += dif

    def query(self, L, R):
        tre, n = self.tre, self.n
        res = 0

        def recursive(j, l, r):
            nonlocal L, R, res
            if r < L or l > R or l > r: return
            if L <= l and r <= R:
                res += tre[j]
                return
            m = (l + r) // 2
            recursive(2 * j + 1, l, m)
            recursive(2 * j + 2, m + 1, r)

        recursive(0, 0, (1 << n.bit_length()) - 1)
        return res


def calcDst(nums):
    n = len(nums)
    tp = [(nums[i], i + 1) for i in range(n)]
    tp.sort()
    sm = n * (n + 1) // 2
    ofs = n * (n + 1) // 2  # ofs is the offset dst which sm overcalculate

    prv = 0
    res = 0
    for i in range(n):
        e, j = tp[i]
        x = e - prv
        res += x * (sm - ofs)

        prv = e
        sm -= j
        ofs -= (n - i)

    return res


def solve():
    n = int(input())
    nums = [int(e) - 1 for e in input().split()]
    smt = SumTree([0] * n)
    cp = [0] * n

    suf = [0] * n

    stk = []
    for i in range(n):
        while stk and stk[-1][0] <= nums[i]:
            _, j = stk.pop()
            suf[j] = i
        stk.append((nums[i], i))
    while stk: suf[stk.pop()[1]] = n

    idx, mx = -1, 0
    for i in range(n):
        e = nums[i]
        sm = smt.query(e, n - 1)

        dst = suf[i] - i - 1
        t = sm - dst
        if t > mx: idx, mx = i, t

        cp[e] += 1
        smt.update(e, cp[e])

    if idx != -1: nums[idx] -= 1
    print(calcDst(nums[::-1]))


for _ in range(int(input())): solve()