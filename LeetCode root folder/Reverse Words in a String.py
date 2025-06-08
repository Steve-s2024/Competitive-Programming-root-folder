# this is actually pretty easy...


class Solution:
    def reverseWords(self, s: str) -> str:
        # brute-force
        idx = 0
        word = ''
        words = []
        while idx < len(s):
            if s[idx] != ' ':
                word += s[idx]
            elif len(word) != 0:
                words.append(word)
                word = ''
            idx += 1
        if len(word):
            words.append(word)
        # print(words[::-1])
        return ' '.join(words[::-1])