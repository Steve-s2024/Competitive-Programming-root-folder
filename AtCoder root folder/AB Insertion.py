# F for a lazy segment tree haha, still TLE on one last test case...


class LazyMinTree:
    def __init__(self, a):
        n = len(a)
        self.n = n
        self.t = [0] * (4 * n)
        self.lz = [0] * (4 * n)

        def build(o, l, r):
            if l == r:
                self.t[o] = a[l]
                return
            m = (l + r) // 2
            build(o*2, l, m)
            build(o*2+1, m+1, r)
            self.t[o] = min(self.t[o*2], self.t[o*2+1])

        build(1, 0, n-1)

    def push(self, o):
        x = self.lz[o]
        if x:
            for c in (o*2, o*2+1):
                self.t[c] += x
                self.lz[c] += x
            self.lz[o] = 0

    def update(self, L, R, x):
        def dfs(o, l, r):
            if R < l or r < L:
                return
            if L <= l and r <= R:
                self.t[o] += x
                self.lz[o] += x
                return

            self.push(o)
            m = (l + r) // 2
            dfs(o*2, l, m)
            dfs(o*2+1, m+1, r)
            self.t[o] = min(self.t[o*2], self.t[o*2+1])

        dfs(1, 0, self.n-1)

    def query(self, L, R):
        def dfs(o, l, r):
            if R < l or r < L:
                return float('inf')
            if L <= l and r <= R:
                return self.t[o]

            self.push(o)
            m = (l + r) // 2
            return min(
                dfs(o*2, l, m),
                dfs(o*2+1, m+1, r)
            )

        return dfs(1, 0, self.n-1)

def solve():
    n = int(input())
    S = [' '] + list(input()) # sentinel value
    n += 1

    ar = [0]*n
    x = 0
    for i in range(1, n):
        if S[i] == 'A': x += 1
        else: x -= 1
        ar[i] = x
    laz = LazyMinTree(ar)
    # print(ar)
    for _ in range(int(input())):
        t, a, b = [e for e in input().split()]
        a = int(a)
        if int(t) == 1:
            o = S[a]
            S[a] = b
            if o == b: continue
            # print(o, b)
            if o == 'A': laz.update(a, n-1, -2)
            else: laz.update(a, n-1, 2)
        else:
            l, r = a, int(b)
            a, b = laz.query(l-1, l-1), laz.query(l, r)
            # print(a, b)
            if a <= b: print('Yes')
            else: print('No')




solve()


