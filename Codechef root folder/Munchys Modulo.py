# fking ridiculous, the worst case of 25 millions and passed
# after 20 secs of waiting it passed right before I start translating it into C++
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    nums.sort()
    res = nums[-2]
    # if nums[-2] + nums[-3] > nums[-1]: res = nums[-1]
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            res = max(res, nums[-1] % (nums[i] + nums[j]))

    print(res)


t = int(input())
for i in range(t):
    solve()