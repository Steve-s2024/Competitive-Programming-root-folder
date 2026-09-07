# eureka! said while reading the solution


def solve():
    n = int(input())
    P = [int(x) for x in input().split()]
    I = P.index(n)

    ar = []
    for i in range(I, 0, -2):
        ar.append((P[i], i))

    for i in range(I+2, n-1, 2):
        ar.append((P[i], i))

    ar.sort()
    x = n
    Q = [0]*n
    for i in range(len(ar)):
        _, j = ar[i]
        Q[j] = x
        x -= 1

    # print(Q)

    if Q[I] == 0:
        Q[I] = x
        x -= 1


    ar = []
    for i in range(n):
        if Q[i] == 0: ar.append((P[i], i))
    ar.sort()
    for i in range(len(ar)):
        _, j = ar[i]
        Q[j] = x
        x -= 1


    print(' '.join(str(e) for e in Q))
    # res = [P[i]+Q[i] for i in range(n)]
    # print(res)


for _ in range(int(input())): solve()