# a common technique of doing offset to counter the effect of rotation, then calculate sum in constant time
def solve():
    n, q = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    tot = 0
    pre = []
    for i in range(n):
        tot += nums[i]
        pre.append(tot)
    ofs = 0
    pre.append(0)

    for i in range(q):
        qry = [int(e) for e in input().split()]
        if qry[0] == 1:
            ofs += qry[1]
            ofs %= n
        else:
            _, l, r = qry
            l, r = l-1, r-1
            nl = (l+ofs) % n
            nr = (r+ofs) % n
            if nl <= nr: print(pre[nr] - pre[nl-1])
            else: print(pre[-2] - pre[nl-1] + pre[nr])



solve()
