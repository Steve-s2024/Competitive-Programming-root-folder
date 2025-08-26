# like this question. did reference lot from the Prime Sieve. rest is just union find: 91%
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
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n + 1)
        arr = [False] * (n + 1)
        for i in range(threshold + 1, n + 1):
            if arr[i]: continue
            for j in range(i + i, n + 1, i):
                arr[j] = True
                uf.union(i, j)

        ans = []
        for u, v in queries:
            ans.append(uf.find(u) == uf.find(v))
        return ans