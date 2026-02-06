# an old rival conquered. it's just hard to think of bottom up, but once that clicked it become several level easier
# this is ~1850, but I'd give it ~2100
class Solution:
    def champagneTower(self, poured: int, qi: int, qj: int) -> float:
        if qi == 0: return min(poured, 1)

        @cache
        def recursive(r, c):
            if r == 0: return max((poured - 1) / 2, 0)
            a = recursive(r - 1, c - 1) if c else 0
            b = recursive(r - 1, c) if c <= r - 1 else 0
            if r == qi: return min(1, a + b)
            return max((a + b - 1) / 2, 0)

        return recursive(qi, qj)