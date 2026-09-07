# so annoying that I misread the question definition of child node and wasted time and energy to solve an impossible problem
def solve():
    n = int(input())
    P = [int(e) for e in input().split()]

    g = [[] for _ in range(n)]
    for i in range(n-1): g[P[i]-1].append(i)

    ar = [1]
    for e in g:
        if len(e): ar.append(len(e))

    ar.sort()
    tp = []
    for i, v in enumerate(ar):
        if v-i-1 > 0: tp.append(v-i-1)

    if not tp:
        print(len(ar))
        return
    l, r = 0, max(tp)

    res = -1
    while l <= r:
        m = (l+r)//2
        x = sum([max(0, tp[i]-m) for i in range(len(tp))])
        if x <= m:
            res = m
            r = m-1
        else: l = m+1


    print(len(ar)+res)


for _ in range(int(input())): solve()