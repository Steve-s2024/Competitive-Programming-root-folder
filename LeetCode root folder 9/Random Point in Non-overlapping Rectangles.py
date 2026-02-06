# random point in rectangle algorithm, can be generalized to random point in all shape
# it uses area of individual rectangle as weight when randomly picking which rectangle the point fall in (obvious)
# seeing it work just strengthen my belief in the weight by area concept of randomization (good to see it in practice)
class Solution:

    def __init__(self, rects: List[List[int]]):
        x = 0
        ar = []
        for a, b, c, d in rects:
            l, w = c-a+1, d-b+1
            ar.append((x+1, x+l*w, a, b, c, d))
            x += l*w
        self.x = x
        self.ar = ar

    def pick(self) -> List[int]:
        x = self.x
        ar = self.ar
        t = randint(1, x)
        l, r = 0, len(ar)-1
        res = -1
        while l <= r:
            m = (l+r)//2
            if t in range(ar[m][0], ar[m][1]+1):
                res = m
                break
            elif t < ar[m][0]: r = m-1
            else: l = m+1
        _, _, a, b, c, d = ar[res]
        x, y = a+randint(0, c-a), b+randint(0, d-b)
        return [x, y]


