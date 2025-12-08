# this is not hard version, this is not 1700. this is just annoying and unproductive work.


def solve():
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    quan = [int(e) for e in input().split()]
    zp = list(zip(nums, quan))
    zp.sort()

    res = min(m//zp[-1][0], zp[-1][1]) * zp[-1][0]
    for i in range(n-1):
        x1, y1 = zp[i]
        x2, y2 = zp[i + 1]
        if x1+1 != x2: res = max(res, min(m//x1, y1) * x1)
        else: # when they are consecutive
            mul1 = min(m//x1, y1)
            re = m - mul1*x1
            mul2 = min(re//x2, y2)
            # print(mul1, mul2)
            re -= mul2*x2
            y2 -= mul2
            re -= min(re, min(mul1, y2))
            res = max(res, m-re)
    print(res)


t = int(input())
for i in range(t): solve()


