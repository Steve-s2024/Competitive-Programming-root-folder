# bfs solution: 18%
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def toString(b):
            s = ''
            for r in range(2):
                for c in range(3):
                    s += str(b[r][c])
            return s
        def findZero(b):
            for r in range(2):
                for c in range(3):
                    if b[r][c] == 0:
                        return [r, c]
        def copyBoard(b):
            newB = [[-1]*3 for i in range(2)]
            for r in range(2):
                for c in range(3):
                    newB[r][c] = b[r][c]
            return newB
        visited = set()
        q = deque([board])
        res = 0
        while q:
            l = len(q)
            while l:
                cur = q.popleft()
                if toString(cur) == '123450':
                    return res
                [r, c] = findZero(cur)
                for R, C in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if R in range(2) and C in range(3):
                        newBoard = copyBoard(cur)
                        newBoard[r][c] = cur[R][C]
                        newBoard[R][C] = cur[r][c]
                        s = toString(newBoard)

                        if s not in visited:
                            visited.add(s)
                            q.append(newBoard)
                l-=1
            res+=1
        return -1

# don't know why this didn't work...
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        def swap(r1, c1, r2, c2):
            tmp = board[r1][c1]
            board[r1][c1] = board[r2][c2]
            board[r2][c2] = tmp

        dp = {}
        dp['123450'] = 0
        def recursive(r, c):
            s = ''
            for i in range(2):
                for j in range(3):
                    s += str(board[i][j])
            if s in dp:
                return dp[s]

            print(s, (r, c))
            res = float('inf')
            dp[s] = res
            for R, C in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if R in range(2) and C in range(3):
                    swap(r, c, R, C)
                    res = min(res, recursive(R, C))
                    swap(r, c, R, C)
            res += 1
            dp[s] = res
            return res
            
        for r in range(2):
            for c in range(3):
                if board[r][c] == 0:
                    res = recursive(r, c)
                    if res == float('inf'):
                        return -1
                    return res