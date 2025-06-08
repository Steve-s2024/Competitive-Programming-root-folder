# binary search solution, the search part is really a headache some time
def binarySearch(arr, tar):
    if arr[-1] < tar:
        return 0
    if arr[0] >= tar:
        return len(arr)
    l, r = 0, len(arr)-1
    res = -1
    while l <= r:
        m = (l+r)//2
        if arr[m] >= tar:
            r = m-1
        else:
            res = m
            l = m+1
    return len(arr)-res-1

def solve():
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]

    nums.sort()
    res = 0

    for i in range(1, n):
        # pretend the two colour a, b like this --> a1, a2...ai-1, bi, bi+1...bn-1
        a, b = binarySearch(nums, i), binarySearch(nums, n-i)
        # there are a elements that are suitable for being the left color
        # there are b elements that are suitable for being the right color
        res += a*b
        res -= min(a, b)  # get rid of the overlap(duplicate) color


    print(res)

t = int(input())
for i in range(t):
    solve()




# brute force
def solve():
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]

    res = 0

    for i in range(m):
        for j in range(i+1, m):
            sm = nums[i]+nums[j]
            cnt = min(nums[i], nums[j], n-1, sm -n +1)
            if cnt > 0:
                res += 2*cnt


    print(res)


t = int(input())
for i in range(t):
    solve()

