# NeetCode recommended solution, absolutely an ingenious idea using trie with (word[i], word[len(word)-i-1) as the
# key: 18%
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = {}
        res = 0
        for word in words[::-1]:
            cur = trie
            for i in range(len(word)):
                a, b = word[i], word[len(word) - i - 1]
                if (a, b) not in cur: break
                cur = cur[(a, b)]
            else:
                res += cur['val']

            cur = trie
            for i in range(len(word)):
                a, b = word[i], word[len(word) - i - 1]
                if (a, b) not in cur: cur[(a, b)] = {}
                cur = cur[(a, b)]
                if 'val' not in cur: cur['val'] = 0
                cur['val'] += 1

        return res