

# deprecated champagne tower speed pyramid
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[1]]
        for i in range(1, 10):
            n = i+1
            tower.append([0] * n)
            tower[i][0] = tower[i-1][0]/2
            for j in range(1, n-1):
                a, b = tower[i-1][j-1], tower[i-1][j]
                tower[i][j] = (a + b)/2
            tower[i][-1] = tower[i-1][-1]/2
        print(tower)