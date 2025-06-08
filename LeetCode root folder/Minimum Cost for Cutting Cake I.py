# 2D dp solution, the states is quite hard to maintain, barely passed. but somehow my solution is the intended
# solution according to the LeetCode hint:3155
# ms
# Beats
# 5.40%
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        dp = {}

        def recursive(w, h, W, H):
            if (w, h, W, H) in dp:
                return dp[(w, h, W, H)]
            if W-w == 1 and H-h == 1:
                return 0
            minCost = float('inf')
            # print(w, h, W, H)
            for i in range(w+1, W):
                a = recursive(w, h, i, H)
                b = recursive(i, h, W, H)
                minCost = min(a + b + verticalCut[i-1], minCost)
            for i in range(h+1, H):
                a = recursive(w, h, W, i)
                b = recursive(w, i, W, H)
                minCost = min(a + b + horizontalCut[i-1], minCost)
            # print(minCost, (w, h))
            dp[(w, h, W, H)] = minCost
            return minCost
        return recursive(0, 0, n, m)



# deprecated solution, misunderstood the question
'''class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        dp = {}

        def recursive(w, h):
            if (w, h) in dp:
                return dp[(w, h)]
            if w == 1 and h == 1:
                return 0
            minCost = float('inf')
            for i in range(1, w):
                a = recursive(w - i, h)
                b = recursive(i, h)
                minCost = min(a + b + verticalCut[i-1], minCost)
            for i in range(1, h):
                a = recursive(w, h - i)
                b = recursive(w, i)
                minCost = min(a + b + horizontalCut[i-1], minCost)
            # print(minCost, (w, h))
            dp[(w, h)] = minCost
            return minCost
        return recursive(n, m)'''

