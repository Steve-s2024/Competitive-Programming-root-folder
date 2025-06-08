# brute-force solution: TLE
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        # brute-force
        def findOverlap(coor1, coor2):
            hor, ver = 0, 0
            if coor1[0] in range(coor2[0], coor2[2]):
                hor = min(coor1[2], coor2[2]) - coor1[0]
            elif coor1[2] in range(coor2[0] + 1, coor2[2] + 1):
                hor = coor1[2] - max(coor1[0], coor2[0])

            if coor1[1] in range(coor2[1], coor2[3]):
                ver = min(coor1[3], coor2[3]) - coor1[1]
            elif coor1[3] in range(coor2[1] + 1, coor2[3] + 1):
                ver = coor1[3] - max(coor1[1], coor2[1])

            if hor == 0 or ver == 0:
                tmp = coor1
                coor1 = coor2
                coor2 = tmp
                if coor1[0] in range(coor2[0], coor2[2]):
                    hor = min(coor1[2], coor2[2]) - coor1[0]
                elif coor1[2] in range(coor2[0] + 1, coor2[2] + 1):
                    hor = coor1[2] - max(coor1[0], coor2[0])

                if coor1[1] in range(coor2[1], coor2[3]):
                    ver = min(coor1[3], coor2[3]) - coor1[1]
                elif coor1[3] in range(coor2[1] + 1, coor2[3] + 1):
                    ver = coor1[3] - max(coor1[1], coor2[1])

            return min(hor, ver) ** 2

        maxArea = 0
        for i in range(len(bottomLeft)):
            for j in range(len(bottomLeft)):
                if j == i:
                    continue
                res = findOverlap(bottomLeft[i] + topRight[i], bottomLeft[j] + topRight[j])
                maxArea = max(maxArea, res)
        return maxArea

