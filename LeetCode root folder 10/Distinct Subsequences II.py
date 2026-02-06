# a general approach to count the number of unique subsequences DP & greedy
# similar strategy applied also to LC.1987

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        mod = 10 ** 9 + 7

        mp = [-1] * 26
        for j in range(26): mp[j] = s.rfind(chr(ord('a') + j))
        # print(mp)
        @cache
        def fn(i, t):
            nonlocal mod, n
            if i >= n: return 0
            if t == s[i]:
                res = 0
                for j in range(26):
                    res += fn(i + 1, chr(ord('a')+j)) if mp[j] > i else 0
                    res %= mod
            else:
                res = fn(i + 1, t) - 1
            # print(i, res)
            return (res + 1) % mod

        return sum(fn(0, chr(ord('a') + j)) for j in range(26)) % mod