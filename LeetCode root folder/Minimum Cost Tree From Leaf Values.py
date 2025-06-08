# my masterpiece: 30%

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = {}
        def recursive(l, r):
            if (l, r) in dp:
                return dp[(l, r)]
            if l == r:
                return (arr[l], 0)
            
            minTotal = float('inf')
            mx = 0
            for i in range(l, r):
                [mx1, total1] = recursive(l, i)
                [mx2, total2] = recursive(i+1, r)
                treeTotal = total1 + total2 + mx1*mx2
                if treeTotal < minTotal:
                    minTotal = treeTotal
                    mx = max(mx1, mx2, mx)
            dp[(l, r)] = (mx, minTotal)
            return (mx, minTotal)
        
        n = len(arr)
        return recursive(0, n-1)[1]

            