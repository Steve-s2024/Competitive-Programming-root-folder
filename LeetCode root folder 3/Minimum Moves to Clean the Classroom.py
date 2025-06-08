# crazy, I never feel so exhausted
sys.setrecursionlimit(10000)
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        row, col = len(classroom), len(classroom[0])
        literCnt = 0
        liter = defaultdict(list)
        reset = defaultdict(list)

        for stR in range(row):
            for stC in range(col):
                if classroom[stR][stC] == 'L':
                    literCnt += 1
                    vis = set()
                    vis.add((stR, stC))
                    q = deque([(stR, stC)])
                    cnt = 0
                    while q:
                        l = len(q)
                        while l:
                            r, c = q.popleft()
                            liter[(r, c)].append((cnt, stR, stC))
                            for R, C in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                                if (
                                        R in range(row) and
                                        C in range(col) and
                                        (R, C) not in vis and
                                        classroom[R][C] != 'X'
                                ):
                                    vis.add((R, C))
                                    q.append((R, C))
                            l -= 1
                        cnt += 1

        for stR in range(row):
            for stC in range(col):
                if classroom[stR][stC] == 'R':
                    vis = set()
                    vis.add((stR, stC))
                    q = deque([(stR, stC)])
                    cnt = 0
                    while q:
                        l = len(q)
                        while l:
                            r, c = q.popleft()
                            reset[(r, c)].append((cnt, stR, stC))
                            for R, C in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                                if (
                                        R in range(row) and
                                        C in range(col) and
                                        (R, C) not in vis and
                                        classroom[R][C] != 'X'
                                ):
                                    vis.add((R, C))
                                    q.append((R, C))
                            l -= 1
                        cnt += 1

        # print(liter)
        # print(reset)
        vis = set()

        def recursive(r, c, eng):
            nonlocal energy, literCnt
            if len(vis) == literCnt:
                return 0
            if eng == 0:
                return float('inf')
            res = float('inf')

            for cost, R, C in liter[(r, c)]:
                if (R, C) in vis:
                    continue
                if cost <= eng:
                    vis.add((R, C))
                    a = recursive(R, C, eng - cost) + cost
                    res = min(res, a)
                    vis.remove((R, C))

            for cost, R, C in reset[(r, c)]:
                if cost <= eng:
                    a = recursive(R, C, energy) + cost
                    res = min(res, a)
            return res


        for r in range(row):
            for c in range(col):
                if classroom[r][c] == 'S':
                    a = recursive(r, c, energy)
                    return a if a != float('inf') else -1
