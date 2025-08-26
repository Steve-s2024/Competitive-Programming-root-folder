# can't solve Q2, thought I gonna get fked, but still solved Q3. this is a good problem

def solve():
    n, m = [int(e) for e in input().split()]
    arr = [int(e) for e in input().split()]
    brr = [int(e) for e in input().split()]
    one = []
    zero = []
    cnt = 0
    res = n
    for i in range(n):
        if i < m and brr[i] == 1: one.append(i)
        elif i < m and brr[i] == 0: zero.append(i)
        if arr[i] == 1:
            if one and one[-1] >= i-cnt:
                res -= 1
                cnt += 1
        else:
            if zero and zero[-1] >= i-cnt:
                res -= 1
                cnt += 1

    print(res)

t = int(input())
for i in range(t):
    solve()