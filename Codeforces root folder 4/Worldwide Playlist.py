# so frustrating omg (not complete)


def solve():
    n, d = map(int, input().split())
    A = [int(x)-1 for x in input().split()]
    B = [int(x)-1 for x in input().split()]

    amp = [0]*n
    for i, v in enumerate(A): amp[v] = i
    bmp = [0]*n
    for i, v in enumerate(B): bmp[v] = i

    lp = 0
    for i in range(1, n):
        a, b = B[i-1], B[i]
        if amp[b] < amp[a]: lp += 1
    print(lp*n + amp[B[-1]]+1 - n)
    print("lp", lp)

    def check(ar):
        return sum(int(i in range(1, n) and amp[B[i-1]] > amp[B[i]]) for i in ar)


    for _ in range(d-1):
        c, x, y = map(int, input().split())
        x, y = x-1, y-1
        i, j = x, y

        l, r = bmp[A[x]], bmp[A[y]]
        if l > r: l, r = r, l
        if abs(l-r) == 1: ar = [l, r, r+1]
        else: ar = [l, l+1, r, r+1]
        lp -= check(ar)

        if c == 1:
            A[i], A[j] = A[j], A[i]
            amp[A[i]] = i
            amp[A[j]] = j
        else:
            l, r = x, y
            B[l], B[r] = B[r], B[l]
            bmp[B[l]] = l
            bmp[B[r]] = r

        lp += check(ar)
        print(lp*n + amp[B[-1]]+1 - n)
        print("lp", lp)
    print(A, B)


solve()
