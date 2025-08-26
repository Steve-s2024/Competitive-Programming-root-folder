# why the several consecutive 2100 question are so easy?: 54%
class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)

        @cache
        def recursive(i, b, e):
            nonlocal n
            if i >= n: return 0
            a = recursive(i + 1, b, words[i][-1]) - (1 if words[i][0] == e else 0)
            b = recursive(i + 1, words[i][0], e) - (1 if words[i][-1] == b else 0)
            return min(a, b) + len(words[i])

        return recursive(1, words[0][0], words[0][-1]) + len(words[0])