# ... didn't expect it to pass: 5%
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        row, col = len(mat), len(mat[0])

        @cache
        def recursive(r, tot):
            nonlocal row, col, target, res
            if tot >= target and res <= tot - target:
                return
            if r >= row:
                res = min(res, abs(tot - target))
                return
            for c in range(col):
                recursive(r + 1, tot + mat[r][c])

        res = float('inf')
        recursive(0, 0)
        return res
