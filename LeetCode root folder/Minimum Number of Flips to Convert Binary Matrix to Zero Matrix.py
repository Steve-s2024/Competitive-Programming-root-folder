# dp solution: 22%, no pressure
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        def swap(r, c):
            for R, C in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if R in range(row) and C in range(col):
                    mat[R][C] = (mat[R][C]+1)%2
            mat[r][c] = (mat[r][c]+1)%2

        visited = set()
        dp = {}
        dp['0'*(row*col)] = 0
        def recursive():
            s = ''
            for r in range(row):
                for c in range(col):
                    s+=str(mat[r][c])
            if s in dp:
                return dp[s]
            if s in visited:
                return float('inf')
            visited.add(s)

            res = float('inf')
            for r in range(row):
                for c in range(col):
                    swap(r, c)
                    res = min(res, recursive())
                    swap(r, c)        
            res+=1
            dp[s] = res
            return res
        ans = recursive()
        if ans == float('inf'):
            return -1
        return ans