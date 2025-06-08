# Trie solution:59
# ms
# Beats
# 63.19%
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = {}
        for word in words:
            cur = trie
            for c in word[::-1]:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['end'] = True

        # print(trie)
        def dfs(cur, length):
            if 'end' in cur and len(cur) == 1:
                # length is the length of the word, and add one to it to represent the #
                return length + 1
            res = 0
            for next_ in cur.values():
                if next_ != True:
                    res += dfs(next_, length + 1)
            return res

        return dfs(trie, 0)
