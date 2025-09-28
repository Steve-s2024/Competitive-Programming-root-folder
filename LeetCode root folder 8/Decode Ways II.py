# you actually need to do every possibilities in a state manually, which is pretty annoying DP implementation: 22%

class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)

        @cache
        def recursive(i):
            nonlocal MOD, n
            if i >= n: return 1
            res = 0
            if '1' <= s[i] <= '9': res += recursive(i + 1)
            if i < n - 1 and '*' not in [s[i], s[i + 1]] and 10 <= int(s[i] + s[i + 1]) <= 26: res += recursive(i + 2)
            if s[i] == '*':
                res += 9 * recursive(i + 1)
                if i < n - 1:
                    if '0' <= s[i + 1] <= '9': res += recursive(i + 2)
                    if '0' <= s[i + 1] <= '6': res += recursive(i + 2)
                    if s[i + 1] == '*': res += 9 * recursive(i + 2) + 6 * recursive(i + 2)
            elif i < n - 1 and s[i + 1] == '*':
                if s[i] == '1': res += 9 * recursive(i + 2)
                if s[i] == '2': res += 6 * recursive(i + 2)
            return res % MOD

        return recursive(0)