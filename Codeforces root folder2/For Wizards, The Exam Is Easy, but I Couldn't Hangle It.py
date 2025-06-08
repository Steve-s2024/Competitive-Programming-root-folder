# not elegant at all, just brute force...

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[j] <= nums[i]:
                total += 1
    l, r = 0, 0
    minPair = total
    for i in range(n):
        less, more = 0, 0
        for j in range(i+1, n):
            if nums[j] > nums[i]:
                more += 1
            if nums[j] < nums[i]:
                less += 1
            # minPair - less + more
            cur = total - less + more
            if cur < minPair:
                minPair = cur
                l, r = i, j
    print(l+1, r+1)


t = int(input())
for tt in range(t):
    solve()