# no motiv to do the iterative since this is accepted


def solve():
    n, k = [int(e) for e in input().split()]
    cl = n*(n-1)//2 - k

    # print(cl)


    @cache
    def fn(i, t):
        if i >= n: return t == cl

        j = 1
        res = False
        while i+j <= n:
            if t + j*(j-1)//2 > cl: break
            res = res or fn(i+j, t + j*(j-1)//2)
            j += 1

        return res

    fn(0, 0)


    if not fn(0, 0):
        print(0)
        return



    i = 0
    t = 0
    ar = []
    x = n
    while i < n:
        for j in range(1, n+1):
            if fn(i+j, t+j*(j-1)//2):
                for k in range(j):
                    ar.append(x-j+k+1)

                i, t = i+j, t+j*(j-1)//2
                x -= j
                break
    print(' '.join(str(e) for e in ar))

for _ in range(int(input())): solve()
