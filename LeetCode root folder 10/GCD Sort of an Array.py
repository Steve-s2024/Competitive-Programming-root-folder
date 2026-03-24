# done something very similar

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

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
    def fac(self, n):
        fs = []
        f = 2
        while f <= int(sqrt(n)):
            while n % f == 0:
                if not fs or fs[-1] != f: fs.append(f)
                n //= f
            f += 1
        if n > 1: fs.append(n)
        return fs

    def gcdSort(self, nums: List[int]) -> bool:
        n = len(nums)
        uf = UnionFind(n)
        mp = defaultdict(list)
        for i, v in enumerate(nums):
            for f in self.fac(v): mp[f].append(i)

        for ar in mp.values():
            for i in range(len(ar)-1): uf.union(ar[i], ar[i + 1])

        MP = defaultdict(list)
        for u in range(n): MP[uf.find(u)].append(u)

        def helper(ar):
            br = [nums[i] for i in ar]
            br.sort()
            for i in range(len(ar)): nums[ar[i]] = br[i]

        # print(MP)
        for ar in MP.values(): helper(ar)
        # print(nums)
        for i in range(n-1):
            if nums[i+1] < nums[i]: return False
        return True