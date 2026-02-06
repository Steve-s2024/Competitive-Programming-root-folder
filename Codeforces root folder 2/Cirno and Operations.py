# I gambled a bit, even though I did figure out the majority of the question
# and I'm pretty sure that it is the right track.


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    sm = sum(nums)
    res = -float('inf')
    while len(nums) > 1:
        n = len(nums)
        res = max(abs(nums[0] - nums[-1]), res)
        tmp = []
        for i in range(1, n):
            diff = nums[i]-nums[i-1]
            tmp.append(diff)
        nums = tmp
    print(max(res, sm))




t = int(input())
for tt in range(t):
    solve()