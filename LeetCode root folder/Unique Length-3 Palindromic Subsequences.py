# brute force: TLE

'''class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # brute-force
        count = 0
        hashSet = set()

        def backtrack(i, seq):
            nonlocal count, s
            if len(seq) >= 3:
                if seq not in hashSet and seq[0] == seq[2]:
                    hashSet.add(seq)
                    count += 1
                return
            if i >= len(s):
                return
            backtrack(i + 1, seq + s[i])
            backtrack(i + 1, seq)

        backtrack(0, '')
        return count

'''


