# execute the problem writer as he committed homicide to my brain
# easily the worst contest ever
# round 1085 div1+2. 2026-03-08
# by the way i spent 2 hours on B and only able to solve A, B

from collections import defaultdict, deque, Counter
from heapq import heapify, heappush, heappop


def solve():
    n, m, l = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]

    m = min(m, n+1)
    prv, hp, mp = 0, [0]*m, defaultdict(int)
    mp[0], mx = m, 0
    for i in range(n):
        dif = nums[i]-prv
        while dif:
            e = heappop(hp)
            if mp[e] == 0: continue
            mx, mp[e+1], mp[e] = max(mx, e+1), mp[e+1]+1, mp[e]-1
            heappush(hp, e+1)
            dif -= 1

        while mp[mx] == 0: mx -= 1
        mp[mx] -= 1
        if n-i >= m:
            mp[0] += 1
            heappush(hp, 0)

        while mp[mx] == 0: mx -= 1
        prv = nums[i]

    mx = 0
    for k, v in mp.items():
        if v: mx = max(mx, k)

    print(mx+l-nums[-1])


for _ in range(int(input())): solve()

