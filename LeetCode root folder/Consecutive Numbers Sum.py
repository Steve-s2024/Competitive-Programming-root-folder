# hard? really? glad to solve a hard tagged question after quite a while
# it almost feels like codeforces style question: 57.21%
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        m = 0
        total = 0
        res = 0
        while total <= n:
            remain = n-total
            if remain % (m+1) == 0 and total != n:
                # print(m+1)
                res+=1
            m+=1
            total = m*(m+1)//2
        return res



# depricated
class Solution:
    def __init__(self):
        self.ref = set()
        total = 0
        n = 0
        while total <= 1_000_000_000:
            self.ref.add(total)
            n += 1
            total += n
        
        
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 0
        for total in self.ref:
            remain = total - n
            if remain in self.ref:
                res += 1
        return res