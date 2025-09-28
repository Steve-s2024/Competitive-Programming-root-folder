# so hard to understand KMP man! the confusion is always the line l = lps[l-1]. couldn't understand this line only
# but the intuition using kmp on all the parts separate by '*' comes up very fast in this problem: 61%
class Solution:
    def kmp(self, s1, s2):
        n, m = len(s1), len(s2)
        lps = [0] * m
        l = 0
        for i in range(1, m):
            while s2[i] != s2[l] and l: l = lps[l - 1]
            if s2[i] == s2[l]:
                l += 1
                lps[i] = l
        # print(lps)
        res = []
        l = 0
        for i in range(n):
            while s1[i] != s2[l] and l: l = lps[l - 1]
            if s1[i] == s2[l]:
                l += 1
                if l == m:
                    res.append((i - l + 1, i))
                    l = lps[l - 1]
        # print(res)
        return res

    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        cands = p.split('*')
        tmp = []
        for cand in cands:
            if cand: tmp.append(cand)
        cands = tmp
        if len(cands) == 0: return 0

        qs = []
        for cand in cands:
            q = deque(self.kmp(s, cand))
            qs.append(q)
        # print(qs)
        def recursive(strt, i):
            if i == len(qs): return strt
            while qs[i] and qs[i][0][0] < strt: qs[i].popleft()
            if qs[i]: return recursive(qs[i][0][1] + 1, i + 1)
            return inf

        res = inf
        for l, r in qs[0]:
            end = recursive(r + 1, 1)
            # print(l, end)
            res = min(res, end - l)
        return res if res != inf else -1