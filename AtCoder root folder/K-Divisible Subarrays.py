# this is just simple for an ABC E (D >> E) for sure


def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]

    # sentinel value
    nums = [0]+nums
    n += 1


    pre = [0]*n
    for i in range(n): pre[i] = (pre[i-1] + nums[i])%k
    mp = {}
    mk = [-1]*n
    for i in range(n-1, -1, -1):
        e = pre[i]
        if e in mp: mk[i] = mp[e]
        mp[e] = i

    dp = [0]*(n+1)
    for i in range(n-1, -1, -1):
        res = dp[i+1]
        if mk[i] != -1:
            a = dp[mk[i]] + 1
            res = max(res, a)
        dp[i] = res

    res = dp[0]
    print(res)


    #
    # @cache
    # def fn(i):
    #     if i >= n: return 0
    #
    #     res = fn(i+1)
    #     if mk[i] != -1:
    #         a = fn(mk[i]) + 1
    #         res = max(res, a)
    #     return res


    # res = fn(0)
    # print(res)


solve()




