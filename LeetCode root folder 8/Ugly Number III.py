# ahhhhH!!!!!!!fffffffk!11!!!!11!: 6ms beats 1.13%

# the solution is two line difference than "Nth Magical Number".
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ref = [a, b, c]
        m = len(ref)
        stk = []

        def recursive(i):
            nonlocal m, mid
            size = len(stk)
            res = 0
            if size:
                LCM = stk[0]
                for v in stk: LCM = lcm(LCM, v)
                if size % 2 == 1:
                    res += mid // LCM
                else:
                    res -= mid // LCM
            if size == m: return res
            for j in range(i, m):
                stk.append(ref[j])
                res += recursive(j + 1)
                stk.pop()
            return res

        res = -1
        l, r = 0, 1 << 63
        while l <= r:
            mid = (l + r) // 2
            if recursive(0) >= n:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
