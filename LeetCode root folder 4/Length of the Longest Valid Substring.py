# this is so far the highest rated problem solved on zerotrac: 2203
#: 25%
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        st = set(forbidden)

        s = []
        l, r = 0, 0
        res = 0
        for i in range(n):
            s.append(word[i])
            if len(s) > 10:
                s.pop(0)
            for i in range(len(s)-1, -1, -1):
                if ''.join(s[i:]) in st:
                    s = s[i+1:]
                    l = r-len(s)+1
                    break
            # print(l, r)
            res = max(res, r-l+1)
            r += 1
        return res