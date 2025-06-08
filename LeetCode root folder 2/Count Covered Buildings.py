# shouldn't make this Q1, not very easy
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        res = 0
        row, col = defaultdict(list), defaultdict(list)
        for r, c in buildings:
            row[r].append(c)
            col[c].append(r)
        for val in row.values():
            val.sort()
        for val in col.values():
            val.sort()
        for r, c in buildings:
            if (
                len(row[r]) > 2 and 
                row[r][0] != c and
                row[r][-1] != c and
                len(col[c]) > 2 and
                col[c][0] != r and
                col[c][-1] != r 
            ):
                res += 1
        return res