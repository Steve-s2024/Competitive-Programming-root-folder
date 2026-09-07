# first 1900 construct algo, pretty tough ngl

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    if A == B:
        print('Yes')
        return

    xor = 0
    for e in A: xor ^= e
    for e in B: xor ^= e
    # print(xor)
    if xor not in A or xor not in B:
        print('No')
        return
    # print(A, xor)
    f = 0
    for i in range(n):
        if A[i] == xor and not f:
            f = 1
            continue
        A[i] ^= xor

    # print(A, B)
    A.sort()
    B.sort()
    print('Yes' if A == B else 'No')


for _ in range(int(input())): solve()