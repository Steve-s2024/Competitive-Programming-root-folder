# simple brute-force simulation will do thanks to the poor constraint:3
# ms
# Beats
# 33.82%
class Solution:
    def minimizeResult(self, expression: str) -> str:
        [n1, n2] = expression.split('+')
        a, b,  = '', n1
        res = ''
        minVal = float('inf')
        for l in range(len(n1)):
            c, d = n2, ''
            for r in range(len(n2)-1, -1, -1):
                # print(a, b, c, d)
                val = (int(a) if len(a) else 1) * (int(b)+int(c)) * (int(d) if len(d) else 1)
                if val < minVal:
                    minVal = val
                    res = a+'('+b+'+'+c+')'+d
                c = c[:-1]
                d = n2[r] + d
            a += n1[l]
            b = b[1:]
        return res