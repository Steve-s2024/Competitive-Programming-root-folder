# the key is to note that with the operation specified, we will always convert n to 1 in log(n) time, so a knap sack
# that tries out all the operation(s) at any moment will work.

class Solution:
    def integerReplacement(self, n: int) -> int:

        @cache
        def recursive(m):
            if m == 1: return 0
            if m % 2 == 0:
                return recursive(m // 2) + 1
            else:
                return min(
                    recursive(m + 1),
                    recursive(m - 1)
                ) + 1

        return recursive(n)


