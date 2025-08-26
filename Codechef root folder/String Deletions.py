# fking kidding me? this is exactly the same as the long code commented out. I did not expect this to work while the
# long one failed

import math
from math import inf, gcd, lcm
from functools import cache
from collections import Counter



def solve():
    n = int(input())
    s = input()
    l, r = 0, n-1
    res = 0
    while l < n and s[l] == s[0]:
        res += 1
        l += 1
    while r >= 0 and s[r] == s[-1]:
        res += 1
        r -= 1
    if res == n*2:
        print(n)
        return


    if s[0] != s[-1] and res != n: res += 1
    print(res)

t = int(input())
for i in range(t):
    solve()




# def solve():
#     n = int(input())
#     s = input()
#     onel, oner = inf, -inf
#     zerol, zeror = inf, -inf
#     for i in range(n):
#         if s[i] == '0':
#             zerol = min(zerol, i)
#             zeror = max(zeror, i)
#
#         if s[i] == '1':
#             onel = min(onel, i)
#             oner = max(oner, i)
#
#     # print(zerol, zeror)
#     # print(onel, oner)
#     if zerol == inf or onel == inf:
#         print(n)
#         return
#
#     if zerol < onel and oner < zeror:
#         print(n-(oner-oner+1))
#         return
#     if onel < zerol and zeror < oner:
#         print(n-(zeror-zerol+1))
#         return
#     if oner < zerol or onel > zeror:
#         print(n)
#         return
#
#     l = max(zerol, onel)
#     r = min(zeror, oner)
#     print(n-(r-l))

