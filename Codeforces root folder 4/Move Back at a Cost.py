# took me 10 minutes to both read and coding it up? 1600 is just soso.
from heapq import heapify, heappush, heappop

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    mi = nums[-1]
    minheap = []
    for i in range(n - 2, -1, -1):
        if nums[i] > mi:
            heappush(minheap, nums[i] + 1)
            nums[i] = 0
        else:
            mi = nums[i]

    arr = []
    for num in nums:
        if num: arr.append(num)

    if minheap:
        l, r = 0, len(arr) - 1
        res = n
        while l <= r:
            m = (l + r) // 2
            if arr[m] > minheap[0]:
                res = m
                r = m - 1
            else:
                l = m + 1
        while arr and len(arr) > res: heappush(minheap, arr.pop() + 1)
        while minheap: arr.append(heappop(minheap))

    print(' '.join(str(e) for e in arr))


t = int(input())
for i in range(t): solve()





