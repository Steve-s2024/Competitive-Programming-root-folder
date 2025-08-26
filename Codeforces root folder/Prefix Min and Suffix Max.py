# not very easy...
from collections import defaultdict, deque, Counter
import heapq, math
from linecache import cache


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    strarr = [1]
    mxs = [0]*n
    mx = -float('inf')
    for i in range(n-1, -1, -1):
        mx = max(mx, nums[i])
        mxs[i] = mx

    mi = nums[0]
    for i in range(1, n-1):
        x = nums[i]
        if mi > x or mxs[i+1] < x: strarr.append(1)
        else: strarr.append(0)
        mi = min(mi, nums[i])
    strarr.append(1)

    # print(strarr)
    print(''.join(str(e) for e in strarr))



t = int(input())
for i in range(t):
    solve()



