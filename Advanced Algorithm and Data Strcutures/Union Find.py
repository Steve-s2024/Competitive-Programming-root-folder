# union find implementation, unlike my flood fill union find method, this is the standard union find algo that supports
# dynamic update and find
# as to the time complexity of find function, because I did path compression and rank by size, so it will be
# amortized O(1), for realistic input the actual time will not exceed the constant '5'.
# it is calculated by the ackermann function

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

