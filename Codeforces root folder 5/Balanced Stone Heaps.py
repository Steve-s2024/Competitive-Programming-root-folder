#
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    res = -1
    l, r = 0, max(nums)
    while l <= r:
        m = (l+r)//2
        cp = nums[:]
        for i in range(n-1, 1, -1):
            x = min(max(0, cp[i]-m), nums[i]) // 3
            cp[i-1] += x
            cp[i-2] += 2*x

        if min(cp) >= m:
            res = m
            l = m+1
        else: r = m-1
    print(res)


for _ in range(int(input())): solve()
