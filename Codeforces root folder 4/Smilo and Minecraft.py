# too easy



def helper(g, k):
    n, m = len(g), len(g[0])
    ct = 0
    mat = [[0] * m for _ in range(n)]
    cp = [[0]*m for _ in range(n)]
    k -= 1
    for i in range(n):
        for j in range(m):
            a = mat[i - 1][j] if i else 0
            b = mat[i][j - 1] if j else 0
            c = mat[i - 1][j - 1] if i and j else 0
            mat[i][j] = a + b - c
            if g[i][j] == 'g':
                mat[i][j] += 1
                ct += 1


    # for r in mat: print(r)
    # print(ct)


    mi = 1 << 60
    for i in range(k, n):
        for j in range(k, m):
            x, y = i - k, j - k
            if g[x][y] != '.': continue

            l = 2 * k + 1
            a = mat[i - l][j] if i - l >= 0 else 0
            b = mat[i][j - l] if j - l >= 0 else 0
            c = mat[i - l][j - l] if i - l >= 0 and j - l >= 0 else 0
            res = mat[i][j] + (-a - b + c)

            mi = min(mi, res)

    return ct - mi


def solve():
    n, m, k = [int(x) for x in input().split()]
    g = []
    for _ in range(n):
        g.append(list(input()))

    nn, nm = n+k-1, m+k-1
    ng = [['.']*nm for _ in range(nn)]
    for i in range(n):
        for j in range(m): ng[i][j] = g[i][j]
    # for r in ng: print(r)

    res = helper(ng, k)

    print(res)
for _ in range(int(input())): solve()