# two pointer solution, a few details need to pay extra
# attention: 40%
class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        l, r = 0, n-1
        while r >= l and s[l] == s[r]:
            if r-l == 0:
                return 1
            cur = s[l]
            while l < n and s[l] == cur:
                l += 1
            while r >= 0 and s[r] == cur:
                r -= 1
        return max(r-l+1, 0)