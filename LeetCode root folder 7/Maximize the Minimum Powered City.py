# the name give it away that this is a binary search question: 51%
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        sm = sum(stations)
        left, right = 0, sm + k
        res = 0
        n = len(stations)
        while left <= right:
            m = (left + right) // 2
            arr = stations[:]
            tot = sum(arr[:r])
            tmp = k
            for i in range(n):
                tot += arr[i + r] if i + r < n else 0
                if tot < m:
                    gap = m - tot
                    if i + r < n:
                        arr[i + r] += gap
                    else:
                        arr[-1] += gap
                    tot = m
                    tmp -= gap

                if i - r >= 0: tot -= arr[i - r]
            if tmp >= 0:
                res = m
                left = m + 1
            else:
                right = m - 1

        return res