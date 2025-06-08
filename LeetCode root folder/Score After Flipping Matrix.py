# This is an idea that occurs to me right after i read the 
# problem description, but after spending a long time and failed to 
# prove it to be absolute correct (however it did worked at the end):
# 100%
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        for r in range(row):
            if grid[r][0] == 0:
                for c in range(col):
                    grid[r][c] = (grid[r][c] + 1) % 2
        
        res = row*pow(2, col-1)
        tmp = pow(2, col-2)
        for c in range(1, col):
            cnt1, cnt0 = 0, 0
            for r in range(row):
                if grid[r][c] == 1:
                    cnt1 += 1
                else:
                    cnt0 += 1
            # print(cnt1, cnt0)
            res += tmp*max(cnt1, cnt0)
            tmp /= 2
        return int(res) 