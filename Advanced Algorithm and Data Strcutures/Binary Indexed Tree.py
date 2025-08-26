# here is the implementation of a binary indexed tree, computing the sum range query in log(n) time, update also in
# log(n) time
'''
class BinaryIndexedTree:
    def __init__(self, arr):
        n = len(arr)
        pre = [0]*n
        pre[0] = arr[0]
        for i in range(1, n): pre[i] = pre[i-1] + arr[i]

        tree = [0]*(n+1)
        for i in range(1, n+1):
            j = i&(~i+1)
            sm = pre[i-1] - pre[i^j] + arr[i^j]
            tree[i] = sm
        self.tree = tree
        self.arr = arr[:]

    def query(self, l, r):
        tree = self.tree
        res = 0
        r += 1
        while r:
            res += tree[r]
            r -= r&(~r+1)

        while l:
            res -= tree[l]
            l -= l&(~l+1)
        return res


    def update(self, idx, val):
        oldVal = self.arr[idx]
        self.arr[idx] = val
        tree = self.tree

        idx += 1
        dif = val-oldVal
        n = len(tree)
        while idx < n:
            tree[idx] += dif
            idx += idx&(~idx+1)



arr = [1, 2, 3, 4, 5, 6, 7]
bit = BinaryIndexedTree(arr)
print(
bit.query(0, 6),
bit.query(0, 3),
bit.query(2, 3),
bit.query(4, 6),
)
bit.update(4, 3)
bit.update(2, 0)
print(
bit.query(0, 6),
bit.query(0, 3),
bit.query(2, 3),
bit.query(4, 6)
)
'''

'''
for i in range(1, 100):
    print(f'node {i} can cover a range of {(i & (~i + 1))}')
'''
# a more concise version
class BinaryIndexedTree:
    def __init__(self, arr):
        n = len(arr)
        self.tree = [0]*(n+1)
        for i in range(n):
            self.update(i, arr[i])
    def query(self, l, r):
        tree = self.tree
        res = 0
        r += 1
        while r:
            res += tree[r]
            r -= r&(~r+1)

        while l:
            res -= tree[l]
            l -= l&(~l+1)
        return res


    def update(self, idx, delta):
        tree = self.tree
        idx += 1
        n = len(tree)
        while idx < n:
            tree[idx] += delta
            idx += idx&(~idx+1)

arr = [1, 2, 3, 4, 5, 6, 7]
bit = BinaryIndexedTree(arr)
print(
bit.query(0, 6),
bit.query(0, 3),
bit.query(2, 3),
bit.query(4, 6)
)
bit.update(4, -1)
bit.update(2, -3)
print(
bit.query(0, 6),
bit.query(0, 3),
bit.query(2, 3),
bit.query(4, 6)
)