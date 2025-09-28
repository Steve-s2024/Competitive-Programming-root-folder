# made history today, live ranking 346 all killed in 27 minutes. though the contest is easy but the question is really
# my type.
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
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:

        def helper(arr):
            res = 0
            idx = [e[0] for e in arr]
            val = [e[1] for e in arr]
            val.sort()
            l, r = 0, len(arr) - 1
            for i in range(len(arr)):
                if idx[i] % 2 == 0:
                    res += val[r]
                    r -= 1
                else:
                    res -= val[l]
                    l += 1
            return res

        n = len(nums)
        uf = UnionFind(n)
        for u, v in swaps: uf.union(u, v)
        mp = defaultdict(list)
        for i in range(n): mp[uf.find(i)].append((i, nums[i]))

        # print(mp)
        res = 0
        for val in mp.values():
            res += helper(val)
        return res
