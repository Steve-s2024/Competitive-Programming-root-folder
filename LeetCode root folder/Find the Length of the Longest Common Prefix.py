# standard trie solution, very straight forward question:239
# ms
# Beats
# 73.26%
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = {}
        for num in arr1:
            cur = trie
            for c in str(num):
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]

        res = 0
        for num in arr2:
            length = 0
            cur = trie
            for c in str(num):
                if c not in cur:
                    break
                cur = cur[c]
                length+=1
            res = max(res, length)
        return res