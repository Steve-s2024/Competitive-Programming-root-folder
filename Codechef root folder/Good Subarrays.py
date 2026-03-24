# 2026-02-18 E

# two minutes before the contest ends, I all killed!!!
# history made today: first codechef all kill. first non-leetcode all kill, first time solved 5 problems in a
# div2 codechef round.

# final rank 127

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    stk = []
    ar = [-1]*n
    for i in range(n):
        while stk and stk[-1][0] < nums[i]:
            _, j = stk.pop()
            ar[j] = i
        stk.append((nums[i], i))

    # print(ar)

    dp = [1]*n
    ans = 0
    for i in range(n-1, -1, -1):
        j = ar[i]
        if j == -1: dp[i] = n-i
        elif nums[j]-nums[i] == 1: dp[i] = j-i + dp[j]
        else: dp[i] = max(dp[i], j-i)
        if nums[i] == 1: ans += dp[i]
    # print(dp)
    print(ans)



for _ in range(int(input())): solve()