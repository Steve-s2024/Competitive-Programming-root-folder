# quite direct BS solution

def solve():
    s = [int(e) for e in input()]
    n = len(s)
    zar = [0]*n
    for i in range(n): zar[i] = zar[i-1] + s[i]
    oar = [0]*n
    for i in range(n-1, -1, -1): oar[i] = oar[(i+1)%n] + s[i]

    ans = sum(s)
    x = 0
    for i in range(n):
        l, r = i, n-1
        while l <= r:
            m = (l+r)//2
            t1, t2 = zar[m]-zar[i]+(s[i]^1), oar[m+1] if m < n-1 else 0
            ans = min(ans, max(x+t2, t1))
            if t1 > t2+x: r = m-1
            else: l = m+1
        x += s[i]
    print(ans)






for _ in range(int(input())): solve()