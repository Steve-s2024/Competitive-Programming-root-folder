# love this div3!~ Moooooo~~~~
from heapq import heapify, heappush, heappop

def solve():
    n, m = [int(e) for e in input().split()]
    ar, br = [], []
    for _ in range(n):
        x, y = [int(e) for e in input().split()]
        ar.append((x, y))
    for _ in range(m):
        x, y = [int(e) for e in input().split()]
        br.append((x, y))

    mp = [0]*(n+1)
    ar.sort(key = lambda i:-i[1])
    l, r = 0, 0
    hp = []
    sm = 0
    miar = [0]*(n+1)
    msar = [0]*(n+1)
    for i in range(n, -1, -1):
        while r < n and ar[r][1] >= i:
            heappush(hp, ar[r][0])
            sm += ar[r][0]
            r += 1
        if not hp: continue
        while len(hp) > i+1:
            sm -= heappop(hp)
        mp[i] = sm
        miar[i] = hp[0]

        if len(hp) <= i: msar[i] = sm

    pre = [0]*(n+1)
    for i in range(n+1): pre[i] = max(pre[i-1], msar[i])
    pre2 = [0]*(n+1)
    for i in range(n+1): pre2[i] = max(pre2[i-1], mp[i]-miar[i])
    # print(mp)
    mx = max(mp)
    ans = [mx]*m
    i = 0
    # print(msar, miar)

    for x, y in br:
        res = max(pre[y], pre2[y]) + x
        ans[i] = max(ans[i], res)
        i += 1
    # print(ans)

    print(' '.join(str(e) for e in ans))

for _ in range(int(input())): solve()

