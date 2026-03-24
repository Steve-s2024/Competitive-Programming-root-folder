# there is actually a lot of things I can use the segment tree to do. it is pretty powerful.
# it is certainly not limited to range query
class SumTree:
    def __init__(self, ar):
        n = len(ar)
        tre = [0]*((1<<n.bit_length())-1 + n)
        self.tre, self.n = tre, n
        for i in range(n): self.update(i, ar[i])

    def update(self, i, v):
        tre, n = self.tre, self.n
        l, r = 0, (1<<n.bit_length())-1
        j, ar = 0, []
        while l < r:
            ar.append(j)
            m = (l+r)//2
            if i <= m: j, r = 2*j+1, m
            else: j, l = 2*j+2, m+1
        dif = v-tre[j]
        tre[j] = v
        for j in ar: tre[j] += dif

    def query(self, L, R):
        tre, n = self.tre, self.n
        res = 0
        def recursive(j, l, r):
            nonlocal L, R, res
            if r < L or l > R or l > r: return
            if L <= l and r <= R:
                res += tre[j]
                return
            m = (l+r)//2
            recursive(2*j+1, l, m)
            recursive(2*j+2, m+1, r)
        recursive(0, 0, (1<<n.bit_length())-1)
        return res

class MinTree:
    def __init__(self, ar):
        n = len(ar)
        tre = [1<<31] * ((1 << n.bit_length()) - 1 + n + 1)
        self.tre, self.n = tre, n
        for i in range(n): self.update(i, ar[i])

    def update(self, i, v):
        tre, n = self.tre, self.n
        l, r = 0, (1 << n.bit_length()) - 1
        j, ar = 0, []
        while l < r:
            ar.append(j)
            m = (l + r) // 2
            if i <= m:
                j, r = 2 * j + 1, m
            else:
                j, l = 2 * j + 2, m + 1
        tre[j] = v
        for j in ar[::-1]: tre[j] = min(tre[2 * j + 1], tre[2 * j + 2])

    def query(self, L, R):
        tre, n = self.tre, self.n
        res = 1<<31
        def recursive(j, l, r):
            nonlocal L, R, res
            if r < L or l > R or l > r: return
            if L <= l and r <= R:
                res = min(res, tre[j])
                return
            m = (l + r) // 2
            recursive(2 * j + 1, l, m)
            recursive(2 * j + 2, m + 1, r)

        recursive(0, 0, (1 << n.bit_length()) - 1)
        return res

    def find(self, x):
        tre, n = self.tre, self.n
        res = -1
        def recursive(j, l, r):
            nonlocal res
            if l >= n:
                res = -1
                return
            if l == r:
                res = l
                return
            m = (l + r) // 2
            if tre[2*j+1] <= x: recursive(2 * j + 1, l, m)
            else: recursive(2 * j + 2, m + 1, r)

        recursive(0, 0, (1 << n.bit_length()) - 1)
        return res



class BookMyShow:

    def __init__(self, n: int, m: int):
        self.mit, self.smt, self.n, self.m = MinTree([0]*n), SumTree([0]*n), n, m
        self.j = 0
    def gather(self, k: int, maxRow: int) -> List[int]:
        mit, smt, n, M = self.mit, self.smt, self.n, self.m
        res = mit.find(M-k)
        if res == -1 or res > maxRow: return []
        # print(res)
        x = mit.query(res, res)
        mit.update(res, x+k)
        smt.update(res, x+k)
        # print('::', res, x)
        return [res, x]


    def scatter(self, k: int, maxRow: int) -> bool:
        mit, smt, n, M = self.mit, self.smt, self.n, self.m
        j = self.j

        t = (maxRow+1)*M - smt.query(0, maxRow)
        if t < k: return False

        while k:
            # print(3)
            x = smt.query(j, j)
            mi = min(k, M-x)
            k -= mi
            smt.update(j, x+mi)
            mit.update(j, x+mi)
            if k: j += 1
        self.j = j
        # if j < n: print(j, smt.query(j, j))
        return True

