# very hard, solved independently. the first barrier is to realize the string is a valid parenthesis expression
# then use a mp to denote the close parenthesis of every open parenthesis. at the end just do recursive and construct
# the binary string greedily: 100%
# 2300 rated
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        n = len(s)
        stk = []
        mp = [0]*n
        for i in range(n):
            if s[i] == '1': stk.append(i)
            else: mp[stk.pop()] = i

        def recursive(l, r):
            nonlocal s
            if l+1 == r:
                return s[l:r+1]
            L = l+1
            res = []
            while L < mp[l]:
                a = recursive(L, mp[L])
                res.append(a)
                L = mp[L]+1
            res.sort(reverse = True)
            res = ['1'] + res + ['0']
            return ''.join(res)
        strarr = []
        l = 0
        while l < n:
            strarr.append(recursive(l, mp[l]))
            l = mp[l] + 1
        strarr.sort(reverse = True)
        return ''.join(strarr)