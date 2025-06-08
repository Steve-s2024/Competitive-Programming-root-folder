# I gambled, it worked
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    flag = True
    for i in range(1, n):
        a, b = nums[i-1], nums[i]
        if a == b == 0:
            flag = False
            break

    if flag and Counter(nums)[1] != n:
        print('No')
    else:
        print('Yes')


t = int(input())
for i in range(t):
    solve()


