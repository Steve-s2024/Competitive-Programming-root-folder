# good brain teaser! hard but doable.

from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n = int(input())
    nums = [int(e) for e in input().split(' ')]
    if n == 1:
        print(1)
        return
    res = 1
    prev = nums[1] - nums[0]
    for i in range(1, n):
        diff = nums[i] - nums[i-1]
        if diff != 0:
            if prev < 0 and diff > 0:
                res += 1
            prev = diff
    print(res)


t = int(input())
for tt in range(t):
    solve()

