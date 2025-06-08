# I love u codechef u are the best! able to solve this
# shows how much I improved, the hard work is paid off!!
import heapq, math
from collections import defaultdict, deque

def solve():
    [n, m] = [int(e) for e in input().split(' ')]
    if m < n-1:
        print(0)
    else:
        l, r = 0, n
        res = 0
        while l <= r:
            x = (r+l)//2
            # pretend x as the number of node of all edges weighted 1
            totalCost = n*(n-1)//2 - (n-1-x)*(n-x)//2
            if totalCost <= m:
                res = x
                l = x+1
            else:
                r = x-1
        x = res
        offset = n*(n-1)//2 - (n-1)
        cnt = max(m-offset, 0)-1
        x = min(x, n-1)
        print(x*(x+1)//2 - cnt*(cnt+1)//2)
            

t = int(input())
for tt in range(t):
    solve()