# cakewalk is not appropriate here. it got me thinking about the complexity a while before made up my mind with this
# BS & DP approach. the key observation for analyzing complexity is that the for loop summing up the previous
# dp[max(0,b-1),a-1] whill not make the whole thing O(n^2), it is still linear when you think careful enough


def solve():
    n, x = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    pre = [0]
    dp = []
    for i in range(n):
        tmp = pre[-1]+nums[i]
        l, r = 0, len(pre)-1
        a = -1
        while l <= r:
            m = (l+r)//2
            if tmp-pre[m] > x:
                a = m
                l = m+1
            else: r = m-1

        l, r = 0, len(pre)-2
        b = i
        while l <= r:
            m = (l+r)//2
            if pre[-1]-pre[m] <= x:
                b = m
                r = m-1
            else: l = m+1
        # print(b, a)
        if b <= a:
            sm = a-b+1
            for i in range(max(0, b-1), a): sm += dp[i]
            dp.append(sm)
        else: dp.append(0)

        pre.append(tmp)
    # print(dp)
    tot = n*(n+1)//2
    print(tot-sum(dp))


t = int(input())
for i in range(t): solve()