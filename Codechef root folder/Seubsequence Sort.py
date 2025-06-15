# first time in top 100 in a div2 codechef contest.
import sys
import heapq, math
from collections import defaultdict, deque, Counter

def solve():
    n = int(input())
    arr = [int(e) for e in input().split()]

    res = 0
    for i in range(1, n):
        a, b = arr[i-1], arr[i]
        cnt = 0
        if b < a:
            while b < a:
                b |= 1<<cnt
                cnt+=1
            res = max(res, 1<<(cnt-1))
            arr[i] = b
    print(res)




t = int(input())
for i in range(t):
    solve()