# O(n^2) without even deque, thankfully passed...
def solve():
    n, c = [int(e) for e in input().split()]
    c -= 1
    g = []
    for _ in range(n): g.append(input())

    mp = [0]*n
    for i in range(n):
        for j in range(n):
            if g[i][j] == '#': mp[j] = max(i, mp[j])


    col = [0]*n
    cr = [0]*n
    cr[c] = 1
    for i in range(n-2, -1, -1):
        tmp = [0]*n
        for j in range(n):
            f = 0
            for c in [j-1, j, j+1]:
                if c in range(n) and cr[c]: f = 1
            if f and (g[i][j] == '.' or mp[j] == i or col[j]):
                if tmp[j]: continue
                tmp[j] = 1
                if mp[j] <= i: col[j] = 1
        cr = tmp
    print(''.join(str(e) for e in cr))




# a working solution, TLE for no reason. it is O(n^2), and with no hashing overhead.

from collections import defaultdict, deque, Counter
def solve():
    n, c = [int(e) for e in input().split()]
    c -= 1
    g = []
    for _ in range(n): g.append(input())

    mp = [0]*n
    for i in range(n):
        for j in range(n):
            if g[i][j] == '#': mp[j] = max(i, mp[j])


    res = [0]*n
    col = [0]*n
    q = deque([(n-1, c)])
    while q:
        r, c = q.popleft()
        if r == 0: res[c] = 1
        if mp[c] <= r: col[c] = 1
        vs = [0] * n
        for R, C in ((r-1, c-1), (r-1, c), (r-1, c+1)):
            if R in range(n) and C in range(n) and (g[R][C] == '.' or mp[C] == R or col[C]):
                if vs[C]: continue
                vs[C] = 1
                q.appendleft((R, C))

    # print(col)
    print(''.join(str(e) for e in res))
