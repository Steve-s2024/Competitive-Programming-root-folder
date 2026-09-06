# i think the query only used n...



def query(u, v):
    print(f'? {u} {v}')
    stdout.flush()
    res = int(input())
    if res == -1: exit()
    return res


def solve():
    n = int(input())
    u = 1
    v = -1
    for i in range(2, n):
        if not query(u, i):
            v = i
            break

    ar = [(u, v)]
    for i in range(u, v): ar.append((0, i))

    v = v+1
    u = 2
    while len(ar) < n-1:
        if not query(u, v):
            ar.append((u, v))
            v += 1
            u += 1
        else: u += 1
    # print(ar)
    g = [0]*n
    for u, v in ar: g[v] = u

    print('! ' + ' '.join(str(e) for e in g[1:]))


for _ in range(int(input())): solve()
