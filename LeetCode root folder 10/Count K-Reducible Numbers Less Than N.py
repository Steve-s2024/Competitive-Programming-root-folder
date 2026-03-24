# pretty generic digit dp... with pop count depth
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        def helper(n):
            res = 0
            while n > 1: n, res = n.bit_count(), res+1
            return res

        M = 10**9 + 7
        n = len(s)
        @cache
        def fn(i, f, x):
            if i >= n: return 1 if helper(x) < k and not f else 0

            res = fn(i+1, f and s[i]=='0', x)
            if not f or s[i] == '1': res += fn(i+1, f, x+1)
            return res%M
        return fn(0, 1, 0)-1

