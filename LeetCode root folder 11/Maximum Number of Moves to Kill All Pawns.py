# for no reason this TLE, there could not be a better solution. and I also tried iterative DP and that shit is 4 times slower than the recursive
#
class Solution:

    def helper(self, x, y):
        vs = set([(x, y)])
        q = deque([(x, y)])
        ct = 0
        dp = {}
        while q:
            for _ in range(len(q)):
                l, r = q.popleft()
                dp[(l, r)] = ct
                for f1 in [1, -1]:
                    for f2 in [1, -1]:
                        for x, y in [(1, 2), (2, 1)]:
                            L, R = l + f1 * x, r + f2 * y
                            if L in range(50) and R in range(50) and (L, R) not in vs:
                                vs.add((L, R))
                                q.append((L, R))
            ct += 1
        return dp

    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        mp = []
        for x, y in positions: mp.append(self.helper(x, y))
        n = len(positions)

        @cache
        def fn(msk, x, y, f):
            if msk == (1 << n) - 1: return 0
            res = 0 if not f else inf
            for i in range(n):
                if 1 << i & msk: continue
                X, Y = positions[i]
                cst = mp[i][(x, y)]
                a = fn(msk | 1 << i, X, Y, f ^ 1) + cst
                if not f:
                    res = max(res, a)
                else:
                    res = min(res, a)
            return res

        res = fn(0, kx, ky, 0)
        return res
