# weekly contest 448 Q3
# my humble solution, which obviously didn't work, this contest Q3 and 4 is
# simply at another level, probably be around 2500 to 2700
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        for kk in range(k):
            n = len(position)
            diff = []
            for i in range(1, n):
                diff.append(position[i] - position[i - 1])

            res = 0
            minChange = float('inf')
            for i in range(1, n - 2):
                a, b = diff[i], diff[i + 1]
                c, d = time[i], time[i + 1]
                minChange = min(a * d + b * c, minChange)

            for i in range(1, n - 2):
                a, b = diff[i], diff[i + 1]
                c, d = time[i], time[i + 1]
                if a * d + b * c == minChange:
                    position.pop(i)
                    tmp = time.pop(i)
                    time[i] += tmp

        # print(position)
        # print(time)
        n = len(position)
        res = 0
        for i in range(1, n):
            dst = position[i] - position[i - 1]
            t = dst * time[i - 1]
            res += t
        return res
        ©leetcode