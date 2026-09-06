# greedy... not so greedy
# work that iter DP



def solve():
    n, s = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    ar = []
    for i in range(n):
        x = nums[i]
        if x <= s: ar.append((0, x))
        else: ar.append((x-s, s))
        # elif s > x//2: # neg only
        #     ar.append((x-s, s))
        # else: # pos only
        #     ar.append((s, x-s))
    ar[0] = [0, nums[0]]
    dp = [{} for _ in range(n)]
    for v in ar[-2]: dp[n-1][v] = nums[-1]*v


    for i in range(n-2, 0, -1):
        a, b = ar[i]
        for v in ar[i-1]:
            dp[i][v] = min(dp[i+1][b] + v*a, dp[i+1][a] + v*b)
    print(dp[1][nums[0]])
    #
    # @cache
    # def fn(i, prv):
    #     if i >= n-1: return nums[i]*prv
    #     a, b = ar[i]
    #     res = min(fn(i+1, b) + prv*a, fn(i+1, a) + prv*b)
    #     return res
    # print(fn(1, nums[0]))



for _ in range(int(input())): solve()