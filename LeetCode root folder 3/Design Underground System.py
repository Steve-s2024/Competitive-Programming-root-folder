# can't believe this is so fast: 99.66%
class UndergroundSystem:

    def __init__(self):
        self.mp1 = {} # mp.key --> (src, dst), mp.val --> (totalTime, count)
        self.mp2 = {} # mp2.items --> (id, (src station, enter time))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.mp2[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        src, srcT = self.mp2.pop(id)
        dst, dstT = stationName, t
        key = (src, dst)
        time = dstT - srcT
        if key not in self.mp1:
            self.mp1[key] = [time, 1]
        else:
            self.mp1[key][0] += time
            self.mp1[key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.mp1[(startStation, endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)