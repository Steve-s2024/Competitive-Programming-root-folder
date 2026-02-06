# thoertically this n*sqrt(nums[i]) should not pass, worst case is 3*1e7
# but the testcases are not extreme so it passed. if [1e5]*1e5 is the input I would expect TLE

# also, linear sieve should be able to optimize it to n*log(nums[i])
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]

class Solution:
    def fac(self, e):
        res = []
        n, f = e, 2
        while f <= sqrt(e):
            while n % f == 0:
                res.append(f)
                n //= f
            f += 1
        if n > 1: res.append(n)
        return res

    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        ar = [self.fac(v) for v in nums]
        uf = UnionFind(n)
        # print(ar)
        mp = {}
        i = 0
        for fs in ar:
            for f in fs:
                if f in mp:
                    uf.union(mp[f], i)
                else:
                    mp[f] = i
            i += 1
        return max(uf.size)