# good question, need decent math and greedy intuition
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    nums.sort()
    b, a = nums[1:n], nums[n:-1]
    a.append(nums[0])
    a.append(nums[-1])
    b.append(nums[0]+nums[-1])
    b[-1] += sum(a)-sum(b)

    res = []
    for i in range(n):
        res.append(a[i])
        res.append(b[i])
    res.append(a[-1])

    print(' '.join(str(e) for e in res))



t = int(input())
for i in range(t):
    solve()
