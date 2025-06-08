# does not deserve the difficulty at all: 77.24%

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        rectangles.sort(key = lambda i : i[0])
        res = 0
        prev = -1
        for x1, y1, x2, y2 in rectangles:
            if prev <= x1:
                res += 1
            prev = max(prev, x2)
        if res >= 3:
            return True
        
        rectangles.sort(key = lambda i : i[1])
        res = 0
        prev = -1
        for x1, y1, x2, y2 in rectangles:
            if prev <= y1:
                res += 1
            prev = max(prev, y2)
        if res >= 3:
            return True
        
        return False