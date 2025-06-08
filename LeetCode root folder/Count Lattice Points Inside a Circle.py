# this is the first time ever where the brute-force solution actually passed with average speed...:1644
# ms
# Beats
# 63.92%
# then, the question should be deleted because it can't contribute to coder improvement.
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = 0
        xMax = 0
        yMax = 0
        for x, y, radius in circles:
            xMax = max(xMax, x+radius)
            yMax = max(yMax, y+radius)

        for r in range(yMax+1):
            for c in range(xMax+1):
                for x, y, radius in circles:
                    dist = math.sqrt((r-y)**2 + (c-x)**2)
                    if dist <= radius:
                        res += 1
                        break
        return res


# I also adjusted the solution by sorting the circle input array to store the circle's radius in descending order:
# 742
# ms
# Beats
# 91.24%
'''class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        circles.sort(key = lambda i : i[2], reverse=True)
        res = 0
        xMax = 0
        yMax = 0
        for x, y, radius in circles:
            xMax = max(xMax, x+radius)
            yMax = max(yMax, y+radius)

        for r in range(yMax+1):
            for c in range(xMax+1):
                for x, y, radius in circles:
                    dist = math.sqrt((r-y)**2 + (c-x)**2)
                    if dist <= radius:
                        res += 1
                        break
        return res'''