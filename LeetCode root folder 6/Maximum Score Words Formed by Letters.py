# backtrack: 69%
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        mp = {}
        for word in words:
            tot = 0
            for c in word:
                idx = ord(c) - ord('a')
                tot += score[idx]
            mp[word] = tot
        frq = Counter(letters)

        n = len(words)
        res = 0

        def backtrack(i, tot):
            nonlocal n, res
            if i >= n:
                res = max(tot, res)
                return

            backtrack(i + 1, tot)
            flag = True
            for c in words[i]:
                frq[c] -= 1
                if frq[c] < 0: flag = False
            if flag: backtrack(i + 1, tot + mp[words[i]])
            for c in words[i]:
                frq[c] += 1

        backtrack(0, 0)
        return res