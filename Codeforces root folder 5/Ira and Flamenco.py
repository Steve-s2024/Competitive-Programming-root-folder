# this is no Construct algo, just combinatorics. what tagging is this??



def solve():
    M = 10**9 + 7
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]

    nums.sort()
    ar = []
    prv, x = -1, 0

    for e in nums:
        if e != prv:
            ar.append((prv, x))
            prv, x = e, 1
        else: x += 1

    ar.append((nums[-1], x))
    ar.pop(0)



    if len(ar) < m:
        print(0)
        return


    res = 1
    for i in range(m): res = (res*ar[i][1])%M
    # print(ar)
    # print(res)
    ans = 0
    for i in range(m-1, len(ar)):
        # print(ar[i], res)
        a, b = ar[i-(m-1)], ar[i]
        if b[0]-a[0] == m-1: ans = (ans+res)%M
        if i == len(ar)-1: break
        res = (res*pow(a[1], M-2, M))%M
        res = (res * ar[i+1][1])%M

    print(ans)






for _ in range(int(input())): solve()

