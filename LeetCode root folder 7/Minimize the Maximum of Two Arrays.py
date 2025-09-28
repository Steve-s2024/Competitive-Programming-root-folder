# show some respect to the genius please!: 100%
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        LCM = lcm(divisor1, divisor2)
        l, r = 0, 1<<64
        res = -1
        while l <= r:
            m = (l+r)//2
            mul = m//LCM
            cnt1 = m//divisor1 - mul
            cnt2 = m//divisor2 - mul
            a, b = max(0, uniqueCnt1-cnt2), max(0, uniqueCnt2-cnt1)
            if m - mul - cnt1 - cnt2 >= a+b:
                res = m
                r = m-1
            else: l = m+1

        return res


# binary search attempt, a bug need fix
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        LCM = lcm(divisor1, divisor2)
        tot = uniqueCnt1 + uniqueCnt2
        l, r = 0, 1<<64
        res = -1
        while l <= r:
            m = (l+r)//2
            mul = m//LCM
            if m-mul >= tot:
                res = m
                r = m-1
            else: l = m+1
        return res