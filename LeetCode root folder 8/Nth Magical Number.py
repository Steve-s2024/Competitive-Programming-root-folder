# using the PIE (principle of inclusion-exclusion) template, easily compute the number of magical number in a given
# range. then, binary search for the answer: 16%
class Solution:

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        ref = [a, b]
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

        return res % (10 ** 9 + 7)


