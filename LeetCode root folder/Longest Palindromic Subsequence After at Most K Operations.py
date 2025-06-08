# brute-force: tle
class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        def cost(s):
            res = 0
            l, r = 0, len(s)-1
            while l < r:
                n1, n2 = ord(s[l]), ord(s[r])
                res += min(
                    abs(n1 - n2),
                    n1 - ord('a') + ord('z') - n2 + 1,
                    n2 - ord('a') + ord('z') - n1 + 1
                )
                l += 1
                r -= 1
            # print(s, res)
            return res

        res = 0

        def recursive(idx, subs):
            nonlocal res
            if idx >= len(s):
                # print(subs)
                if len(subs) > res and cost(subs) <= k:
                    res = len(subs)
                return
            for i in range(idx, len(s)):
                recursive(i+1, subs + s[i])
            recursive(len(s), subs)
        recursive(0, '')
        return res


