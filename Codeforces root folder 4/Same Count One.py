# greedy leads the way, I can feel greedy blood run through my veins


def solve():
    n, m = [int(e) for e in input().split()]
    g = []
    for _ in range(n): g.append([int(e) for e in input().split()])
    SM = sum(sum(g[i]) for i in range(n))
    if SM%n != 0:
        print(-1)
        return
    x = SM//n
    mp = [[] for _ in range(m)]
    cmp = [0]*n
    for i in range(n):
        sm = sum(g[i])
        cmp[i] = sm
        if sm < x:
            for j in range(m):
                if g[i][j] == 0: mp[j].append(i)
    # print(x)
    res = []
    for i in range(n):
        if cmp[i] <= x: continue
        for j in range(m):
            if not g[i][j]: continue

            while mp[j] and cmp[mp[j][-1]] == x: mp[j].pop()
            if mp[j]:
                t = mp[j].pop()
                res.append((i, t, j))
                cmp[i] -= 1
                cmp[t] += 1
                if cmp[i] <= x: break
    # print(cmp)
    print(len(res))
    for u, v, w in res: print(u+1, v+1, w+1)
    # for u, v, w in res:
    #     g[u][w], g[v][w] = g[v][w], g[u][w]
    # for r in g: print(r)


for _ in range(int(input())): solve()