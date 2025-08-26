# didn't prove it, but seems to be okay. passed all the pretests
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    nums.sort()
    res = 0
    if n%2 == 1:
        for i in range(0, n, 2): res += nums[i]
    else:
        for i in range(1, n, 2): res += nums[i]
    print(res)



t = int(input())
for i in range(t):
    solve()
