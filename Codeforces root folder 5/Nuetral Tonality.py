# Imma actually some kind of genius

def solve():
    n, m = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]


    B.sort()
    j = m-1

    res = []

    for i in range(n):
        while j >= 0 and B[j] >= A[i]:
            res.append(B[j])
            j -= 1

        res.append(A[i])

    while j >= 0:
        res.append(B[j])
        j -= 1



    print(' '.join([str(e) for e in res]))



for _ in range(int(input())): solve()

