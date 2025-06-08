# worth notice the way which I do spiral matrix traversal: 15%
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1]*n for _ in range(m)]
        rr, cc = 0, 1
        mp = {
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
            (0, 1): (1, 0)
        }
        grid[0][0] = head.val
        cur = head.next
        r, c = 0, 0
        while cur:
            if (
                r + rr not in range(m) or
                c + cc not in range(n) or
                grid[r+rr][c+cc] != -1
            ):
                rr, cc = mp[(rr, cc)]
            r += rr
            c += cc
            grid[r][c] = cur.val
            cur = cur.next
        return grid