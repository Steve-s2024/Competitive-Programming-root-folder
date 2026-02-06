# very simple squeezing/topo-sort style solution


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        mp = defaultdict(list)
        for i in range(n):
            for j in range(m):
                mp[mat[i][j]].append((i, j))
        ar = sorted(mp.keys())

        row = defaultdict(int)
        col = defaultdict(int)
        for k in ar:
            trow = defaultdict(int)
            tcol = defaultdict(int)
            for r, c in mp[k]:
                trow[r] = max(row[r]+1, col[c]+1, trow[r])
                tcol[c] = max(row[r]+1, col[c]+1, tcol[c])
            for k, v in trow.items(): row[k] = v
            for k, v in tcol.items(): col[k] = v

        # print(row, col)
        return max(max(row.values()), max(col.values()))

