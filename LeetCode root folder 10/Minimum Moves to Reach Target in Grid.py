# observation intensive | simple implementation
# very tough problem, CF style
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        t = (sx, sy)
        x, y = tx, ty
        res = 0
        while x >= sx and y >= sy and (x, y) != t:
            if x == y:
                n = x
                ans = res
                while n:
                    if t == (n, 0): return ans+1
                    if n%2: break
                    ans += 1
                    n >>= 1
                n = y
                ans = res
                while n:
                    if t == (0, n): return ans+1
                    if n%2: break
                    ans += 1
                    n >>= 1
                return -1
            if x > y:
                if x >= 2*y:
                    if x%2 != 0: return -1
                    x, y = x//2, y
                else: x, y = x-y, y
            else:
                if y >= 2*x:
                    if y%2 != 0: return -1
                    x, y = x, y//2
                else: x, y = x, y-x
            res += 1
        return res if (x, y) == t else -1



# TLE
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        @cache
        def fn(x, y):
            if (x, y) == (sx, sy): return 0
            if x == 0 and y == 0: return inf
            if x == y: return min(fn(0, y), fn(x, 0))+1
            if y > x:
                return min(
                    fn(x, y-x) if x else inf,
                    fn(x, y//2) if y%2 == 0 and y//2 >= x else inf
                )+1
            else:
                return min(
                    fn(x-y, y) if y else inf,
                    fn(x//2, y) if x%2 == 0 and x//2 >= y else inf
                )+1
        res = fn(tx, ty)
        return res if res != inf else -1

