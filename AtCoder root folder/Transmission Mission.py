# this is some rarely good question in ABC
def solve():
    n, m = [int(e) for e in input().split()]
    nums = [2*int(e) for e in input().split()]
    nums.sort()
    tot = nums[-1] - nums[0]

    difs = []
    for i in range(1, n):
        difs.append(nums[i] - nums[i-1])
    difs.sort(reverse = True)
    offset = sum(difs[:m-1])
    # print(difs)
    # print(tot, offset)
    print((tot-offset)//2)


solve()
