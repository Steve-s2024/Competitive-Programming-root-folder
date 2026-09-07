# hard


def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    nums.sort()


    sm = sum(nums)
    ans = 1<<30
    l, r = -1<<30, nums[0]-1
    while l <= r:
        m = (l+r)//2
        x = 0
        t = sm - (nums[0]-m)
        for i in range(n-1, 0, -1):
            if x > nums[i]-m: break
            if t <= k: break
            t -= nums[i]-m
            x += 1

        # print(t, m, x, nums[0]-m)
        if t <= k:
            ans = min(ans, x+nums[0]-m)
            l = m+1
        else: r = m-1


    sm = sum(nums)
    x = 0
    for i in range(n-1, 0, -1):
        if sm <= k: break
        sm -= nums[i]-nums[0]
        x += 1
    if sm <= k: ans = min(ans, x)
    print(ans)

for _ in range(int(input())): solve()






