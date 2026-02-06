# was afraid this may not work, but no more worry. learned a few things about writing palindrome manipulation
# and n^2 algorithm of finding all palindromes.
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n = len(s)

        def helper(s):
            n = len(s)
            mp = [1] * n
            for i in range(n):
                l, r = i, i
                while l > 0 and r < n - 1 and s[l - 1] == s[r + 1]:
                    l, r = l - 1, r + 1
                    mp[l] = max(mp[l], r - l + 1)
                if i:
                    l, r = i, i - 1
                    while l > 0 and r < n - 1 and s[l - 1] == s[r + 1]:
                        l, r = l - 1, r + 1
                        mp[l] = max(mp[l], r - l + 1)
            return mp

        mp = helper(s)
        t = t[::-1]
        ref = helper(t)
        # print(ref)
        m = len(t)
        trie = {'*': 0}
        for i in range(m):
            cr = trie
            for j in range(i, m):
                if t[j] not in cr: cr[t[j]] = {'*': 0}
                cr = cr[t[j]]
                cr['*'] = max(cr['*'], (ref[j + 1] if j < m - 1 else 0))

        # print(trie)
        ans = max(mp + ref)
        for i in range(n):
            cr = trie
            for j in range(i, n):
                if s[j] not in cr: break
                cr = cr[s[j]]
                res = 2 * (j - i + 1) + max(mp[j + 1] if j < n - 1 else 0, cr['*'])
                ans = max(ans, res)
        return ans
