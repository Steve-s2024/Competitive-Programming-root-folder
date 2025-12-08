# another problem that forbid recursive DFS. fortunately the iterative version is very easy to write, unlike in
# some cases where there's a loop in the function body, then its disaster to do iterative DFS.

# the solution constructed parent array, used BFS (for enumerate each depth) and topological sort (as to prune the lower branches).


def solve():
    n = int(input())
    g = [[] for _ in range(n)]
    d = [0]*n
    for i in range(n-1):
        u, v = [int(e) for e in input().split()]
        u, v = u-1, v-1
        g[u].append(v)
        g[v].append(u)
        d[u] += 1
        d[v] += 1
    p = [0] * n
    p[0] = -1
    vis = [0] * n
    vis[0] = 1
    stk = [0]
    while stk:
        u = stk.pop()
        for v in g[u]:
            if vis[v]: continue
            vis[v] = 1
            p[v] = u
            stk.append(v)

    # def dfs(u):
    #     for v in g[u]:
    #         if vis[v]: continue
    #         vis[v] = 1
    #         p[v] = u
    #         dfs(v)
    # vis[0] = 1
    # dfs(0)

    vis = [0] * n
    vis[0] = 1

    res = n-1
    q = deque([0])
    tt, ct = 1, 0
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            if u != 0 and d[u] == 1:
                while u != 0 and d[u] == 1:
                    d[u] -= 1
                    d[p[u]] -= 1
                    u = p[u]
                    ct += 1
                continue

            for v in g[u]:
                if vis[v]: continue
                vis[v] = 1
                q.append(v)
                tt += 1

        res = min(res, n-tt + ct)
    print(res)


t = int(input())
for i in range(t): solve()
