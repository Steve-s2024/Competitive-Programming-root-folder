# 12%, should be higher

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
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = list(zip(nums, [i for i in range(n)]))
        arr.sort()

        uf = UnionFind(n)
        for i in range(1, n):
            if abs(arr[i][0] - arr[i - 1][0]) <= limit:
                uf.union(arr[i][1], arr[i - 1][1])

        ans = [0] * n
        mp = defaultdict(list)
        for i in range(n):
            mp[uf.find(arr[i][1])].append(arr[i])

        for val in mp.values():
            arr1, arr2 = [], []
            for a, b in val:
                arr1.append(a)
                arr2.append(b)
            arr1.sort()
            arr2.sort()
            for i in range(len(val)):
                ans[arr2[i]] = arr1[i]

        return ans
