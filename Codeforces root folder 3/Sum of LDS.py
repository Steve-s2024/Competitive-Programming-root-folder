# to tackle this problem, need to observe the pattern of LDS when max(p(i), p(i+1)) > p(i+2)
# such pattern exist, for finding the size of LDS in an interval, iterate through the interval
# when nums[i-1] > nums[i], LDS increase by 1, when nums[i-1] < nums[i], LDS stays the same.
# this observation & some summation math is enough to solve the problem efficiently

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    cnt = 1
    tot = 1
    for i in range(1, n):
        if nums[i] < nums[i-1]: cnt += 1
        tot += cnt
    res = 0
    for i in range(n):
        res += tot
        tot -= 1
        if i < n-1 and nums[i+1] < nums[i]: tot -= n-i-1
    print(res)


t = int(input())
for i in range(t):
    solve()