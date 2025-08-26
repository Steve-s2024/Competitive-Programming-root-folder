# 38%
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mp = {}
        mp[0] = -1
        mask = 0
        res = 0
        for i, c in enumerate(s):
            if c in 'aeiou':
                num = ord(c)-ord('a')
                mask ^= 1<<num
            if mask in mp: res = max(res, i-mp[mask])
            if mask not in mp: mp[mask] = i
        return res