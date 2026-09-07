# this is not easy



def solve():
    n = int(input())
    g = []
    for _ in range(n): g.append([int(e) for e in list(input())])

    ar = []
    for v in range(n):
        for u in range(n):
            if v == u:
                if not g[v][u]:
                    print('No')
                    return
                continue

            if not g[v][u]: continue

            for w in range(n):
                if w in [v, u]: continue
                if g[v][w] and g[w][u]: break
            else: ar.append((v, u))

    if len(ar) != n-1:
        print('No')
        return


    # print(ar)
    V = [[] for _ in range(n)]

    vs = [0]*n
    for u, v in ar:
        V[u].append(v)
        V[v].append(u)
    q = deque([(0, -1)])
    while q:
        u, p = q.popleft()
        if vs[u]:
            print('No')
            return

        vs[u] = 1
        for v in V[u]:
            if v == p: continue
            q.append((v, u))


    if sum(vs) != n:
        print('No')
        return



    V = [[] for _ in range(n)]
    for u, v in ar: V[u].append(v)

    def dfs(u):
        tp[u] = 1
        for v in V[u]: dfs(v)

    for v in range(n):
        tp = [0]*n
        dfs(v)

        for i in range(n):
            if g[v][i] != tp[i]:
                print('No')
                return

    print('Yes')
    for u, v in ar: print(u+1, v+1)



for _ in range(int(input())): solve()

