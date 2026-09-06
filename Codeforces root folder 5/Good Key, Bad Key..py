# tag says greedy, but not really. its more like log trick


def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]

    dp = [[0]*31 for _ in range(n+1)]


    for i in range(30+1): dp[n][i] = 0
    for i in range(n-1, -1, -1):
        for x in range(30+1):
            dp[i][x] = max(0, dp[i+1][x] + nums[i]//(1<<x) -k)
            if x < 30: dp[i][x] = max(dp[i][x], dp[i+1][x+1] + nums[i]//(1<<(x+1)))

    print(dp[0][0])
    #
    # @cache
    # def fn(i, x):
    #     if i >= n: return 0
    #     a = fn(i+1, x) + nums[i]//(1<<x) -k
    #     res = max(0, a)
    #     if x < 30: res = max(res, fn(i+1, x+1) + nums[i]//(1<<(x+1)))
    #     return res
    # print(fn(0, 0))



for _ in range(int(input())): solve()