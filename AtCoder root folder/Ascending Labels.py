# maxheap propagation, magically fits the description requirement



def solve():
    n, m = [int(x) for x in input().split()]
    if n == 1:
        print(0)
        return

    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        u, v = u-1, v-1
        g[u].append(v)
        g[v].append(u)

    vs = [0]*n
    mk = [-1]*n
    mk[0] = 0

    hp = [[0, 0]]
    while hp:
        c, u = heappop(hp)
        if vs[u]: continue
        vs[u] = 1
        c = -c
        mk[u] = c

        for v in g[u]:
            heappush(hp, (-(c+1), v))


    print(' '.join(map(str, mk)))


for _ in range(int(input())): solve()