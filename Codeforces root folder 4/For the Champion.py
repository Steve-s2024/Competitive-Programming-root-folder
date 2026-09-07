# not really enjoyable
from sys import stdout

def query(d, v):
    print(f'? {d} {v}')
    stdout.flush()
    res = int(input())
    if res == -1: exit(4399)
    return res

def solve():
    n = int(input())
    inf = 1<<60
    v = 10**9
    mi = inf
    mi2 = inf
    for _ in range(n):
        x, y = [int(x) for x in input().split()]
        mi = min(y+x, mi)
        mi2 = min(x-y, mi2)

    query('D', v)
    query('D', v)
    query('L', v)
    res = query('L', v)
    xpy = 4*v + mi - res

    query('U', v)
    query('U', v)
    query('U', v)
    res = query('U', v)
    xmy = 4*v + mi2-res

    x = xpy + xmy
    x //= 2
    y = xpy - x
    print(f'! {x} {y}')

for _ in range(int(input())): solve()