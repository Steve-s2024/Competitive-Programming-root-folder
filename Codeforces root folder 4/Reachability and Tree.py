# damn light weight babyeah~ second 1700 problem solved. I can feel my brain growing
from collections import defaultdict, deque, Counter


def solve():
    n = int(input())
    f = [0]*n
    g = [[] for _ in range(n)]
    for i in range(n-1):
        u, v = [int(e) for e in input().split()]
        u, v = u-1, v-1
        f[u] += 1
        f[v] += 1
        g[u].append(v)
        g[v].append(u)

    if 2 not in f:
        print('No')
        return

    st = [0]*n
    nde = f.index(2)
    a, b = g[nde]
    st[nde] = st[a] = st[b] = 1
    ans = [[a, nde], [nde, b]]


    q = deque([a])
    cnt = 0
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            for v in g[u]:
                if st[v]: continue
                st[v] = 1
                q.append(v)
                if cnt%2 == 0: ans.append((u, v))
                else: ans.append((v, u))
        cnt += 1

    q = deque([b])
    cnt = 0
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            for v in g[u]:
                if st[v]: continue
                st[v] = 1
                q.append(v)
                if cnt % 2 == 0: ans.append((v, u))
                else: ans.append((u, v))
        cnt += 1


    print('Yes')
    for u, v in ans: print(f'{u+1} {v+1}')

t = int(input())
for i in range(t): solve()