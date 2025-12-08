# under progress

def solve():
    n, m, k = [int(e) for e in input().split()]
    g = []
    for i in range(n): g.append([int(e) for e in input().split()])
    t = []
    for i in range(n): t.append(input())

    pre = [[0]*m for _ in range(n)]
    for j in range(m-1, -1, -1): pre[-1][j] = pre[-1][(j+1)%m] + int(t[-1][j])

    for i in range(n-2, -1, -1):
        for j in range(m-1, -1, -1): pre[i][j] = pre[i][(j+1)%m] + int(t[i][j])
        for j in range(m-1, -1, -1): pre[i][j] += pre[i+1][j]

    st = set()
    for i in range(n-k+1):
        for j in range(m-k+1):
            a = pre[i][j]
            b = pre[i+k][j] if i+k < n else 0
            c = pre[i][j+k] if j+k < m else 0
            d = pre[i+k][j+k] if i+k < n and j+k < m else 0
            gap = abs(2*(a-b-c+d) - k*k)
            st.add(gap)

    a, b = 0, 0
    for i in range(n):
        for j in range(m):
            if t[i][j] == '1': a += g[i][j]
            else: b += g[i][j]

    dif = abs(a-b)
    print(dif, st)

t = int(input())
for i in range(t): solve()