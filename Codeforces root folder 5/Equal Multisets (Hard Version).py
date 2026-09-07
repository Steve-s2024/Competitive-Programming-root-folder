# this is not easy, got me really worried



def solve():
    n, k = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]

    ar = [-1]*n
    for i in range(k):
        f = 0
        for j in range(i, n-k, k):
            a, b = A[j], A[j+k]
            if a != b:
                if ar[j] not in [-1, a]:
                    print('No')
                    return
                ar[j], ar[j+k] = a, b

                if not f:
                    f = 1
                    for I in range(j-k, -1, -k): ar[I] = a
            else: ar[j+k] = ar[j]

        if not f:
            x = -1
            for j in range(i, n, k):
                if B[j] != -1: x = B[j]
            for j in range(i, n, k): ar[j] = x



    # print(ar)

    for i in range(n):
        a, b = B[i], ar[i]
        if -1 not in [a, b] and a != b:
            print('No')
            return
        if a == -1 and b != -1: B[i] = b


    frq = [0]*(n+1)
    for i in range(k):
        frq[A[i]] += 1
        if B[i] == -1: continue
        frq[B[i]] -= 1

    for e in frq:
        if e < 0:
            print('No')
            return


    print('Yes')


for _ in range(int(input())): solve()

