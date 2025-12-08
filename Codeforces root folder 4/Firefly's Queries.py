# quite crazy, the idea is so straightforward compares to other same rating problems. but to get the indexing right
# with the prefix and suffix sum is definitely a tedious and non-fruitful process

def solve():
    n, q = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    sm = sum(nums)

    pre = [0]*n
    suf = [0]*n
    for i in range(n): pre[i] = pre[i-1]+nums[i]
    for i in range(n-1, -1, -1): suf[i] = suf[(i+1)%n]+nums[i]
    # print(pre, suf)

    for i in range(q):
        l, r = [int(e) for e in input().split()]
        l, r = l-1, r-1

        lmul = l // n
        lre = (n - l % n) % n
        rmul = r//n
        rre = (r+1)%n
        lx = l+lre
        rx = r-rre
        res = 0
        if lx <= rx:
            md = (rx - lx + 1) // n
            res += md*sm

        a = 0
        if lre and lmul: a += pre[lmul-1]-(pre[lmul-lre-1] if lmul-lre > 0 else 0)
        lre -= min(lre, lmul)
        if lre: a += suf[-lre]


        b = 0
        if rre:
            # rmul == 0? then start with 1, rmul == i? then start with i+1
            # if rmul is i, then the excluded part is always i, i-1, i-2...
            ext = n-rre
            ofs = 0
            if rmul and ext:
                mi = min(rmul, ext)
                ofs += pre[rmul-1] - (pre[rmul-mi-1] if rmul-mi-1 >= 0 else 0)
                rmul -= mi
                ext -= mi
            if ext: ofs += suf[-ext]

            b = sm-ofs

        # print(res, a, b)
        res += a + b
        if r//n == l//n and a and b: res -= sm
        print(res)


t = int(input())
for i in range(t): solve()



