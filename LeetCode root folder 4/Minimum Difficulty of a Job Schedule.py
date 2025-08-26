# pretty straight forward DP solution, 300*300*10: 33%
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        arr = jobDifficulty
        n = len(arr)
        if n < d: return -1

        @cache
        def recursive(i, d):
            nonlocal n
            if i >= n: return 0 if d == 0 else float('inf')
            if d <= 0: return float('inf')

            res = float('inf')
            mx = arr[i]
            for j in range(i, n):
                mx = max(mx, arr[j])
                a = recursive(j + 1, d - 1) + mx
                res = min(res, a)
            return res

        return recursive(0, d)