# funny enough i tried to always return the first element of the set
# for the getRandom method, but somehow leetcode test program consider
# it is incorrect when I return the number continuously for over 100 times...
# wonder how the program really judge: 89%
class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.hashMap = {}

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        self.arr.append(val)
        self.hashMap[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False
        idx = self.hashMap.pop(val)
        if idx != len(self.arr)-1:
            a, b = self.arr[idx], self.arr[-1]
            self.arr[idx] = b
            self.arr[-1] = a
            self.hashMap[b] = idx
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        n = len(self.arr)
        idx = int(n*random.random())
        return self.arr[idx]