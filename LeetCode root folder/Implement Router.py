# this question absolutely makes no sense.

class Router:

    def __init__(self, memoryLimit: int):
        self.memLimit = memoryLimit
        self.q = deque()
        self.hashSet = set()
        self.hashMap = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        t = (source, destination, timestamp)
        if t in self.hashSet:
            return False

        self.hashSet.add(t)
        if destination not in self.hashMap:
            self.hashMap[destination] = defaultdict(int)
        self.hashMap[destination][timestamp] += 1

        self.q.append(t)
        if len(self.q) > self.memLimit:
            t = self.q.popleft()
            self.hashMap[t[1]][t[2]] -= 1
            if self.hashMap[t[1]][t[2]] == 0:
                del self.hashMap[t[1]][t[2]]
            self.hashSet.remove(t)
        return True

    def forwardPacket(self) -> List[int]:
        if self.q:
            t = self.q.popleft()
            self.hashSet.remove(t)
            self.hashMap[t[1]][t[2]] -= 1
            if self.hashMap[t[1]][t[2]] == 0:
                del self.hashMap[t[1]][t[2]]
            return list(t)
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        res = 0
        for key, val in self.hashMap[destination].items():
            if key in range(startTime, endTime + 1):
                res += val
        return res

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)©leetcode