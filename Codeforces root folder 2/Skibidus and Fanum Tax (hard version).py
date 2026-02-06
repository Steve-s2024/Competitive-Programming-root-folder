# medium level, it's actually easier than some of the 1200 I've done
# not hard to discover the greedy solution here
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n, M = [int(e) for e in input().split()]
    arr = [int(e) for e in input().split()]
    brr = [int(e) for e in input().split()]
    brr.sort()
    flag = True
    prev = -float('inf')
    for i in range(n):
        l, r = 0, M-1
        idx = -1
        while l <= r:
            m = (r+l)//2
            # print('binary search', prev, brr[m], arr[i])
            if prev <= brr[m] - arr[i]:
                idx = m
                r = m-1
            else:
                l = m+1
        # print(i, prev, idx)
        if idx != -1:
            if arr[i] >= prev:
                arr[i] = min(arr[i], brr[l]-arr[i])
            else:
                arr[i] = brr[idx]-arr[i]
        elif arr[i] < prev:
            flag = False
            break
        prev = arr[i]
    # print(arr)
    if flag:
        print('Yes')
    else:
        print('No')



t = int(input())
for tt in range(t):
    solve()