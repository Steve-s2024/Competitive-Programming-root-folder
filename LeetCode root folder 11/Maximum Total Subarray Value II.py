# good to learn this way of Dijkstra, the tough part is to link it with the shortest path algo.
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




class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        n = len(nums)
        mxt, mit = maxSparseTable(nums), minSparseTable(nums)
        res = 0
        hp = [[-(mxt.query(0, n-1)-mit.query(0, n-1)), 0, n-1]]
        vs = set()
        while k:
            x, i, j = heappop(hp)
            if (i, j) in vs: continue
            res += -x
            vs.add((i, j))
            if i<j:
                heappush(hp, (-(mxt.query(i+1, j)-mit.query(i+1, j)), i+1, j))
                heappush(hp, (-(mxt.query(i, j-1)-mit.query(i, j-1)), i, j-1))
            k -= 1
        return res

