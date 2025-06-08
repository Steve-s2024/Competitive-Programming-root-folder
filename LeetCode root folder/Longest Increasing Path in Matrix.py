# brute-force
'''class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # brute-force
        visited = set()

        def findMaxPath(r, c, prev):
            if (
                    ((r, c) in visited) or
                    (r >= len(matrix) or r < 0) or
                    (c >= len(matrix[0]) or c < 0)
            ):
                return 0
            cur = matrix[r][c]
            if cur <= prev:
                return 0
            visited.add((r, c))
            res = max(
                findMaxPath(r + 1, c, cur),
                findMaxPath(r - 1, c, cur),
                findMaxPath(r, c + 1, cur),
                findMaxPath(r, c - 1, cur)
            ) + 1
            visited.remove((r, c))
            return res

        maxPath = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                maxPath = max(maxPath, findMaxPath(r, c, -float('inf')))
        return maxPath'''

# dp solution:242
# ms
# Beats
# 16.38%
# I realized that the dp don't need to be assigned value in the nested for loop, instead it can be populated inside the
# dfs, this works only because of the uniqueness of the question that the path is monotonic increasing! which really
# reduced the time complexity from O((m*n)^2) to O(m*n)
# because of the monotonic increasing feature, I also don't really need the visited hash set to warn me from stepping
# back to the path itself, I only need to check if matrix[r][c] <= prev.
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dp solution
        visited = set()
        dp = {}

        def findMaxPath(r, c, prev):
            if (
                    ((r, c) in visited) or
                    (r >= len(matrix) or r < 0) or
                    (c >= len(matrix[0]) or c < 0) or
                    (matrix[r][c] <= prev)
            ):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            cur = matrix[r][c]
            visited.add((r, c))
            res = max(
                findMaxPath(r + 1, c, cur),
                findMaxPath(r - 1, c, cur),
                findMaxPath(r, c + 1, cur),
                findMaxPath(r, c - 1, cur)
            ) + 1
            visited.remove((r, c))
            dp[(r, c)] = res
            return res

        maxPath = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                maxPath = max(maxPath, findMaxPath(r, c, -float('inf')))
        return maxPath


# dp solution without the visited hash set:186
# ms
# Beats
# 41.21%
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dp solution
        dp = {}

        def findMaxPath(r, c, prev):
            if (
                    (r >= len(matrix) or r < 0) or
                    (c >= len(matrix[0]) or c < 0) or
                    (matrix[r][c] <= prev)
            ):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            cur = matrix[r][c]
            res = max(
                findMaxPath(r + 1, c, cur),
                findMaxPath(r - 1, c, cur),
                findMaxPath(r, c + 1, cur),
                findMaxPath(r, c - 1, cur)
            ) + 1
            dp[(r, c)] = res
            return res

        maxPath = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                maxPath = max(maxPath, findMaxPath(r, c, -float('inf')))
        return maxPath
'''
