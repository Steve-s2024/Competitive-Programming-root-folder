#19%
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        distinctX = len(set([e[0] for e in coordinates]))
        if distinctX == 1:
            return True
        n = len(coordinates)
        if distinctX < n:
            return False
        a, b = coordinates[0], coordinates[1]
        slope = (a[1] - b[1]) / (a[0] - b[0])
        for i in range(2, n):
            b = coordinates[i]
            curSlope = (a[1] - b[1]) / (a[0] - b[0])
            if curSlope != slope:
                return False
        return True