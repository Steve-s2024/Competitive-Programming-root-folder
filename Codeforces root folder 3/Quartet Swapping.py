# no way I can solve this by myself, these div.1
# purple guys can't solve it while it only took them
# 15 minutes to solve C. I give up for now
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    odd, even = [], []
    for i in range(n):
        if i % 2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    odd.sort()
    even.sort()
    res = []
    i1, i2 = 0, 0
    for i in range(n-3):
        if i % 2 == 0:
            res.append(even[i1])
            i1 += 1
        else:
            res.append(odd[i2])
            i2 += 1
    if n % 2 == 0:
        idx1, idx2 = nums.index(odd[-2]), nums.index(odd[-1])
        if idx1 < idx2:
            res.append(odd[-1])
            res.append(even[-1])
            res.append(odd[-2])
        else:
            res.append(odd[-2])
            res.append(even[-1])
            res.append(odd[-1])
    else:
        idx1, idx2 = nums.index(even[-2]), nums.index(even[-1])
        if idx1 < idx2:
            res.append(even[-1])
            res.append(odd[-1])
            res.append(even[-2])
        else:
            res.append(even[-2])
            res.append(odd[-1])
            res.append(even[-1])


    print(' '.join([str(e) for e in res]))

t = int(input())
for i in range(t):
    solve()


