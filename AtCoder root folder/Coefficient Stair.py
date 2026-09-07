# seems impossible, but actually kindda neat problem with a small twist


def solve():
    n, k = [int(e) for e in input().split()]

    stk = []
    res = [[] for _ in range(k+1)]
    def fn(i, x):
        if i >= n-1:
            # print(i, x)
            res[k-x].append([k-x] + stk)
            return

        for j in range(k):
            if x+(i+2)*j > k: break
            stk.append(j)
            fn(i+1, x+(i+2)*j)
            stk.pop()


    fn(0, 0)
    # print(res)
    for ar in res:
        for a in ar: print(' '.join(str(e) for e in a))




solve()


