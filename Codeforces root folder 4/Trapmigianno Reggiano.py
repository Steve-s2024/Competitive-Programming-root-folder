# whoever decide to ban all the recursive DFS solution by run time error should be hanged, son of bitch wasted
# me so many times just to convert the recursive one into iterative one. that mk is really detestable
# though it is good to practice writing iterative post order DFS in different ways. it is much harder than recursive
# DFS I can say.
def solve():
    n, srt, end = [int(e) for e in input().split()]
    srt, end = srt-1, end-1
    g = [[] for _ in range(n)]
    st = [0]*n
    for i in range(n-1):
        u, v = [int(e) for e in input().split()]
        u, v = u-1, v-1
        g[u].append(v)
        g[v].append(u)
    cp = [lst[:] for lst in g]

    q = deque()
    ps = set()

    st[srt] = 1
    stk = [srt]
    while stk:
        u = stk[-1]
        if u == end:
            q = deque(stk[:])
            ps = set(q)
        while g[u] and st[g[u][-1]]: g[u].pop()
        if g[u]:
            v = g[u].pop()
            stk.append(v)
            st[v] = 1
        else: stk.pop()

    g = cp

    st = [0]*n
    ans = []
    def peel(u):
        stk = [u]
        while stk:
            u = stk[-1]
            l = len(stk)
            for v in g[u]:
                if st[v] or v in ps: continue
                st[v] = 1
                stk.append(v)
            if len(stk) == l: # here is the post order stage
                ans.append(u)
                stk.pop()

    while q:
        srt = q.popleft()
        st[srt] = 1
        ps.remove(srt)
        peel(srt)

    print(' '.join(str(e+1) for e in ans))


t = int(input())
for i in range(t): solve()





# bad news that the first submission had a runtime error on the 9th testcase, this is pretty rare.
# holy shit this author is evil for setting testcase that even sys.setrecursionlimit(10**5) can't help
# but, the solution is proven to be correct. I may need to turn it into an iterative DFS
import sys
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10**5)
def solve():
    n, srt, end = [int(e) for e in input().split()]
    srt, end = srt-1, end-1
    g = [[] for _ in range(n)]
    st = [0]*n
    for i in range(n-1):
        u, v = [int(e) for e in input().split()]
        u, v = u-1, v-1
        g[u].append(v)
        g[v].append(u)

    stk = [srt]
    q = deque()
    ps = set()
    def dfs(u):
        nonlocal q, ps
        if u == end:
            q = deque(stk[:])
            ps = set(q)
        for v in g[u]:
            if st[v]: continue
            stk.append(v)
            st[v] = 1
            dfs(v)
            stk.pop()
    st[srt] = 1
    dfs(srt)

    st = [0]*n
    ans = []
    def peel(u):
        for v in g[u]:
            if st[v] or v in ps: continue
            st[v] = 1
            peel(v)
        ans.append(u)

    while q:
        srt = q.popleft()
        st[srt] = 1
        ps.remove(srt)
        peel(srt)

    # print(ans)
    print(' '.join(str(e+1) for e in ans))


t = int(input())
for i in range(t): solve()