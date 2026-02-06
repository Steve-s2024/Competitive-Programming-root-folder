# a lazy tree variation handling binary array "flipping range update" (flip a range of element from 0 to 1 or from 1 to 0)
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


# 2026/01/04, lazy seg tree, same idea as lazy heap "only update when forced to". much harder to implement than a lazy heap though


# an implementation of sum segment tree with lazy propagation, Range Update and Query runs in logn time
# note: rangeUpdate is doing this update,
#           for i in range(l, r+1): ar[i] += v
# it is, however, not doing this update (I can't figure out a way to do this update)
#           for i in range(l, r+1): ar[i] = v
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
        tre[i] += size*x
        laz[i] = 0


    def rangeUpdate(self, L, R, v):
        tre, n, laz = self.tre, self.n, self.laz
        def recursive(j, l, r):
            nonlocal L, R, v
            if r < L or l > R or l > r: return 0
            self.push(j, r-l+1)
            if L <= l and r <= R:
                laz[j] += v
                return
            m = (l + r) // 2
            recursive(2 * j + 1, l, m)
            recursive(2 * j + 2, m + 1, r)
            tre[j] += (min(R, r) - max(L, l) + 1)*v
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






st = LazyTree([1, 2, 3, 4, 5])
print(st.tre)
print(st.query(0, 3))
print(st.query(2, 4))
print(st.tre)
st.rangeUpdate(0, 2, 2)
print(st.tre, st.laz)
print(st.query(0, 3))
print(st.query(2, 4))
print(st.query(1, 4))
st.rangeUpdate(3, 4, -2)
print(st.query(0, 3))
print(st.query(2, 4))
print(st.query(1, 4))
# 10
# 12
# 16
# 14
# 18
# 14
# 10
# 14