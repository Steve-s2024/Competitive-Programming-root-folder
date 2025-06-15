# Q3 solved, this could be my best codechef contest so far
import sys
import heapq, math
from collections import defaultdict, deque, Counter

def solve():
    n, x = [int(e) for e in input().split()]
    dog = [int(e) for e in input().split()]
    par = [int(e) for e in input().split()]

    l, r = 0, n
    res = 0
    while l <= r:
        m = (l+r)//2
        # pretend m is the number of parries
        skill = x-m
        cnt = 0
        flag = True
        for i in range(n-1, -1, -1):
            if par[i] <= skill+1:
                skill+=1
                cnt+=1
            elif dog[i] > skill:
                flag = False
                break
        if flag and cnt >= m:
            res = m
            l = m+1
        else:
            r = m-1
    print(res)


t = int(input())
for i in range(t):
    solve()