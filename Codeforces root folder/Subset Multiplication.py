# fking letsgoooo!, no tle gang!, gcd lcm gang! no idea why the math.gcd and lcm function only take log(n) time but not
# sqrt(n) time, otherwise it will definitely hit TLE

import math


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    g = nums[-1]
    res = 1
    for i in range(n-2, -1, -1):
        g = math.gcd(g, nums[i])
        re = nums[i]//g
        res = math.lcm(res, re)

    print(res)

t = int(input())
for i in range(t):
    solve()