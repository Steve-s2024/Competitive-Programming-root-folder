# idk what algorithm solution: time-limit exceeded

'''class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        visited = set()
        maxSeqLen = 0

        def matchSeq(seq, text):
            if len(seq) > len(text):
                return False
            if len(seq) == 0:
                return True
            idx = 0
            for c in text:
                if c == seq[idx]:
                    idx += 1
                    if idx == len(seq):
                        return True
            return False

        def dfs(seq, idx):
            # print(seq)
            nonlocal maxSeqLen
            if seq in visited:
                return
            visited.add(seq)
            if not matchSeq(seq, text2):
                return
            maxSeqLen = max(maxSeqLen, len(seq))
            for i in range(idx, len(text1)):
                dfs(seq + text1[i], i + 1)

        dfs('', 0)

        return maxSeqLen'''


# NeetCode's Idea:1680
# ms
# Beats
# 5.09%

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        visited = {}
        def dfs(idx1, idx2):
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            if (idx1, idx2) in visited:
                return visited[(idx1, idx2)]

            if text1[idx1] == text2[idx2]:
                visited[(idx1, idx2)] =  1 + dfs(idx1 + 1, idx2 + 1)
            else:
                visited[(idx1, idx2)] =  max(
                    dfs(idx1 + 1, idx2),
                    dfs(idx1, idx2 + 1)
                )
            return visited[(idx1, idx2)]
        return dfs(0, 0)
