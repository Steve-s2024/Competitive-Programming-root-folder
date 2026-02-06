# worrying that I must have miss something crucial, then WA on the testcases where require additional checking on whether
# result could be 1
# the binary search will cover cases from 2 to n, but 1 must be handled separately. really rare to happen that binary search
# can't handle below certain threshold
# overall very straightforward considered it is 2376
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        ar = []
        x = 1
        for i in range(1, n):
            if s[i] != s[i - 1]:
                ar.append(x)
                x = 1
            else:
                x += 1
        ar.append(x)

        l, r = 2, n
        res = -1
        while l <= r:
            m = (l + r) // 2
            t = 0
            for i in range(len(ar)): t += ar[i] // (m + 1)
            if t <= numOps:
                res = m
                r = m - 1
            else:
                l = m + 1

        f = '0'
        a = 0
        for i in range(n):
            if s[i] != f: a += 1
            f = '1' if f == '0' else '0'

        f = '1'
        b = 0
        for i in range(n):
            if s[i] != f: b += 1
            f = '1' if f == '0' else '0'
        if min(a, b) <= numOps: res = 1

        return res