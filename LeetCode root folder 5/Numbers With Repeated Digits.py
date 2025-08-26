

# MLE
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        size = len(str(n))

        @cache
        def recursive(num, i):
            nonlocal n, size
            if num > n: return 0
            if i == size: return 1
            res = 0
            for j in range(10):
                x = num * 10 + j
                if len(str(x)) != len(set(str(x))): continue
                res += recursive(x, i + 1)
            return res

        res = recursive(0, 0)
        return n - res + 1




