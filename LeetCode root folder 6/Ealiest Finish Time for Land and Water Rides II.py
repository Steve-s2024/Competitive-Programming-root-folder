# pretty simple question for a Q3, but I am too impatient end up make a mistake and cost me one WA
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterDuration)
        mi = inf
        for i in range(n):
            mi = min(mi, landStartTime[i] + landDuration[i])

        res1 = inf
        for i in range(m):
            cur = max(mi, waterStartTime[i]) + waterDuration[i]
            res1 = min(res1, cur)

        mi = inf
        for i in range(m):
            mi = min(mi, waterStartTime[i] + waterDuration[i])

        res2 = inf
        for i in range(n):
            cur = max(mi, landStartTime[i]) + landDuration[i]
            res2 = min(res2, cur)

        return min(res1, res2)