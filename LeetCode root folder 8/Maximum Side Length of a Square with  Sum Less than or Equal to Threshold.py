# very hard binary search and 2D prefix sum problem: 38%
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(1, m):
                mat[i][j] += mat[i][j - 1]

        for j in range(m):
            for i in range(1, n):
                mat[i][j] += mat[i - 1][j]

        for r in mat: print(r)
        l, r = 1, min(n, m)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            for i in range(mid - 1, n):
                for j in range(mid - 1, m):
                    a = mat[i][j]
                    b = mat[i][j - mid] if j - mid >= 0 else 0
                    c = mat[i - mid][j] if i - mid >= 0 else 0
                    d = mat[i - mid][j - mid] if i - mid >= 0 and j - mid >= 0 else 0
                    if a - b - c + d <= threshold: break
                else:
                    continue
                break
            else:
                r = mid - 1
                continue
            res = mid
            l = mid + 1

        return res

