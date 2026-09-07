# first ever atcoder regular contest problem
# not easy for sure and this is just the first problem (would be an ABC fourth problem)

def solve():
    n, W = [int(e) for e in input().split()]
    ar = []
    for _ in range(n): ar.append([int(e) for e in input().split()])
    ans = 0
    tt = 0
    pre = [0]*n
    for i in range(n): pre[i] = pre[i-1] + ar[i][1]
    for i in range(n-1, -1, -1):
        w, v = ar[i]
        if w <= W:
            ans = max(ans, (pre[i-1] if i else 0)+tt)
            tt += v
            W -= w
    print(max(ans, tt))




for _ in range(int(input())): solve()