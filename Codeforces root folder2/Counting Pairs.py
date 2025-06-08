# binary search solution, I need to be more fluent in implementing
# binary search
def binarySearch(lBound, rBound, arr):
    n = len(arr)
    l, r = 0, n-1
    while l < r:
        m = (l+r+1)//2
        if arr[m] < lBound:
            l = m
        else:
            r = m-1
    left = l
    l, r = 0, n-1
    while l < r:
        m = (l+r)//2
        if arr[m] > rBound:
            r = m
        else:
            l = m+1
    right = r
    # print(arr, lBound, rBound, left, right)
    return right-left-1


def solve():
    n, x, y = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    sm = sum(nums)
    nums.sort()
    inf = float('inf')
    nums = [-inf] + nums + [inf]
    res = 0
    for i in range(1, n+1):
        # the range to query --> (sm-(x+nums[i]), sm-(y+nums[i]))
        l, r = sm-(y+nums[i]), sm-(x+nums[i])
        tmp = binarySearch(l, r, nums)
        res += tmp

        if nums[i] in range(l, r+1):
            res -= 1
    print(res//2)


t = int(input())

for tt in range(t):
    solve()