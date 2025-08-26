# DP my ass, I crushed this question with hash map: 27%
class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        mp = defaultdict(list)
        for i in range(n):
            if s[i] not in mp: mp[s[i]].append(-1)
            mp[s[i]].append(i)

        res = 0
        for val in mp.values():
            for i in range(1, len(val)):
                a, b = val[i-1], val[i]
                l, r = b-a, n-b
                res += l*r
        # print(res)
        return res