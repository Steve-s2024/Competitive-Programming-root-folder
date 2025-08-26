# alright
import sys
from collections import defaultdict, deque, Counter
import cmath, heapq
sys.setrecursionlimit(1 << 20)  # Increase recursion limit for deep trees



def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    nums = [nums[0]] + (sorted(nums[1:-1]) if n > 2 else []) + [nums[-1]]
    cnt = 1
    prev = nums[0]
    flag = True
    i = 0
    # print(nums)
    while i < n-1:
        if prev*2 >= nums[-1]:
            cnt += 1
            break
        tmp = i
        while i < n and prev*2 >= nums[i]:
            i += 1
        i -= 1
        if tmp == i:
            flag = False
            break
        prev = nums[i]
        cnt += 1
    if flag: print(cnt)
    else: print(-1)


t = int(input())
for i in range(t):
    solve()


