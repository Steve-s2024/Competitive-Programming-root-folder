# sliding window solution:274
# ms
# Beats
# 20.29%
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = 0
        l, r = 0, 0
        res = 0
        while r < len(answerKey):
            if answerKey[r] == 'F':
                count += 1
            while count > k:
                if answerKey[l] == 'F':
                    count -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        count = 0
        l, r = 0, 0
        while r < len(answerKey):
            if answerKey[r] == 'T':
                count += 1
            while count > k:
                if answerKey[l] == 'T':
                    count -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res

