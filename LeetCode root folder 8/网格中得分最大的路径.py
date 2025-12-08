# AC, the most stupid question ever. f_cking stupid leetcode sucks. have to f_ck me over with stupid question like this
# from time to time
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dp = {}
        def recursive(r, c, kcur):
            nonlocal k
            if kcur > k: return -inf
            if r == n-1 and c == m-1: return 0
            state = (r, c, kcur)
            if state in dp: return dp[state]
            res = -inf
            if r < n-1:
                a = recursive(r+1, c, (1 if grid[r+1][c] else 0)+kcur)+grid[r+1][c]
                res = max(res, a)
            if c < m-1:
                a = recursive(r, c+1, (1 if grid[r][c+1] else 0)+kcur)+grid[r][c+1]
                res = max(res, a)
            dp[state] = res
            return res
        res = recursive(0, 0, 0)
        return res if res != -inf else -1




#WA
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dp = {}
        def recursive(r, c, kcur, score):
            if kcur > k: return -inf
            if r == n-1 and c == m-1:
                return score
            state = (r, c, kcur)
            if state in dp and dp[state] >= score: return dp[state]
            dp[state] = score
            res = -inf
            if r < n-1:
                a = recursive(r+1, c, (1 if grid[r+1][c] else 0)+kcur, grid[r+1][c]+score)
                res = max(res, a)
            if c < m-1:
                a = recursive(r, c+1, (1 if grid[r][c+1] else 0)+kcur, grid[r][c+1]+score)
                res = max(res, a)
            return res
        res = recursive(0, 0, 0, 0)
        return res if res != -inf else -1



#WA
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        maxheap = [(0, 0, 0, 0)]
        vis = {}
        while maxheap:
            score, r, c, kcur = heappop(maxheap)
            score = -score
            state = (kcur, r, c)
            if state in vis and vis[state] >= score: continue
            vis[state] = score
            if kcur > k: continue
            if r == n-1 and c == m-1:
                return score
            if r < n-1:
                nk = kcur+(1 if grid[r+1][c] != 0 else 0)
                nscore = score + grid[r+1][c]
                heappush(maxheap, (-nscore, r+1, c, nk))
            if c < m-1:
                nk = kcur+(1 if grid[r][c+1] != 0 else 0)
                nscore = score + grid[r][c+1]
                heappush(maxheap, (-nscore, r, c+1, nk))
        return -1