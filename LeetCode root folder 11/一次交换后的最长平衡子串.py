# 写着东西快把我弄死了
class Solution:
    def longestBalanced(self, s: str) -> int:
        if '1' not in s: return 0
        if '0' not in s: return 0
        n = len(s)

        ar = [1 if c == '1' else -1 for c in s]
        res = 0


        fz, fo = s.index('0'), s.index('1')
        mp = {0:n}
        x = 0
        for i in range(n - 1, -1, -1):
            x += ar[i]
            if x in mp: res = max(res, mp[x] - i)
            if x - 2 in mp and i > fz: res = max(res, mp[x - 2] - i)  # good, 0 exist
            if x + 2 in mp and i > fo: res = max(res, mp[x + 2] - i)  # good, 1 exist

            if x not in mp: mp[x] = i
        lz, lo = s.rindex('0'), s.rindex('1')
        x = 0
        mp = {0:-1}
        for i in range(n):
            x += ar[i]
            if x in mp: res = max(res, i - mp[x])
            if x - 2 in mp and i < lz: res = max(res, i - mp[x - 2])  # good, 0 exist
            if x + 2 in mp and i < lo: res = max(res, i - mp[x + 2])  # good, 1 exist
            # print(i, res)

            if x not in mp: mp[x] = i
        return res
©leetcode