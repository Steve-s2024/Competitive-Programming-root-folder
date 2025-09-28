# super annoying question with the BIT update function: 65%
class BIT:
    def __init__(self, arr):
        n = len(arr)
        tree = [0] * (n + 1)
        self.tree = tree
        self.arr = [0] * n
        for i, v in enumerate(arr): self.update(i, v)

    def update(self, i, v):
        arr = self.arr
        tmp = arr[i]
        m = len(arr)
        ov = 1 if i and i < m - 1 and arr[i - 1] < arr[i] > arr[i + 1] else 0
        arr[i] = v
        nv = 1 if i and i < m - 1 and arr[i - 1] < arr[i] > arr[i + 1] else 0
        d = nv - ov
        tree = self.tree
        n = len(tree)
        j = i + 1
        while j < n:
            tree[j] += d
            j += j & (~(j - 1))

        if i > 1:
            arr[i] = tmp
            ov = 1 if arr[i - 2] < arr[i - 1] > arr[i] else 0
            arr[i] = v
            nv = 1 if arr[i - 2] < arr[i - 1] > arr[i] else 0
            d = nv - ov
            tree = self.tree
            n = len(tree)
            j = i
            while j < n:
                tree[j] += d
                j += j & (~(j - 1))

        if i < m - 2:
            arr[i] = tmp
            ov = 1 if arr[i] < arr[i + 1] > arr[i + 2] else 0
            arr[i] = v
            nv = 1 if arr[i] < arr[i + 1] > arr[i + 2] else 0
            d = nv - ov
            tree = self.tree
            n = len(tree)
            j = i + 2
            while j < n:
                tree[j] += d
                j += j & (~(j - 1))

    def query(self, l, r):
        tree = self.tree
        ls, rs = 0, 0
        li, ri = l, r + 1
        while li:
            ls += tree[li]
            li &= li - 1
        while ri:
            rs += tree[ri]
            ri &= ri - 1
        return rs - ls


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        bit = BIT(nums)
        ans = []
        n = len(nums)
        for q in queries:
            if q[0] == 1:
                res = bit.query(q[1], q[2])
                arr = bit.arr
                l, r = q[1], q[2]
                # print(arr, l, r)
                if 0 < l < n - 1 and arr[l - 1] < arr[l] > arr[l + 1]: res -= 1
                if 0 < r < n - 1 and arr[r - 1] < arr[r] > arr[r + 1] and r != l: res -= 1
                ans.append(res)
            else:
                bit.update(q[1], q[2])
        return ans