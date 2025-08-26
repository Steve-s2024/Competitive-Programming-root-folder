# solved last year, solve it again this year with better performance and cleaner code: 80%
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rowMp, colMp = defaultdict(list), defaultdict(list)
        for r, c in stones:
            rowMp[r].append(c)
            colMp[c].append(r)

        rowSt, colSt = set(), set()
        vis = set()
        cluster = 0
        for r, c in stones:
            if (r, c) not in vis:
                vis.add((r, c))
                q = deque([(r, c)])
                while q:
                    R, C = q.popleft()
                    if R not in rowSt:
                        rowSt.add(R)
                        for nxt in rowMp[R]:
                            if (R, nxt) not in vis:
                                vis.add((R, nxt))
                                q.append((R, nxt))
                    if C not in colSt:
                        colSt.add(C)
                        for nxt in colMp[C]:
                            if (nxt, C) not in vis:
                                vis.add((nxt, C))
                                q.append((nxt, C))
                cluster += 1
        return n - cluster


# submission a year ago: 46%
class Solution():
    def removeStones(self, stones):
        r = dict()
        c = dict()
        for s in stones:
            if s[0] not in r:
                r[s[0]] = list()
            if s[1] not in c:
                c[s[1]] = list()
            r[s[0]].append(s[1])
            c[s[1]].append(s[0])
        ans = [0]

        # print(r, c)

        def dfs(xy, num):
            # print(stones, xy)
            temp = stones.index(xy)
            if temp < num:
                num -= 1
            stones.remove(xy)
            while len(r[xy[0]]):
                ans[0] += 1
                a = r[xy[0]].pop(0)
                c[a].remove(xy[0])
                dfs([xy[0], a], num)

            while len(c[xy[1]]):
                ans[0] += 1
                a = c[xy[1]].pop(0)
                r[a].remove(xy[1])
                dfs([a, xy[1]], num)
            return num

        i = 0
        while i < len(stones):
            s = stones[i]
            if len(r[s[0]]) + len(c[s[1]]) == 3 or i == len(stones) - 1:
                r[s[0]].remove(s[1])
                c[s[1]].remove(s[0])
                # print(s)
                i = dfs(s, i)
            i += 1

        while len(stones):
            s = stones[0]
            r[s[0]].remove(s[1])
            c[s[1]].remove(s[0])
            dfs(s, 0)

        return ans[0]