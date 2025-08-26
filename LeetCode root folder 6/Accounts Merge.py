# union find solution with path compression and union by size: 20%
class UnionFind:
    def __init__(self, n):
        self.size = [1] * n
        self.prt = [i for i in range(n)]

    def find(self, x):
        if self.prt[x] != x:
            self.prt[x] = self.find(self.prt[x])
        return self.prt[x]

    def union(self, x, y):
        size = self.size
        prt = self.prt
        p1 = self.find(x)
        p2 = self.find(y)
        if p1 == p2: return
        if size[p1] > size[p2]:
            prt[p2] = p1
            size[p1] += size[p2]
        else:
            prt[p1] = p2
            size[p2] += size[p1]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        mp = defaultdict(set)
        for i in range(n):
            m = len(accounts[i])
            for j in range(1, m):
                for neighbor in mp[accounts[i][j]]:
                    uf.union(i, neighbor)
                mp[accounts[i][j]].add(i)

        res = defaultdict(set)
        for i in range(n):
            prt = uf.find(i)
            for j in range(1, len(accounts[i])):
                res[prt].add(accounts[i][j])

        ans = []
        for key, val in res.items():
            ans.append([accounts[key][0]] + sorted(list(val)))
        return ans



