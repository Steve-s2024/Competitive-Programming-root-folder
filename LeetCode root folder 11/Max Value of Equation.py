# a few simple observation and a little change of the equation. solved under 20 minutes, this is not 2456 this is ~2200
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        n = len(points)
        mi = min(e[0] for e in points)
        for i in range(n): points[i][0] += mi

        j = n - 1
        hp = [-points[-1][1] - points[-1][0]]
        mp = defaultdict(int)
        mp[-hp[0]] = 1
        res = -inf
        for i in range(n - 2, -1, -1):
            while points[j][0] - points[i][0] > k:
                mp[sum(points[j])] -= 1
                j -= 1

            # print(mp)
            while hp and mp[-hp[0]] == 0: heappop(hp)
            # print(hp, j)
            if hp: res = max(res, points[i][1] - points[i][0] + -hp[0])
            heappush(hp, -sum(points[i]))
            mp[sum(points[i])] += 1
        return res
