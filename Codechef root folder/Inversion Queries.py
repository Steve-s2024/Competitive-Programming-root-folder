# tle
def solveQuery(l, r, nums):
    n = len(nums)
    res = []
    for i in range(n):
        if nums[i] < l:
            res.append(l)
        elif nums[i] > r:
            res.append(r)
        else:
            res.append(nums[i])
    tot = 0
    for i in range(n):
        cnt = 0
        for j in range(i):
            if res[j] > res[i]:
                cnt += 1
        tot += cnt
    return tot

def solve():
    n, q = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    for i in range(q):
        l, r = [int(e) for e in input().split()]
        print(solveQuery(l, r, nums))









t = int(input())
for i in range(t):
    solve()