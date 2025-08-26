# some luck helped me to this discovery, I couldn't prove it at the time, but then the hypothesis turns out to be
# correct: 84%
class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        vis = {}

        for idx, row in enumerate(grid):
            cur = int(''.join([str(e) for e in row]), 2)
            if cur == 0: return [idx]
            for num in vis:
                if num & cur == 0:
                    return [vis[num], idx]
            vis[cur] = idx
        return []