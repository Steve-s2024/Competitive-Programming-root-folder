# 有点烦人的一题， 估计思路不太正常有更好更简单的解法，主要是太多人做出来了
class BIT:
    def __init__(self, arr):
        n = len(arr)
        tree = [0] * (n + 1)
        self.tree = tree
        self.arr = [0] * n
        for i, v in enumerate(arr): self.update(i, v)

    def update(self, i, v):
        d = v - self.arr[i]
        self.arr[i] += d
        tree = self.tree
        n = len(tree)
        i += 1
        while i < n:
            tree[i] += d
            i += i & (~(i - 1))

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
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        s = list(s)
        n = len(s)
        prv = s[0]
        ar = [0] * n
        ar[0] = 1
        ar[-1] = 1
        for i in range(1, n):
            if s[i] != prv:
                ar[i] += 1
                ar[i - 1] += 1
            prv = s[i]
        # print(ar)
        ans = []
        bit = BIT(ar)
        for q in queries:
            if len(q) == 2:
                j = q[1]
                if j < n - 1:  # right side
                    if s[j] != s[j + 1]:
                        ar[j] -= 1
                        ar[j + 1] -= 1
                    else:
                        ar[j] += 1
                        ar[j + 1] += 1
                    bit.update(j, ar[j])
                    bit.update(j + 1, ar[j + 1])
                if j:  # left side
                    if s[j] != s[j - 1]:
                        ar[j] -= 1
                        ar[j - 1] -= 1
                    else:
                        ar[j] += 1
                        ar[j - 1] += 1
                    bit.update(j, ar[j])
                    bit.update(j - 1, ar[j - 1])
                s[j] = 'A' if s[j] != 'A' else 'B'

            else:
                l, r = q[1], q[2]
                if l == r:
                    ans.append(0)
                    continue
                x = bit.query(l, r)
                if l and s[l] == s[l - 1]: x += 1
                if r < n - 1 and s[r] == s[r + 1]: x += 1
                if x == 0: x = 2
                # print(ar, l, r, x)
                x //= 2
                ans.append(r - l + 1 - x)
        return ans

