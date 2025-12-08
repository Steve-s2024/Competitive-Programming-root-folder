# interesting approach, start from extreme case as base case, manipulate the exclusion and convert problem into sub
# problem with one less element (this is the brute force implementation, which can be optimized by SortedList, unfortunately
# codeforces OJ don't allow import of SortedList)

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    arr = []
    for i, num in enumerate(nums): arr.append((i, num))
    arr.sort(key = lambda i:i[1])
    res = 0
    for i, num in arr:
        a, b = 0, 0
        for j in range(i):
            if nums[j]: a += 1
        for j in range(i+1, n):
            if nums[j]: b += 1
        res += min(a, b)
        nums[i] = 0
    print(res)

t = int(input())
for i in range(t):
    solve()