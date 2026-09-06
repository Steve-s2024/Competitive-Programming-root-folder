# DP? I thought i filtered constructive algo only...


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    inf = 1<<50
    mk = [0]*n
    z = n-1
    for i in range(n-1, -1, -1):
        if nums[i] == 0: z = i
        else: mk[i] = z


    dp = [[0, 0] for _ in range(n+1)]
    dp[-1][1] = inf
    for i in range(n-1, -1, -1):
        for f in range(2):
            if nums[i]-f < 0:
                dp[i][f] = inf
                continue

            a = dp[i+1][0]+1
            b = dp[i+1][1]
            c = (dp[mk[i]+1][0]+1) if nums[i]-f > 0 else inf
            dp[i][f] = min(a, b, c)

    print(dp[0][0])


    # @cache
    # def fn(i, f):
    #     if i >= n: return 0 if not f else inf
    #     if nums[i]-f < 0: return inf
    #
    #     a = fn(i+1, 0)+1
    #     b = fn(i+1, 1)
    #     c = (fn(mk[i]+1, 0)+1) if nums[i]-f > 0 else inf
    #
    #     return min(a, b, c)
    #
    # print(fn(0, 0))



# for _ in range(int(input())): solve()

solve()
