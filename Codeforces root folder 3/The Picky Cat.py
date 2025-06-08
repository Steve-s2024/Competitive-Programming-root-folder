# lucky, get it first try
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n = int(input())
    nums = [abs(int(e)) for e in input().split()]
    tar = nums[0]
    nums.sort()
    idx = nums.index(tar)
    if idx <= n//2:
        print('Yes')
    else:
        print('No')


t = int(input())
for i in range(t):
    solve()


