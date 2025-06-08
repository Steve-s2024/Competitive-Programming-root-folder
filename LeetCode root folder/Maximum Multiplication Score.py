# this is the best time complexity, O(4*n), the problem is consider solved for me: TLE
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = {}
        def recursive(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= len(a)-1:
                return 0
            if j >= len(b)-1:
                return -float('inf')

            res = -float('inf')
            for nextJ in range(j+1, len(b)):
                res = max(recursive(i+1, nextJ) + a[i+1]*b[nextJ], res)
            dp[(i, j)] = res
            return res

        ans = -float('inf')
        for j in range(len(b)):        
            ans = max(recursive(0, j) +  a[0]*b[j], ans)
        return ans