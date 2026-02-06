# easy straightforward recursive solution, O(nm(n+m))
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        mp = {}
        for h, w, p in prices: mp[(h, w)] = p
        @cache
        def recursive(H, W):
            res = mp[(H, W)] if (H, W) in mp else 0
            for i in range(1, H):
                a = recursive(i, W) + recursive(H-i, W)
                res = max(res, a)
            for i in range(1, W):
                a = recursive(H, i) + recursive(H, W-i)
                res = max(res, a)
            return res
        return recursive(m, n)


# or, a trivial optimization reduce time by a factor of 2
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        mp = {}
        for h, w, p in prices: mp[(h, w)] = p
        @cache
        def recursive(H, W):
            res = mp[(H, W)] if (H, W) in mp else 0
            for i in range(1, H//2+1):
                a = recursive(i, W) + recursive(H-i, W)
                res = max(res, a)
            for i in range(1, W//2+1):
                a = recursive(H, i) + recursive(H, W-i)
                res = max(res, a)
            return res
        return recursive(m, n)