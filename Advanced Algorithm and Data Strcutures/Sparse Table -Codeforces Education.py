from math import inf, ceil, floor, sqrt, gcd, lcm
# a compact revision of sparse table
class maxSparseTable():
    def __init__(self, nums):
        n, sp, pw = len(nums), [nums[:]], 2
        while pw <= n:
            tmp = []
            for i in range(0, n - pw + 1): tmp.append(max(sp[-1][i], sp[-1][i + pw // 2]))
            sp.append(tmp)
            pw *= 2
        self.sp = sp

    def query(self, l, r):
        sp, ln = self.sp, (r - l + 1).bit_length()
        return max(sp[ln - 1][l], sp[ln - 1][r - pow(2, ln - 1) + 1])


# a more generic version of the sparse table
class minSparseTable():
    def __init__(self, nums):
        self.sp = self.build(nums)

    def build(self, nums):
        n = len(nums)
        sp = [nums[:]]
        pw = 2
        while pw <= n:
            tmp = []
            for i in range(0, n-pw+1): tmp.append(min(sp[-1][i], sp[-1][i+pw//2]))
            sp.append(tmp)
            pw *= 2
        return sp

    def query(self, l, r):
        sp = self.sp
        sz = r - l + 1
        ln = sz.bit_length()
        res = min(sp[ln - 1][l], sp[ln - 1][r - pow(2, ln - 1) + 1])
        return res


# behold, sparse table, processing in n*log(n), query in constant time (brilliant algorithm for min/max range query)
# the data structure is designed to only work for min/max/gcd (idempotent) query but not sum query since the blocks overlap
# want sum query? need to avoid overlap and therefore introduce another log(n) factor per query (which behaves exactly
# like segment tree)
def minSparseTable():
    n = int(input())
    nums = [int(e) for e in input().split()]
    mp = [nums[:]]
    pw = 2
    while pw <= n:
        tmp = []
        for i in range(0, n-pw+1): tmp.append(min(mp[-1][i], mp[-1][i+pw//2]))
        mp.append(tmp)
        pw *= 2

    ans = []
    q = int(input())
    for i in range(q):
        l, r = [int(e) for e in input().split()]
        sz = r-l+1
        ln = sz.bit_length()
        res = min(mp[ln-1][l], mp[ln-1][r-pow(2, ln-1)+1])
        ans.append(res)
    for mi in ans: print(mi)





# first step, minimum range query with block AKA square root decomposition. time complexity per query O(sqrt(n))
# introducing to the idea of breaking array into blocks to speed up query
# this code didn't pass the first practice problem, TLE on testcase3
# though it follows the optimal partition of blocks.
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    q = int(input())
    sqr = ceil(sqrt(n))
    blk = [inf]*sqr
    for i in range(n): blk[i//sqr] = min(blk[i//sqr], nums[i])
    # print(blk)
    ans = []
    for i in range(q):
        l, r = [int(e) for e in input().split()]
        nl = l + l%sqr + sqr
        nr = r - r%sqr
        mi = inf
        for i in range(l, nl): mi = min(nums[i], mi)
        for i in range(nl//sqr, nr//sqr + 1): mi = min(blk[i], mi)
        for i in range(nr, r): mi = min(nums[i], mi)
        # print(mi)
        ans.append(mi)
    for mi in ans: print(mi)

t = int(input())
for i in range(t):
    solve()




