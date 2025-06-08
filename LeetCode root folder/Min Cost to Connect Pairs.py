



# discarded solution. does not match the question's requirement
'''class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hashSet = set()
        for x, y in points:
            hashSet.add((x, y))


        def findPoint(coor):
            x, y = coor[0], coor[1]
            idx = 1
            while True:
                for i in range(idx+1):
                    if (x + i, y + idx-i) in hashSet:
                        return (x+i, y+idx-i)
                    elif (x - i, y + idx-i) in hashSet:
                        return (x-i, y+idx-i)
                    elif (x + i, y - idx+i) in hashSet:
                        return (x+i, y-idx+i)
                    elif (x - i, y - idx+i) in hashSet:
                        return (x-i, y-idx+i)
                idx += 1


        visited = set()
        totalCost = 0
        for x, y in points:
            if (x, y) not in visited:
                point2 = findPoint((x, y))
                totalCost += abs(x - point2[0]) + abs(y - point2[1])
                visited.add((x, y))
                visited.add((point2[0], point2[1]))
        return totalCost'''