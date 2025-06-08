# greedy solution:201
# ms
# Beats
# 15.50%
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        diffs = []
        for i in range(len(s)):
            if s[i] != t[i]:
                if ord(t[i]) > ord(s[i]):
                    diff = ord(t[i])-ord(s[i])
                else:
                    diff = ord('z')-ord(s[i])+(ord(t[i])-ord('a')) + 1
                diffs.append(diff)
        # print(diffs)
        if len(diffs) == 0:
            return True
        for key, val in Counter(diffs).items():
            if k < key+((val-1)*26):
                return False
        return True