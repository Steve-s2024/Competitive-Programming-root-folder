# appalling problem. I spent all that I can to come down to this genius solution. then the hint says bitmask...
# bitmask is what I rejected right from the beginning since the analysis I made give worst case as 2^28, not 2^14.


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @cache
        def fn(a, b, l):
            if a == b: return 1
            if a > b: a, b = b, a

            dif = b - a - 1
            if b >= (l + 1) // 2:  # b and a share side and b will eliminate one element
                x = b - (l + 1) // 2
                b -= 1 + x
                dif -= 1 + 2 * x + l % 2

            res = 100
            for i in range(a + 1):
                A, B = i, b - i - 1
                for j in range(dif + 1):
                    res = min(res, fn(A, B - j, (l + 1) // 2) + 1)

            return res

        @cache
        def fn2(a, b, l):
            if a == b: return 1
            if a > b: a, b = b, a

            dif = b - a - 1
            if b >= (l + 1) // 2:  # b and a share side and b will eliminate one element
                x = b - (l + 1) // 2
                b -= 1 + x
                dif -= 1 + 2 * x + l % 2

            res = 0
            for i in range(a + 1):
                A, B = i, b - i - 1
                for j in range(dif + 1):
                    res = max(res, fn2(A, B - j, (l + 1) // 2) + 1)

            return res

        a, b = firstPlayer - 1, n - secondPlayer
        return [fn(a, b, n), fn2(a, b, n)]








