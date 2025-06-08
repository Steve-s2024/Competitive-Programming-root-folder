class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hashMap = defaultdict(int)
        res = 0
        for w, h in rectangles:
            ratio = float(w) / h
            if ratio in hashMap:
                res += hashMap[ratio]
            hashMap[ratio] += 1
        return int(res)
