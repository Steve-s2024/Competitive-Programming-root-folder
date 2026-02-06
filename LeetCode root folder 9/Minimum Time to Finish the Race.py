# damn not a bad one, log trick solution

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        n = len(tires)
        mi = min(e[0] for e in tires)
        cap = mi * (changeTime - 1) * numLaps

        ar = [inf]
        mp = [[e[0], e[0]] for e in tires]
        while 1:
            mi = min([e[1] for e in mp])
            if mi == inf: break
            ar.append(mi)
            for i in range(n):
                if mp[i][0] > cap:
                    mp[i][1] = inf
                    continue
                mp[i][0] *= tires[i][1]
                mp[i][1] += mp[i][0]

        # print(ar)
        @cache
        def recursive(i):
            nonlocal numLaps, changeTime
            if i >= numLaps: return 0
            res = inf
            for j in range(1, min(len(ar), numLaps - i + 1)):
                a = recursive(i + j) + ar[j] + (changeTime if i != 0 else 0)
                res = min(res, a)
            return res

        return recursive(0)
