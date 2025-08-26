# kindda boring and unproductive question, very easy to implement the brute-force, happens to be the intended solution
# only that you need to calibre the lim variable, the number of cells to visited before terminate the BFS: 49%
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        n = len(blocked)
        lim = n * n // 2
        blocks = set((r, c) for r, c in blocked)

        def bfs(src):
            vis = set()
            vis.add(tuple(src))
            q = deque([src])
            cnt = 0
            while q:
                if cnt >= lim: break
                r, c = q.popleft()
                cnt += 1
                for R, C in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if R in range(10 ** 6) and C in range(10 ** 6) and (R, C) not in blocks and (R, C) not in vis:
                        vis.add((R, C))
                        q.append((R, C))

            return cnt >= lim

        if bfs(source) and bfs(target): return True

        vis = set()
        vis.add(tuple(source))
        q = deque([source])
        cnt = 0
        while q:
            if cnt >= lim: break
            r, c = q.popleft()
            if r == target[0] and c == target[1]: return True
            cnt += 1
            for R, C in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if R in range(10 ** 6) and C in range(10 ** 6) and (R, C) not in blocks and (R, C) not in vis:
                    vis.add((R, C))
                    q.append((R, C))

        return False