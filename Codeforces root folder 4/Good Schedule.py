# just painful

def solve():
    n = int(input())
    A = [int(x)-1 for x in input().split()]
    B = [int(x)-1 for x in input().split()]

    mp1, mp2 = [-1]*n, [-1]*n
    dp = [-1]*(n+1)
    for i in range(n-1, -1, -1):
        a, b = A[i], B[i]
        if a != b:
            mp1[a], mp1[b] = i, i
            continue

        if a == n-1: dp[i] = n-1
        else:
            j = mp1[a+1]
            if mp2[a+1] != -1:
                if j != -1 and j < mp2[a+1]: dp[i] = j-1
                else: dp[i] = dp[mp2[a+1]]
            else:
                if j != -1: dp[i] = j-1
                else: dp[i] = n-1
        mp2[a] = i

    ans = 0
    for i in range(n):
        if A[i] == B[i] == 0: ans += dp[i]-i+1
        else: dp[i] = -1


    for i in range(n-1, -1, -1):
        a, b = A[i], B[i]
        if 0 not in [a, b]:
            dp[i] = max(i, dp[i+1])
            ans += dp[i]-i+1

    print(ans)


for _ in range(int(input())): solve()
