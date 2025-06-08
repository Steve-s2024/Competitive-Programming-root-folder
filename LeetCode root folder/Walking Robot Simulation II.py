# broing hashing solution...: 87%
class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.parameter = 2*self.width + 2*(self.height-2)
        self.curDst = 0
        self.dstMap = {}
        self.dirMap = {}
        self.createMaps()
        self.flag = True
        # print(self.dstMap)
        # print(self.dirMap)
    def step(self, num: int) -> None:
        self.flag = False
        self.curDst += num
        self.curDst %= self.parameter        
        

    def getPos(self) -> List[int]:
       [a, b] = self.dstMap[self.curDst]
       return [b-1, a-1]

    def getDir(self) -> str:
        if self.flag:
            return 'East'
        i = self.dirMap[self.curDst]
        mp = ['East','North','West','South']
        return mp[i]

    def createMaps(self):
        dst = 0
        ref = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        r, c = 1, 1
        while dst < self.parameter:
            self.dstMap[dst] = (r, c)
            self.dirMap[dst] = i
            
            if r+ref[i][0] not in range(1, self.height+1) or c+ref[i][1] not in range(1, self.width+1):
                i += 1
            r += ref[i][0]
            c += ref[i][1]
            dst+=1
        self.dirMap[0] = 3
        