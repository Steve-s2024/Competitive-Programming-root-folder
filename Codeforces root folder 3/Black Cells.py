# boring binary search implementation
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    if n%2 == 0:
        maxDiff = 0
        for i in range(0, n-1, 2):
            diff = nums[i+1] - nums[i]
            maxDiff = max(maxDiff, diff)
        print(maxDiff)
    else:
        l, r = 1, 10**18
        ans = -1
        while l <= r:
            m = (l+r)//2
            res = 1
            flag = 1
            i = 0
            while i < n-1:
                diff = nums[i+1] - nums[i]
                if diff > m:
                    if flag:
                        i-=1
                        flag = 0
                    else:
                        res = 0
                        break
                i += 2
            if res:
                ans = m
                r = m-1
            else:
                l = m+1
        print(ans)

t = int(input())
for i in range(t):
    solve()


