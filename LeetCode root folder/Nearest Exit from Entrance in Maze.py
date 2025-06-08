# quite obvious bfs solution, don't know why it took me so long to realize this:159
# ms
# Beats
# 11.91%
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        visited = set()
        step = 0
        entr = (entrance[0], entrance[1])
        q = deque([entr])
        visited.add(entr)
        while q:
            l = len(q)
            while l:
                (r, c) = q.popleft()
                if (r in [0, row-1] or c in [0, col-1]) and (r, c) != entr:
                    print(step, (r, c))
                    return step
                nextCoor = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for R, C in nextCoor:
                    if (
                        R in range(row) and
                        C in range(col) and
                        maze[R][C] != '+' and
                        (R, C) not in visited
                    ):
                        visited.add((R, C))
                        q.append((R, C))
                l -= 1
            step += 1
        return -1

# dp solution no.1: tle
'''class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        minStep = float('inf')
        row, col = len(maze), len(maze[0])
        dp = {}
        # dp[(r, c)] --> min step to exit from position (r, c)
        def dfs(r, c, step):
            nonlocal minStep
            if (
                r not in range(row) or
                c not in range(col) or
                maze[r][c] == '+'
            ):
                return float('inf')
            if (r, c) in dp and dp[(r, c)] <= step:
                return
            if (
                (
                    r in [0, row-1] or
                    c in [0, col-1]
                ) and
                (r, c) != (entrance[0], entrance[1])
            ):
                minStep = min(minStep, step)

            dp[(r, c)] = step
            dfs(r+1, c, step+1)
            dfs(r-1, c, step+1)
            dfs(r, c+1, step+1)
            dfs(r, c-1, step+1)
        dfs(entrance[0], entrance[1], 0)
        if minStep == float('inf'):
            return -1
        return minStep'''

# dp solution [discarded]
'''
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        dp = {}
        visited = set()
        # dp[(r, c)] --> min step to exit from position (r, c)
        def dfs(r, c):
            if (
                r not in range(row) or
                c not in range(col) or
                maze[r][c] == '+'
            ):
                return float('inf')
            if (
                (
                    r in [0, row-1] or
                    c in [0, col-1]
                ) and
                (r, c) != (entrance[0], entrance[1])
            ):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            if (r, c) in visited:
                return float('inf')
            visited.add((r, c))
            res = min(
                dfs(r + 1, c),
                dfs(r - 1, c),
                dfs(r, c + 1),
                dfs(r, c - 1)
            ) + 1
            dp[(r, c)] = res
            visited.remove((r, c))
            return res

        dfs(entrance[0], entrance[1])
        res = dp[(entrance[0], entrance[1])]
        if res == float('inf'):
            return -1
        return res
'''