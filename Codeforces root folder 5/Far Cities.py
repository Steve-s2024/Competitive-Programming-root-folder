# I could've squashed it in contest... so sad

def query(u, v, d):
    print(f'? {u} {v} {d}')
    stdout.flush()
    res = int(input())
    if res == -1: exit(4399)
    return res



def solve():
    n = int(input())
    u, v, d = 1, 2, 1
    res = (u, v, d)
    while v <= n:
        while query(u, v, d):
            res = (u, v, d)
            d += 1
        v += 1

    u, v, d = res[1], 1, res[2]
    while v <= n:
        if u == v:
            v += 1
            continue
        while query(u, v, d):
            res = (u, v, d)
            d += 1
        v += 1

    u, v, d = res
    print(f'! {u} {v} {d}')



for _ in range(int(input())): solve()




# this should be working... same as the B2 why is it not working??

def query(u, v, d):
    print(f'? {u} {v} {d}')
    stdout.flush()
    res = int(input())
    if res == -1: exit(4399)
    return res

def solve():
    n = int(input())
    u, v = 1, 2
    f = 1
    d = 1
    while f:
        d += 1
        f = query(u, v, d)
    d -= 1

    w = 3
    while w <= n:
        d += 1
        a, b = query(u, w, d), query(v, w, d)
        if a: v = w
        elif b: u = w
        else:
            d -= 1
            w += 1


    print(f'! {u} {v} {d}')


for _ in range(int(input())): solve()
