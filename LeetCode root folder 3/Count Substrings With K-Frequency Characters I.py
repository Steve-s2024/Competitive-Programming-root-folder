# i wrote the brute force solution, and it passed, but i still
# want to write the optimal..., linear solution with
# hashing and sliding window: 98%
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        mp = defaultdict(int)
        maxCnt = 0
        l, r = 0, 0
        while r < n or (l < n and maxCnt):
            while r < n and not maxCnt:
                mp[s[r]] += 1
                if mp[s[r]] >= k:
                    maxCnt += 1
                r += 1
            # print(l, r)

            if maxCnt:
                res += n - r + 1
                if mp[s[l]] == k:
                    maxCnt -= 1
                mp[s[l]] -= 1
                l += 1

        return res