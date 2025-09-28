# FUCKING first ever ALL KILL!!!!!, love you leetcode after screwing me up in the past few contests now you finally
# give back what I deserve!

# 2025-09-06 11:27
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0: return 1
        if n in [1, 2]: return 2
        if n in [3, 4]: return 3
        if n in [5, 6]: return 4
        if n == 7: return 5

        le = n.bit_length()
        ans = 1
        for size in range(1, le):
            ans += pow(2, (size - 1) // 2)
        print(ans)
        size = le - 2
        if size % 2 == 0:
            hlf = size // 2
            l, r = 0, (1 << hlf) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                prt = str(bin(m))[2:].zfill(hlf)
                ns = '1' + prt + prt[::-1] + '1'
                ns = int(ns, 2)
                if ns > n:
                    r = m - 1
                else:
                    res = m
                    l = m + 1
            ans += res + 1
        else:  # size%2 == 1
            hlf = size // 2
            l, r = 0, (1 << hlf) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                prt = str(bin(m))[2:].zfill(hlf)
                ns = '1' + prt + '0' + prt[::-1] + '1'
                ns = int(ns, 2)
                if ns > n:
                    r = m - 1
                else:
                    res = m
                    l = m + 1
            ans += res + 1

            l, r = 0, (1 << hlf) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                prt = str(bin(m))[2:].zfill(hlf)
                ns = '1' + prt + '1' + prt[::-1] + '1'
                ns = int(ns, 2)
                if ns > n:
                    r = m - 1
                else:
                    res = m
                    l = m + 1
            ans += res + 1
        return ans
