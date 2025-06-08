# i guess using hash map and tupple to do 2D DP is much more 
# memory consuming than array DP... this passed like a charm
# and only difference is array replaced hash map: 41%
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0]*n for i in range(n)]

        def recursive(i, j, turn, total):
            if total == 0:
                # [0] for alice and [1] for bob
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            
            
            a, b = total-stones[i], total-stones[j]
            diff1 = recursive(i+1, j, not turn, a)
            diff2 = recursive(i, j-1, not turn, b)

            if turn:
                res = max(diff1+a, diff2+b)
                dp[i][j] = res
                return res
            else:
                res = min(diff1-a, diff2-b)
                dp[i][j] = res
                return res

        return recursive(0, n-1, True, sum(stones))
    

# I'm already spend all I have to come up with this
# exquisite dp recursion solution: MLE

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp = {}
        def recursive(i, j, turn, total):
            if (i, j) in dp:
                return dp[(i, j)]
            if total == 0:
                # [0] for alice and [1] for bob
                return 0
            
            a, b = total-stones[i], total-stones[j]
            diff1 = recursive(i+1, j, not turn, a)
            diff2 = recursive(i, j-1, not turn, b)

            if turn:
                res = max(diff1+a, diff2+b)
                dp[(i, j)] = res
                return res
            else:
                res = min(diff1-a, diff2-b)
                dp[(i, j)] = res
                return res

        n = len(stones)
        return recursive(0, n-1, True, sum(stones)) 