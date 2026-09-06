#
def solve():
    s = input()
    t = input()
    n, m = len(s), len(t)

    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): dp[i][m] = -1
    for j in range(m): dp[n][j] = 0

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            dp[i][j] = dp[i+1][j+1] if s[i] == t[j] else dp[i+1][j]
            dp[i][j] += 1

    print(sum(dp[i][0] for i in range(n)))
    #
    # @cache
    # def fn(i, j):
    #     if j == m: return -1
    #     if i >= n: return 0
    #     ct = fn(i+1, j+1) if s[i] == t[j] else fn(i+1, j)
    #     return ct+1
    # # for i in range(n): print(fn(i, 0))
    # ans = sum(fn(i, 0) for i in range(n))
    # print(ans)
solve()