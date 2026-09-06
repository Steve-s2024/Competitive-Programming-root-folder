# my greedy journey (second problem) quite happy to come down on the implementation that is much easier than
# I first imagined. implementation is also about observation making and mantel reasoning
# a simple implementation can beat complex ones by a lot, and it also indicates that the mental model is efficient
# good CPer shows this virtue most clearly (from their tutorial and code)




def solve():
    n, k = list(map(int, input().split()))
    s = input()
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    q = int(input())
    qs = list(map(int, input().split()))
    ar = []
    for x in qs:
        i = bisect_right(l, x)
        a, b = l[i-1], r[i-1]
        a, b = min(x, a+b-x), max(x, a+b-x)
        ar.append((a-1, b-1))

    ar.sort()
    # print(ar)
    res = list(s)
    for i in range(len(ar)):
        L, R = ar[i]
        if L == -1: continue
        while L < R:
            if i < len(ar)-1 and ar[i+1][0] <= L:
                ar[i+1] = [-1, -1]
                break
            res[L], res[R] = res[R], res[L]
            L, R = L+1, R-1
    print(''.join(res))

for _ in range(int(input())): solve()



