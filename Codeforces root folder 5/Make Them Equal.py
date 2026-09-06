# em, not easy but I am gaining fast!
mx = 1000
dp = [1 << 30] * (mx + 1)
dp[1] = 0
dp[0] = -1
for i in range(1, mx + 1):
    for j in range(1, mx + 1):
        x = i + i // j
        if x > mx: continue
        dp[x] = min(dp[x], dp[i] + 1)
mp = dp


def solve():
    n, k = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]
    C = [int(e) for e in input().split()]

    t = sum(mp[B[i]] for i in range(n))
    t = min(t+1, k+1)

    dp = [[0]*t for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(t):
            dp[i][j] = dp[i+1][j]
            if j+mp[B[i]] < t: dp[i][j] = max(dp[i][j], dp[i+1][j+mp[B[i]]] + C[i])


    print(dp[0][0])

for _ in range(int(input())): solve()

