# very close to solving the problem

def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    pre = [0]*n
    tot = 0
    for i in range(n):
        if nums[i] > k: tot += 1
        else: tot -= 1
        pre[i] = tot

    suf = [0]*n
    for i in range(n-1, -1, -1):
        if nums[i] > k: tot += 1
        else: tot -= 1
        suf[i] = tot


    premi = [0]*n
    mi = pre[0]
    for i in range(n):
        mi = min(mi, pre[i])
        premi[i] = mi

    sufmi = [0]*n
    mi = suf[0]
    for i in range(n-1, -1, -1):
        mi = min(mi, suf[i])
        sufmi[i] = mi

    #1. check for l _ r
    mi = suf[-1]
    for i in range(n-1, 1, -1):
        mi = min(mi, suf[i])
        if mi <= 0 and premi[i-2] <= 0:
            print('yes')
            return

    #2. check for l m _
    mx = suf[-1]
    for i in range(n-2, 0, -1):
        if suf[i] <= mx and premi[i-1] <= 0:
            print('yes')
            return
        mx = max(mx, suf[i])

    #3. check for _ m r
    mx = pre[0]
    for i in range(1, n-1):
        if pre[i] <= mx and sufmi[i+1] <= 0:
            print('yes')
            return
        mx = max(mx, pre[i])

    print('no')

t = int(input())
for i in range(t):
    solve()