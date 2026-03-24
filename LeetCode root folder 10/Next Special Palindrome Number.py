# I am such a gambler. not until it pass all testcases I did not know this has a good time complexity
# I did this just because no other approaches come to my mind, and this approach has a time complexity
# which hard to analyze but feels not too much.

class Solution:
    def specialPalindrome(self, n: int) -> int:
        if n == 0: return 1
        S = str(n)
        m = len(S)
        if m == 1: return 22
        @cache
        def fn(msk, i, re):
            nonlocal m
            s = list(str(msk).zfill(m//2))
            if i >= 10:
                # print(s)
                x = 0
                for j in range(m//2):
                    if s[j] == '0': x += 1
                x = 2*x+(m%2)
                if x >= 10 or str(x) in s: return 1<<63
                for j in range(m//2):
                    if s[j] == '0': s[j] = str(x)
                res = ''.join(s)
                res = int(res + str(x)*(m%2) + res[::-1])
                return res if res > n else (1<<63)

            if re == 0: return fn(msk, i+2, i+2)
            res = fn(msk, i+2, i+2) if re == i else (1<<63)
            for j in range(m//2):
                if s[-j-1] == '0': res = min(res, fn(msk+i*10**j, i, re-2))
            return res
        ans = fn(0, 2, 2)
        # print(ans)
        if ans == 1<<63:
            n = 10**m
            S = str(n)
            m = len(S)
            fn.cache_clear()
            return fn(0, 2, 2)

        return ans
