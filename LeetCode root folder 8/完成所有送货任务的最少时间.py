# 操， 全国第16个解出前三题的。 我他妈的真鸡巴无敌 2025/11/1



class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        res = 0
        le, ri = 0, 1<<64
        while le <= ri:
            m = (le+ri)//2
            # check if m times is enough
            a = m//r[0]
            b = m//r[1]
            c = m//(lcm(r[0],r[1]))

            x, y = d
            x -= (b-c)
            y -= (a-c)
            x, y = max(x, 0), max(y, 0)
            if x+y <= m-a-b+c:
                res = m
                ri = m-1
            else: le = m+1

        return res