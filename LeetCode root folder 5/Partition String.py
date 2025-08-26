# quite challenging for a Q1

class Solution:
    def partitionString(self, s: str) -> List[str]:
        trie = {}
        n = len(s)
        cur = trie
        strarr = []
        ans = []
        for i in range(n):

            c = s[i]
            strarr.append(c)
            if c not in cur:
                cur[c] = {}
                cur = trie
                ans.append(''.join(strarr))
                strarr.clear()
            else:
                cur = cur[c]

        return ans