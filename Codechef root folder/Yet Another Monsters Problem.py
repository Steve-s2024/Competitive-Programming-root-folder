# greedy and sorting, I solve this kinda fast
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    nums.sort()
    res = float('inf')
    cnt = 0

    for i in range(n-1, -1, -1):
        tot = nums[i] + cnt
        res = min(res, tot)
        cnt += 1

    res = min(res, n)
    print(res)




t = int(input())
for i in range(t):
    solve()