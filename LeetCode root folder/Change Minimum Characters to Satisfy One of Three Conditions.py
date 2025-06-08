# brute-force solution, it surprises me how 
# a brute-force and greedy solution can get
# so fast, only 2% of the submission are less
# then me: 100%
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        self.mp1, self.mp2 = Counter(a), Counter(b)
        res = n-max(self.mp1.values()) + m-max(self.mp2.values())
        for i in range(ord('a'), ord('z')):
            tar = chr(i)
            res = min(res, self.checkMinOp(tar, a, b))
        return res
    
    def checkMinOp(self, tar, a, b):
        n, m = len(a), len(b)
        res1, res2 = 0, 0
        for key, val in self.mp1.items():
            if key > tar:
                res1 += val
            else:
                res2 += val
        for key, val in self.mp2.items():
            if key <= tar:
                res1 += val
            else:
                res2 += val
        return min(res1, res2)