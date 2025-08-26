# pretty simple implementation and good use of bitmask to reduce time complexity: 23%
class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        mp = {}
        mask = 0
        res = 0

        for i in range(n):
            if mask not in mp: mp[mask] = i
            mask ^= 1<<(int(s[i]))
            # print(mask)
            if mask in mp: res = max(res, i-mp[mask]+1)
            for j in range(10):
                cur = mask^(1<<j)
                if cur in mp:
                    res = max(res, i-mp[cur]+1)
        return res