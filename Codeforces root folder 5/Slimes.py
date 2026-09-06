# this is a relative easy 1800 and is very enjoyable


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


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    inf = 1<<50
    pre = [0]*n
    for i in range(n): pre[i] = pre[i-1] + nums[i]

    mxt, mit = maxSparseTable(nums), minSparseTable(nums)

    ans = [0]*n
    for i in range(n):
        e = nums[i]
        if i and nums[i-1] > e or i < n-1 and nums[i+1] > e:
            ans[i] = 1
            continue


        l, r = i+2, n-1
        s = inf
        while l <= r:
            m = (l+r)//2
            x = pre[m]-pre[i]
            if x > e and mxt.query(i+1, m) != mit.query(i+1, m):
                s = m-i
                r = m-1
            else: l = m+1

        l, r = 0, i-2
        t = inf
        while l <= r:
            m = (l+r)//2
            x = pre[i-1]-pre[m]+nums[m]
            if x > e and mxt.query(m, i-1) != mit.query(m, i-1):
                t = i-m
                l = m+1
            else: r = m-1

        ans[i] = min(s, t)
        if ans[i] == inf: ans[i] = -1

    print(*ans)





for _ in range(int(input())): solve()
