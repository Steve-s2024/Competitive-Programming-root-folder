# unbelievable question, imagine it is above 2100 and a Q4, it is not supposed to be even a Q2!: 55%
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        res = [(arr[i], arr[j]) for i in range(n) for j in range(i+1, n)]
        res.sort(key=lambda i:i[0]/i[1])
        return res[k-1]