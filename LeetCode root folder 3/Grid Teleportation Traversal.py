# wtf!!!!!!!! this is easy as fk!!!!!! i got into top 300!!!! for the first time
# in a live contest!!!!!!
class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        tmp = [list(row) for row in matrix]
        matrix = tmp
        row, col = len(matrix), len(matrix[0])

        mp = defaultdict(list)
        for r in range(row):
            for c in range(col):
                if matrix[r][c] not in '#.':
                    mp[matrix[r][c]].append((r, c))

        q = deque()
        if matrix[0][0] == '.':
            matrix[0][0] = '#'
            q.append((0, 0))
        else:
            for rr, cc in mp[matrix[0][0]]:
                matrix[rr][cc] = '#'
                q.append((rr, cc))
        res = 0
        while q:
            l = len(q)
            while l:
                r, c = q.popleft()
                if r == row - 1 and c == col - 1:
                    return res
                for R, C in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if (
                            R in range(row) and
                            C in range(col) and
                            matrix[R][C] != '#'
                    ):

                        if matrix[R][C] == '.':
                            matrix[R][C] = '#'
                            q.append((R, C))
                        else:
                            for rr, cc in mp[matrix[R][C]]:
                                matrix[rr][cc] = '#'
                                q.append((rr, cc))
                l -= 1
            res += 1
        return -1