# DP i did, why the tag prefix sum though?: 60%
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)

        @cache
        def recursive(i, numCarpets):
            nonlocal n, carpetLen
            if i >= n: return 0
            res = recursive(i + 1, numCarpets) + (1 if floor[i] == '1' else 0)
            if numCarpets:
                b = recursive(i + carpetLen, numCarpets - 1)
                res = min(res, b)
            return res

        return recursive(0, numCarpets)

