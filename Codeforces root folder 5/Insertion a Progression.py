# greedy!

def solve():
    n, x = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]

    mi, mx = min(nums), max(nums)
    if mi > 1: ar = [nums[0]-1, nums[-1]-1, 2*(mi-1)]
    else: ar = [0]
    if mx < x: br = [x-nums[0], x-nums[-1], 2*(x-mx)]
    else: br = [0]
    # print(ar, br)

    ans = 1<<62
    base = sum([abs(nums[i]-nums[i+1]) for i in range(n-1)])
    for i in range(len(ar)):
        for j in range(len(br)):
            if i != 2 and ar[i]*br[j] != 0 and i == j: continue
            ans = min(ans, base + ar[i] + br[j])
    print(ans)

for _ in range(int(input())): solve()