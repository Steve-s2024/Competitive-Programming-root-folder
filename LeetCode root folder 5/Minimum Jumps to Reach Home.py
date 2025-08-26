# BFS solution, not really able to prove the solution though: 24%

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        mx = max(max(forbidden), x)
        st = set(forbidden)
        vis = set()
        vis.add((0, 0))
        q = deque([(0, 0)])
        cnt = 0
        while q:
            for _ in range(len(q)):
                pos, flag = q.popleft()
                if pos == x: return cnt
                if pos-b not in st and pos-b >= 0 and (pos-b, 1) not in vis and not flag:
                    vis.add((pos-b, 1))
                    q.append((pos-b, 1))
                if pos+a not in st and pos+a <= mx*4 and (pos+a, 0) not in vis:
                    q.append((pos+a, 0))
                    vis.add((pos+a, 0))
            cnt += 1
        return -1