# looks intimidating, but if you know the trick its easy
# 50% of the description is misleading information
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n, s = [int(e) for e in input().split()]
    cnt = 0
    for i in range(n):
        dx, dy, xi, yi = [int(e) for e in input().split()]
        if xi == yi and dy*dx == 1: cnt += 1
        elif xi+yi == s and dy*dx == -1: cnt += 1
    print(cnt)

t = int(input())
for i in range(t):
    solve()


