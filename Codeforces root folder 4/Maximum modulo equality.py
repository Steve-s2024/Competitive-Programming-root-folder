# hard one involving many non-trivial observation, I admit I guessed the first step, which is that the max mod of two
# number a and b such that a%m == b%m, is always abs(a-b). of course, this only works if the two number are different
# otherwise the max mod will be infinity.

# from there I build a proof from backwards using pretty neat technique.

# finally, it's time to find a good way to implement, and that happens to be sparse table. the implementation of
# sparse table is pretty tricky in this case, I need to build a bridge, x, every time doing initialization and querying



def solve():
    n, q = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    sp = []
    tmp = []
    for i in range(1, n): tmp.append(abs(nums[i-1] - nums[i]))
    sp.append(tmp)
    ln = 4
    while ln <= n:
        tmp = []
        for i in range(0, n-ln+1):
            x = abs(nums[i+ln//2-1]-nums[i+ln//2])
            d = gcd(sp[-1][i], sp[-1][i+ln//2], x)
            tmp.append(d)
        ln *= 2
        sp.append(tmp)



    # print(sp)
    ans = []
    for i in range(q):
        l, r = [int(e) for e in input().split()]
        l, r = l-1, r-1
        ln = (r-l+1).bit_length()-1
        if not ln:
            ans.append(0)
            continue
        # print(l, r)
        a, b = l+(1<<ln)-1, r-(1<<ln)+1
        # print(a, b)
        res = gcd(sp[ln-1][l], sp[ln-1][b])
        if a != b: res = gcd(res, abs(nums[a]-nums[b]))
        ans.append(res)
        # print(res)

    print(' '.join(str(e) for e in ans))



t = int(input())
for i in range(t): solve()
