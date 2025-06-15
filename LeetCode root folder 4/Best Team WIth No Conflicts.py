# recursive and DP: 5%
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        mp = defaultdict(list)
        arr = sorted(list(set(ages)))
        for i in range(n): mp[ages[i]].append(scores[i])
        for val in mp.values(): val.sort()

        @cache
        def recursive(i, mxScore):
            if i >= len(arr): return 0
            age = arr[i]
            l, r = 0, len(mp[age]) - 1
            idx = r + 1
            while l <= r:
                m = (l + r) // 2
                if mp[age][m] >= mxScore:
                    idx = m
                    r = m - 1
                else:
                    l = m + 1

            res = recursive(i + 1, mxScore)
            tot = 0
            for j in range(idx, len(mp[age])):
                tot += mp[age][j]
                a = recursive(i + 1, mp[age][j]) + tot
                res = max(a, res)
            return res

        return recursive(0, 0)