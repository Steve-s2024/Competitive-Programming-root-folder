# first lazy seg tree solution, the one question introduces me to lazy tree
# I am a specialist in lazy tree now!

class LazyTree:
    def __init__(self, ar):
        n = len(ar)
        tre = [0]*((1<<n.bit_length())-1 + n)
        laz = [0]*((1<<n.bit_length())-1 + n)
        self.tre, self.n, self.laz = tre, n, laz
        for i in range(n): self.rangeUpdate(i, i, ar[i])

    def push(self, i, size):
        tre, laz = self.tre, self.laz
        n = len(tre)
        l, r = 2*i+1, 2*i+2
        x = laz[i]
        if l < n: laz[l] += x
        if r < n: laz[r] += x
        tre[i] = size-tre[i] if x%2 else tre[i]
        laz[i] = 0


    def rangeUpdate(self, L, R, v):
        tre, n, laz = self.tre, self.n, self.laz
        def recursive(j, l, r):
            nonlocal L, R, v
            if r < L or l > R or l > r: return 0
            self.push(j, r-l+1)
            if L <= l and r <= R:
                x = tre[j]
                laz[j] += v
                self.push(j, r-l+1)
                return tre[j]-x
            m = (l + r) // 2
            x = 0
            x += recursive(2 * j + 1, l, m) + recursive(2 * j + 2, m + 1, r)
            tre[j] += x
            return x
        recursive(0, 0, (1 << n.bit_length()) - 1)


    def query(self, L, R):
        tre, n, laz = self.tre, self.n, self.laz
        res = 0
        def recursive(j, l, r):
            nonlocal L, R, res
            if r < L or l > R or l > r: return
            self.push(j, r-l+1)
            if L <= l and r <= R:
                res += tre[j]
                return
            m = (l+r)//2
            recursive(2*j+1, l, m)
            recursive(2*j+2, m+1, r)
        recursive(0, 0, (1<<n.bit_length())-1)
        return res

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        ans = []
        sm = sum(nums2)
        tre = LazyTree(nums1)
        for t, a, b in queries:
            if t == 1: tre.rangeUpdate(a, b, 1)
            elif t == 2: sm += tre.query(0, n-1)*a
            else: ans.append(sm)

        return ans