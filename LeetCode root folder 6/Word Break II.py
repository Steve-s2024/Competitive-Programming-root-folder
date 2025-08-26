# pretty simple backtrack question: 100%
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        ans = []
        st = set(wordDict)
        strarr = []

        def backtrack(i):
            nonlocal n
            if i >= n:
                ans.append(' '.join(strarr))
                return

            for j in range(i, n):
                if s[i:j + 1] in st:
                    strarr.append(s[i:j + 1])
                    backtrack(j + 1)
                    strarr.pop()

        backtrack(0)
        return ans