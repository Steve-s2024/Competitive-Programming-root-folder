# 100%
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        i = k
        res = 1
        while i < len(word):
            n1, n2 = i, 0
            while n1 < len(word):
                if word[n1] != word[n2]:
                    break
                n1 += 1
                n2 += 1
            else:
                return res
            i += k
            res += 1
        return res