# fking stupid question make me feel bad! but the moment that i realize its trickery i laughed so badly:0
# ms
# Beats
# 100.00%
# what a trick question.
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return 2
            l += 1
            r -= 1
        return 1