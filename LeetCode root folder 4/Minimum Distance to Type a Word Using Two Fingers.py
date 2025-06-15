# kanp-sack, and keeping track of the state (i, f1, f2): 59%

class Solution:
    def __init__(self):
        self.mp = {}
        mp = self.mp
        cnt = 0
        for i in range(5):
            for j in range(6):
                mp[chr(ord('A') + cnt)] = (i, j)
                cnt += 1

    def helper(self, a, b):
        mp = self.mp
        x1, y1 = mp[a]
        x2, y2 = mp[b]
        return abs(x1 - x2) + abs(y1 - y2)

    def minimumDistance(self, word: str) -> int:
        n = len(word)

        @cache
        def recursive(i, f1, f2):
            nonlocal n
            if i >= n: return 0, 0

            a, b = recursive(i + 1, word[i], f2)
            res1 = (a + (0 if f1 == '' else self.helper(f1, word[i])), b)

            a, b = recursive(i + 1, f1, word[i])
            res2 = (a, b + (0 if f2 == '' else self.helper(f2, word[i])))

            if sum(res1) < sum(res2): return res1
            return res2

        return sum(recursive(0, '', ''))
