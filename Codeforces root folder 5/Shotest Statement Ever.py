# baozii make it easier please man what are u doing!

def solve():
    x, y = [int(e) for e in input().split()]
    def helper(x, y):

        n = 32
        t = ((1<<n)-1) ^ x
        tp = [int(e) for e in list(str(bin(t))[2:].zfill(n))]
        ar = []
        for i in range(n):
            if tp[i]: ar.append(i)

        sz = len(ar)
        res = 0
        l, r = 0, (1<<sz)-1

        while l <= r:
            m = (l+r)//2
            i = 0
            tp = [0]*n
            for e in str(bin(m))[2:].zfill(sz):
                tp[ar[i]] = int(e)
                i += 1

            s = ''.join(str(e) for e in tp)
            t = int(s, 2)

            if abs(res-y) > abs(t-y): res = t
            if t >= y: r = m-1
            else: l = m+1
        # print(x, res)
        return x, res



    res = helper(x, y)
    a, b = helper(y, x)
    if abs(x-b) + abs(y-a) <= abs(x-res[0]) + abs(y-res[1]): res = (b, a)

    print(res[0], res[1])


for _ in range(int(input())): solve()

