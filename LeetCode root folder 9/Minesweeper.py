# a minesweeper with a single click

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        q = deque([click])
        n, m = len(board), len(board[0])

        def helper(r, c):
            return ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1), (r + 1, c + 1), (r - 1, c + 1), (r + 1, c - 1),
                    (r - 1, c - 1))

        while q:
            r, c = q.popleft()
            x = 0
            for R, C in helper(r, c):
                if R in range(n) and C in range(m):
                    x += 1 if board[R][C] == 'M' else 0

            if x:
                board[r][c] = str(x)
            else:
                board[r][c] = 'B'
                for R, C in helper(r, c):
                    if R in range(n) and C in range(m) and board[R][C] == 'E':
                        board[R][C] = 'B'
                        q.append((R, C))

        return board