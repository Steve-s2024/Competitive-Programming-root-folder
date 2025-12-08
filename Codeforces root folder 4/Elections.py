# light work babyeah!
from math import inf

def solve():
    n, c = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    # the updated input below doesn't change the result
    nums[0] += c
    c = 0

    suf = [0]*n
    mx = nums[-1]
    for i in range(n-1, -1, -1):
        mx = max(mx, nums[i])
        suf[i] = mx
    suf.append(0)

    mx = -inf
    sm = 0
    ans = []
    for i in range(n):
        cost = 0
        if mx >= nums[i] or nums[i] < suf[i+1]:
            cost += i
            if nums[i] + sm < suf[i+1]: cost += 1
        ans.append(cost)
        sm += nums[i]
        mx = max(mx, nums[i])


    print(' '.join(str(e) for e in ans))


t = int(input())
for i in range(t): solve()