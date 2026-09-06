# man moving up to 1900, 1800 cannot satisfy my stomach for knowledge lol

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
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # print(A, B)
    mxt = maxSparseTable(A)
    mit = minSparseTable(B)

    mk = [False]*n

    for i in range(n):
        a, b = A[i], B[i]
        if a == b: mk[i] = True
        if a > b:
            print('No')
            return


    mp = {}
    for i in range(n-1, -1, -1):
        a, b = A[i], B[i]
        if a == b:
            mp[a] = i
            continue

        if b in mp:
            mk[i] = mxt.query(i, mp[b]) == b and mit.query(i, mp[b]) == b

        mp[a] = i


    mp = {}
    for i in range(n):
        a, b = A[i], B[i]
        if a == b or mk[i]:
            mp[a] = i
            continue

        if b in mp:
            # print(mp[b], i, mxt.query(mp[b], i), mit.query(mp[b], i))
            mk[i] = mxt.query(mp[b], i) == b and mit.query(mp[b], i) == b
        mp[a] = i

    # print(mk)
    for e in mk:
        if not e:
            print('No')
            return

    print('Yes')


for _ in range(int(input())): solve()


