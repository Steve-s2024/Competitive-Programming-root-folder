# topo sort... literally topo sort and nothing else


def solve():
    input()
    n, k = [int(e) for e in input().split()]
    g = [[] for _ in range(n)]
    d = [0]*n
    for _ in range(n-1):
        a, b = [int(e)-1 for e in input().split()]
        g[a].append(b)
        g[b].append(a)
        d[a] += 1
        d[b] += 1

    vs = [0]*n
    q = deque()
    for i in range(n):
        if d[i] <= 1:
            vs[i] = 1
            q.append(i)

    x = sum(vs)
    for _ in range(k-1):
        for _ in range(len(q)):
            u = q.popleft()
            for v in g[u]:
                if vs[v]: continue
                d[v] -= 1
                if d[v] <= 1:
                    vs[v] = 1
                    x += 1
                    q.append(v)
        if x == n: break

    print(n-sum(vs))




for _ in range(int(input())): solve()