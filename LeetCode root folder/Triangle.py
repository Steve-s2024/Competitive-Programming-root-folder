# brute-force 0(2^len(triangle)):
'''class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        minSum = float('inf')
        def backtracking(idx, sum_, prevPosition):
            nonlocal minSum
            if idx >= len(triangle):
                minSum = min(sum_, minSum)
                return
            backtracking(idx+1, sum_ + triangle[idx][prevPosition], prevPosition)
            if prevPosition + 1 < len(triangle[idx]):
                backtracking(idx+1, sum_ + triangle[idx][prevPosition+1], prevPosition+1)
        backtracking(0, 0, 0)'''

# dp solution, the question is legit:7
# ms
# Beats
# 36.65%
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[len(triangle) - 1]]
        for i in range(len(triangle) - 2, -1, -1):
            dp.append([])
            for j in range(len(triangle[i])):
                # dp[-2][j] and dp[-2][j+1]
                dp[-1].append(triangle[i][j] + min(dp[-2][j], dp[-2][j + 1]))
        # print(dp)
        return min(dp[-1])
