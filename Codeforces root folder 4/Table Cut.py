# to ez
def solve():
    n, m = [int(e) for e in input().split()]
    g = []
    for _ in range(n): g.append([int(e) for e in input().split()])

    ct = sum(sum(g[i]) for i in range(n))
    x = ct//2


    res = []
    j = 0
    for i in range(n):
        sm = sum(g[i][j:]) if j < m else 0
        while j < m and sm > x:
            res.append('R')
            sm -= g[i][j]
            j += 1
        x -= sm
        res.append('D')
    while len(res) < n+m: res.append('R')
    print(ct//2*((ct+1)//2))
    print(''.join(res))



for _ in range(int(input())): solve()