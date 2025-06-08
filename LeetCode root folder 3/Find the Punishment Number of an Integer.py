# enumeration and recursive solution:55%
class Solution:
    def recursive(self, s, i, sm, tar):
        if i >= len(s):
            return sm == tar
        for j in range(i, len(s)):
            if self.recursive(s, j+1, sm+int(s[i:j+1]), tar):
                return True
        return False

    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            if self.recursive(str(i*i), 0, 0, i):
                print(i)
                ans += i*i
        return ans