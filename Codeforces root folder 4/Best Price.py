# under process
def solve():
    n, k = [int(e) for e in input().split()]
    arr = [int(e) for e in input().split()]
    brr = [int(e) for e in input().split()]
    arr.sort()
    brr.sort()

    ans = -inf
    for i in range(n):
        # let the price be arr[i]
        a = n-i
        l, r = 0, n-1
        res = n
        while l <= r:
            m = (l+r)//2
            if brr[m] >= arr[i]:
                res = m
                r = m-1
            else: l = m+1
        b = n-res

        # there are b people who can afford the tree, a people who will not leave negative review
        if b-a <= k: ans = max(ans, arr[i]*b)

    for i in range(n):
        # let the price be brr[i]
        b = n-i
        l, r = 0, n-1
        res = n
        while l <= r:
            m = (l+r)//2
            if arr[m] >= brr[i]:
                res = m
                r = m-1
            else: l = m+1
        a = n-res
        # there are b people who can afford the tree, a people who will not leave negative review
        if b - a <= k: ans = max(ans, brr[i] * b)

    print(ans)




t = int(input())
for i in range(t):
    solve()