# at first, I thought first half of the problem is about storing the first and last index of each character,
# it failed on testcase "abab", then thought only about interval merging, which also failed after several attempts
# check the hint and it turns out the thing I and trying to do can be categorized as a graph problem (not straightforward)
# so, first half (where the challenge lies) is graph, second half (standard knapsack and restoration of sequence) is just
# generic.

# the second part is actually very unnecessary, once the first half give the result of the hash map, the rest
# can be done greedily
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        mp = {}
        for i, e in enumerate(s):
            if e not in mp: mp[e] = [i, i]
            mp[e][1] = i

        g = defaultdict(list)
        for c in mp:
            l, r = mp[c]
            for C in set(list(s[l:r + 1])):
                if C != c: g[c].append(C)

        def dfs(u):
            L, R = mp[u]
            for v in g[u]:
                if v in vs: continue
                vs.add(v)
                l, r = dfs(v)
                L, R = min(l, L), max(r, R)
            return L, R

        ref = {}
        for c in mp:
            vs = {c}
            l, r = dfs(c)
            ref[l] = r
        mp = ref

        # print(mp)
        # return

        @cache
        def recursive(i):
            nonlocal n
            if i >= n: return 0, 0
            ct, ln = recursive(i + 1)
            res = [ct, ln]
            if i in mp:  # jump to right end
                CT, LN = recursive(mp[i] + 1)
                CT += 1
                LN += mp[i] - i + 1
                if CT > ct or CT == ct and LN < ln: res = [CT, LN]
            return res

        recursive(0)
        res = []
        i = 0
        s = list(s)
        while i < n:
            ct, ln = recursive(i + 1)
            if i in mp:
                CT, LN = recursive(mp[i] + 1)
                CT += 1
                LN += mp[i] - i + 1
                if CT > ct or CT == ct and LN < ln:
                    ar = [s[j] for j in range(i, mp[i] + 1)]
                    res.append(''.join(ar))
                    i = mp[i]
            i += 1
        return res