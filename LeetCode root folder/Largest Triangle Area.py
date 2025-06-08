# boring question:56
# ms
# Beats
# 34.63%
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    a, b, c = points[i], points[j], points[k]
                    area = 1/2 * abs( a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1]) )
                    maxArea = max(maxArea, area)
        return maxArea