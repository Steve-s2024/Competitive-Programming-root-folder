# hashing solution: 8%
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        mp1, mp2 = defaultdict(int), Counter(s)
        n = len(s)
        res = set()
        for i in range(n):
            mp2[s[i]] -= 1
            for lt in mp1:
                if mp1[lt] and mp2[lt]:
                    res.add(lt + s[i] + lt)
            mp1[s[i]] += 1
        # print(res)
        return len(res)
