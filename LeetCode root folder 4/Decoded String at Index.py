# a bit nerve-racking, sign~: 100%
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        res = ''
        def recursive(i, tot):
            nonlocal k, res
            if tot >= k:
                return
            # print(tot, s[i])
            if s[i] in '23456789':
                if recursive(i+1, tot*int(s[i])): return True
                k = k%tot
                if k == 0: k = tot
            else:
                if recursive(i+1, tot+1): return True
                if tot == k-1:
                    res = s[i]
                    return True
        recursive(0, 0)
        return res