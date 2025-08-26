# don't know why my DFS and DP solution failed, but this BFS did work: 24%
class Solution:
    @staticmethod
    def tostring(board):
        return ''.join(str(board[i][j]) for i in range(2) for j in range(3))

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        q = deque([board])
        vis = set()
        cnt = 0
        while q:
            for _ in range(len(q)):
                board = q.popleft()
                s = Solution.tostring(board)
                if s == '123450': return cnt
                vis.add(s)
                r, c = 0, 0
                for i in range(2):
                    for j in range(3):
                        if board[i][j] == 0:
                            r, c = i, j

                for R, C in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if R in range(2) and C in range(3):
                        copy = [row[:] for row in board]
                        copy[r][c], copy[R][C] = copy[R][C], copy[r][c]
                        if Solution.tostring(copy) in vis: continue
                        q.append(copy)
            cnt += 1
        return -1