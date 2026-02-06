# great question, not hard at all, but make the brain jiggle
def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    nums.sort()
    nums[-1] -= 1
    nums.sort()
    if nums[-1] - nums[0] > k:
        print('Jerry')
    else:
        sm = sum(nums)+1
        if sm % 2 == 0:
            print('Jerry')
        else:
            print('Tom')

t = int(input())
for tt in range(t):
    solve()
