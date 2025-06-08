# simulation brute force, takes four times more than O(rows*cols) solution
#: 8%
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [(rStart, cStart)]
        visited = set()
        visited.add((rStart, cStart))
        r, c = rStart, cStart
        rr, cc = -1, 0
        mp = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1)
        }
        while len(res) < rows * cols:
            newRR, newCC = mp[(rr, cc)]
            if (r + newRR, c + newCC) not in visited:
                rr, cc = newRR, newCC

            r += rr
            c += cc
            visited.add((r, c))
            if r in range(rows) and c in range(cols):
                res.append((r, c))

        return res