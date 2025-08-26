# prefix sum solution: 5%
# didn't know how I come down to this solution, absolutely make no sense to me, but I just somehow figure it out
# this is 100% more difficult than the intended solution
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        mp = {}
        row, col = len(matrix), len(matrix[0])
        pre = []
        res = 0
        for i in range(row):
            pre.append([])
            for j in range(col):
                tot = matrix[i][j]
                if i > 0: tot += pre[i-1][j]
                if j > 0: tot += pre[i][j-1]
                if i > 0 and j > 0: tot -= pre[i-1][j-1]
                pre[i].append(tot)
                for k in range(j):
                    if (j, k) not in mp:
                        mp[(j, k)] = defaultdict(int)
                        mp[(j, k)][0] = 1
                    res += mp[(j, k)][target - (pre[i][j]-pre[i][k])]
                    mp[(j, k)][pre[i][k]-pre[i][j]] += 1
                for k in range(i):
                    if pre[i][j]-pre[k][j] == target: res += 1
                if pre[i][j] == target: res += 1

        return res