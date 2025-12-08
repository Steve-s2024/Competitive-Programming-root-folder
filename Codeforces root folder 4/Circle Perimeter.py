# done it before, simple line sweep algo. but the implementation is not accurate. it does the job nonetheless
from math import gcd, lcm, inf, sqrt, floor, ceil
def solve():
    r = int(input())
    res = 0
    for x in range(-r, r+1):
        y = sqrt((r+1)**2 - x**2)
        if y == int(y): res += 2*(y-1)
        else: res += 2*floor(y)
    for x in range(-r+1, r):
        y = sqrt(r** 2 - x**2)
        if y == int(y): res -= 2*(y - 1)
        else: res -= 2*floor(y)

    print(int(res+2))

t = int(input())
for i in range(t): solve()