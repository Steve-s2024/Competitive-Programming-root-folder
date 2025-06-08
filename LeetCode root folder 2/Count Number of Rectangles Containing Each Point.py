# union find solution, only 100 difference in rating, but
# this is clearly much easier than the 2000 rated math questions: 59%
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        graph = defaultdict(list)
        for a, b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        idMp = defaultdict(list)

        def dfs(node):
            nonlocal curId
            idMp[curId].append(node)
            for nextNode in graph[node]:
                if nextNode not in visited:
                    visited.add(nextNode)
                    dfs(nextNode)

        curId = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                curId += 1
        # print(idMp)

        hummingDst = n
        for curId in idMp:
            cnt = 0
            hashMap = defaultdict(int)
            for idx in idMp[curId]:
                hashMap[source[idx]] += 1
            for idx in idMp[curId]:
                if hashMap[target[idx]]:
                    cnt += 1
                    hashMap[target[idx]] -= 1
            hummingDst -= cnt

        return hummingDst



# brute force: TLE
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        n = len(rectangles)
        m = len(points)
        ans = [0] * m
        for i in range(n):
            [x, y] = rectangles[i]
            for j in range(m):
                [x1, y1] = points[j]
                if x1 <= x and y1 <= y:
                    ans[j] += 1
        return ans