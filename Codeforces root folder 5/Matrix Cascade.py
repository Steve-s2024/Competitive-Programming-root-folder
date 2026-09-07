# i've implemented a pretty wild imagination, wow nice one



def solve():
    n = int(input())
    g = []
    for _ in range(n):
        g.append([int(e) for e in list(input())])

    m = 2*n-1
    ar = [0]*m
    ar2 = [0]*(m+1)
    res = 0
    for i in range(n):
        pre = [0]*m
        pre2 = [0]*(m+1)
        for j in range(m):
            pre[j] = pre[j-1] ^ ar[j]
            pre2[j] = pre2[j-1] ^ ar2[j]

        for j in range(n):
            e = g[i][j]
            k = i+j
            k2 = n-i-1 + j
            e ^= pre[k]
            e ^= pre2[k2]
            if e:
                # print(i, j, pre[k], pre2[k2])
                ar[k] ^= 1
                ar2[k2+1] ^= 1
                res += 1

    print(res)






for _ in range(int(input())): solve()

