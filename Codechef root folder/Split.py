# super fast brain, love this feeling so high~~

def solve():
    n, k = [int(e) for e in input().split()]
    s = input()
    l, r = 1, n
    res = 1
    while l <= r:
        m = (l+r)//2
        cnt = 0
        zero, one = 0, 0
        mx = 0
        for i in range(n):
            if s[i] == '1':
                one += 1
                mx += 1
            else:
                zero += 1
                mx = max(mx, zero)
            if mx >= m:
                cnt += 1
                mx = 0
                zero = 0
                one = 0
        if cnt >= k:
            res = m
            l = m+1
        else: r = m-1
    print(res)



t = int(input())
for i in range(t):
    solve()
