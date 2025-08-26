# about right difficulty, good for consolidating DP technique, not very unorthodox solution: 43%
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])
        mp = [[0] * 26 for _ in range(n)]
        for word in words:
            for i, c in enumerate(word):
                o = ord(c) - ord('a')
                mp[i][o] += 1

        m = len(target)
        MOD = 10 ** 9 + 7

        @cache
        def recursive(i, j):
            nonlocal n, m, MOD
            if i >= m: return 1
            if j >= n: return 0
            o = ord(target[i]) - ord('a')
            res = recursive(i, j + 1)
            if mp[j][o]:
                res += recursive(i + 1, j + 1) * mp[j][o]
            res %= MOD
            return res

        return recursive(0, 0)
