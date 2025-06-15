# its pretty easy...: 87%
class Solution:
    @staticmethod
    def helper(board):
        row, col = len(board), len(board[0])
        mp = {}
        cnt = 1
        for r in range(row - 1, -1, -1):
            if (row - r - 1) % 2 == 0:
                for c in range(col):
                    mp[cnt] = (r, c)
                    cnt += 1
            else:
                for c in range(col - 1, -1, -1):
                    mp[cnt] = (r, c)
                    cnt += 1
        return mp

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        mp = Solution.helper(board)
        # print(mp)

        vis = set()
        vis.add(1)
        q = deque([1])
        cnt = 0
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                r, c = mp[i]
                if board[r][c] != -1: i = board[r][c]

                if i == n**2:
                    return cnt
                for j in range(i+1, min(i+6, n**2)+1):
                    if j in vis:
                        continue
                    vis.add(j)
                    q.append(j)
            cnt += 1

        return -1