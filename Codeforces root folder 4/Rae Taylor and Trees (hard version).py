# my greedy journey
# greedy is the best way to hone mantel capability

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
    nums = [int(e)-1 for e in input().split()]
    sp = minSparseTable(nums)
    mp = Counter(nums)
    hp = nums[:]
    heapify(hp)
    vs = [0]*n
    res = []
    for i in range(n-1, -1, -1):
        if vs[nums[i]]: continue
        mi = sp.query(0, i)
        if i != n-1:
            if vs[mi]: res.append((nums[i], mi))
            else:
                print('No')
                return

        vs[nums[i]] = 1
        while hp and hp[0] < nums[i]:
            while hp and mp[hp[0]] == 0: heappop(hp)
            if hp and hp[0] < nums[i]:
                x = heappop(hp)
                res.append((nums[i], x))
                vs[x] = 1


        mp[nums[i]] -= 1

    # print('Yes', len(res), n)
    # print(res)
    print('Yes')
    for l, r in res: print(l+1, r+1)


for _ in range(int(input())): solve()




