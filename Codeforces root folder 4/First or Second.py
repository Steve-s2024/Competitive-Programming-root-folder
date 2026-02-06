# tough, un-enjoyable, and doesn't teach much
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    pre = [nums[0]]
    ar = [nums[0]]
    t = 0
    for i in range(1, n):
        ar.append(nums[i])
        if ar[1] < 0:
            t += -ar[1]
            ar = ar[:1]
        else:
            t += ar[0]
            ar = [nums[i]]
        pre.append(t + ar[0])

    suf = [0]*n
    for i in range(n-1, -1, -1): suf[i] = suf[(i+1)%n] - nums[i]
    # print(pre)
    # print(suf)


    res = -inf
    for i in range(n):
        a = (suf[i+1] if i < n-1 else 0) + (pre[i-1] if i else 0)
        res = max(res, a)
    print(res)