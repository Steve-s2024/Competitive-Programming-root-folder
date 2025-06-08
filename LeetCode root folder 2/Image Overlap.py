# brute force with optimization: 5%
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        res = 0
        n = len(img1)
        for offsetR in range(n):
            for offsetC in range(n):
                a = self.getOverlap(img1, img2, offsetR, offsetC, n)
                b = self.getOverlap(img1, img2, offsetR, -offsetC, n)
                c = self.getOverlap(img1, img2, -offsetR, offsetC, n)
                d = self.getOverlap(img1, img2, -offsetR, -offsetC, n)
                res = max(res, a, b, c, d)
        return res

    def getOverlap(self, matrix1, matrix2, offsetR, offsetC, n):
        res = 0
        for r in range(max(offsetR, 0), min(n+offsetR, n)):
            for c in range(max(offsetC, 0), min(n+offsetC, n)):
                R, C = r-offsetR, c-offsetC
                if R in range(n) and C in range(n):
                    res += matrix1[R][C] * matrix2[r][c]
        return res


# brute force: TLE
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        res = 0
        n = len(img1)
        for offsetR in range(n):
            for offsetC in range(n):
                a = self.getOverlap(img1, img2, offsetR, offsetC, n)
                b = self.getOverlap(img1, img2, offsetR, -offsetC, n)
                c = self.getOverlap(img1, img2, -offsetR, offsetC, n)
                d = self.getOverlap(img1, img2, -offsetR, -offsetC, n)
                res = max(res, a, b, c, d)
        return res

    def getOverlap(self, matrix1, matrix2, offsetR, offsetC, n):
        res = 0
        for r in range(n):
            for c in range(n):
                R, C = r-offsetR, c-offsetC
                if R in range(n) and C in range(n):
                    res += matrix1[R][C] * matrix2[r][c]
        return res

