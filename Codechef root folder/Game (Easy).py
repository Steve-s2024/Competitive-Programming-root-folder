# finally... it is so annoying to mix things up like this
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    nums.sort(reverse = True)
    strarr = []
    pre = [0]
    for i in range(n): pre.append(pre[i] + nums[i])
    pre = pre[1:]
    pre += [pre[-1]]*n
    # print(pre)

    for coin in range(1, 2*n+1):
        tot = pre[coin-1]
        # pretend m is the number of nums[i] to collect
        # so, coin - m is the number of x to collect
        for m in range(min(coin, n)+1):
            re = coin - m
            if re > m: continue
            cur = pre[m-1]
            extra = m-re
            curTot = cur + ( m*(m-1)//2 - extra*(extra-1)//2 )
            tot = max(tot, curTot)
        strarr.append(str(tot))

    # print(strarr)
    print(' '.join(strarr))




#TLE
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    strarr = []
    for coin in range(1, 2*n+1):
        dp = {}
        def recursive(i, c, x):
            state = (i, c, x)
            if state in dp: return dp[state]
            nonlocal n
            if c < 0: return -inf
            if i >= n: return 0
            a, b = nums[i], x
            res = max(
                recursive(i + 1, c, x),
                recursive(i + 1, c - 1, x+1) + a,
                recursive(i + 1, c - 2, x+1) + a + b
            )
            dp[state] = res
            return res
        strarr.append(str(recursive(0, coin, 0)))

    # print(strarr)
    print(' '.join(strarr))

