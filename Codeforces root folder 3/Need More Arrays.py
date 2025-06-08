# nice
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    prev = -10**10
    cnt = 0
    for i in range(n):
        if nums[i] in [prev+1, prev]:
            continue
        cnt += 1
        prev = nums[i]
    print(cnt)


t = int(input())
for i in range(t):
    solve()
