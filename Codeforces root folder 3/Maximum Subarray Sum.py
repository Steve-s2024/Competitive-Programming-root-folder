# don't know why it is not working...

from collections import defaultdict, deque, Counter
import heapq, math
import sys



def solve():
    n, k = [int(e) for e in input().split()]
    s = input()
    nums = [int(e) for e in input().split()]

    idx = -1
    for i in range(n):
        if s[i] == '0':
            idx = i
            nums[i] = -10**18

    if idx == -1:
        dp = [nums[0]]
        for i in range(1, n):
            tot = nums[i]
            if dp[i - 1] > 0:
                tot += dp[i - 1]
            dp.append(tot)
        mx = max(dp)
        if mx == k:
            print('Yes')
            print(' '.join([str(e) for e in nums]))
        else:
            print('No')
    else:
        l, r = -10*18, 10**18
        flag = False
        while l <= r:
            m = (l+r)//2
            nums[idx] = m
            dp = [nums[0]]
            for i in range(1, n):
                tot = nums[i]
                if dp[i-1] > 0:
                    tot += dp[i-1]
                dp.append(tot)
            mx = max(dp)
            if mx == k:
                flag = True
                break
            if mx > k:
                r = m-1
            else:
                l = m+1
        if flag:
            print('Yes')
            print(' '.join([str(e) for e in nums]))
        else:
            print('No')



t = int(input())
for i in range(t):
    solve()
