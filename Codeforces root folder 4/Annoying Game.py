# fking annoying, but indeed forced me to think creatively and invented the algorithm of max sum subarray with one
# addition to some element
# this also helped me to really dig deep and understand the fundamental logic behind the regular max sum subarray algo

from math import sqrt, gcd, lcm, inf


def solve():
    n, k = [int(e) for e in input().split()]
    ar = [int(e) for e in input().split()]
    br = [int(e) for e in input().split()]



    if k%2 == 0:
        x = 0
        res = -inf
        for i, v in enumerate(ar):
            x += v
            res = max(x, res)
            x = max(0, x)
        print(res)
    else:
        y = ar[0]
        x = ar[0]+br[0]
        res = x
        for i in range(1, n):
            y = max(y, 0)
            y += ar[i]

            x += ar[i]
            if y+br[i] > x: x = y+br[i]
            res = max(res, x)

        print(res)

t = int(input())
for i in range(t): solve()