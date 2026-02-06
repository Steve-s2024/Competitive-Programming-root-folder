# this problem is just bullshit, I realize its bullshit-ness after struggling for so long then just wrote this and it worked
class Solution:
    def soupServings(self, n: int) -> float:
        if n > 10000: return 1
        @cache
        def recursive(a, b):
            if a <= 0: return 1 if b > 0 else 0.5
            if b <= 0: return 0
            return sum(
                [0.25*recursive(a-100, b),
                0.25*recursive(a-75, b-25),
                0.25*recursive(a-50, b-50),
                0.25*recursive(a-25, b-75)]
            )

        return recursive(n, n)