class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        zeros = []
        ones = []
        r, l = 0, 0
        while r < len(s):
            while r < len(s) and s[r] == '1':
                r += 1
            if r > l:
                ones.append(r - l)
                l = r
            while r < len(s) and s[r] == '0':
                r += 1
            if r > l:
                zeros.append(r - l)
                l = r

        # print(zeros)
        # print(ones)
        if len(zeros) == 1:
            return sum(ones)
        res = 0
        for i in range(len(zeros) - 1):
            res = max(res, zeros[i] + zeros[i + 1])
        return res + sum(ones)

        ©leetcode