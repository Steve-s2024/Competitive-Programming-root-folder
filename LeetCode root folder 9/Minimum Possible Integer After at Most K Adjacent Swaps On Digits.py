# can't believe my greedy intuition is true!

class BIT:
    def __init__(self, arr):
        n = len(arr)
        tree = [0]*(n+1)
        self.tree = tree
        self.arr = [0]*n
        for i, v in enumerate(arr): self.update(i, v)

    def update(self, i, v):
        d = v - self.arr[i]
        self.arr[i] += d
        tree = self.tree
        n = len(tree)
        i += 1
        while i < n:
            tree[i] += d
            i += i&(~(i-1))

    def query(self, l, r):
        tree = self.tree
        ls, rs = 0, 0
        li, ri = l, r+1
        while li:
            ls += tree[li]
            li &= li-1
        while ri:
            rs += tree[ri]
            ri &= ri-1
        return rs-ls

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        dgts = list(num)
        n = len(dgts)
        ar = sorted(set(dgts))
        mp = defaultdict(deque)
        for i in range(n): mp[dgts[i]].append(i)
        res = []
        bit = BIT([0]*n)
        while k >= 0:
            for v in ar:
                if mp[v]:
                    i = mp[v][0]
                    x = bit.query(0, i-1)
                    if i-x > k: continue
                    bit.update(i, 1)
                    mp[v].popleft()
                    k -= i-x
                    dgts[i] = ''
                    res.append(v)
                    break
            else: break
        # print(res, dgts)
        return ''.join(res) + ''.join(dgts)
