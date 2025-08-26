# it beats the old submission by 4 times: 84%
# I think this is exactly what a topological sort is, by using the in-degree and do BFS first on nodes with zero in-degree
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowDeg = [0] * (k + 1)
        rowDeg[0] = inf
        rowGraph = defaultdict(list)
        for u, v in rowConditions:
            rowDeg[v] += 1
            rowGraph[u].append(v)

        colDeg = [0] * (k + 1)
        colDeg[0] = inf
        colGraph = defaultdict(list)
        for u, v in colConditions:
            colDeg[v] += 1
            colGraph[u].append(v)

        qRow = deque()
        qCol = deque()
        for i in range(1, k + 1):
            if rowDeg[i] == 0: qRow.append(i)
            if colDeg[i] == 0: qCol.append(i)

        mp = {i: [0, 0] for i in range(1, k + 1)}
        rowCnt = 0
        while qRow:
            node = qRow.popleft()
            mp[node][0] = rowCnt
            rowCnt += 1
            for nxt in rowGraph[node]:
                rowDeg[nxt] -= 1
                if rowDeg[nxt] == 0:
                    qRow.append(nxt)

        colCnt = 0
        while qCol:
            node = qCol.popleft()
            mp[node][1] = colCnt
            colCnt += 1
            for nxt in colGraph[node]:
                colDeg[nxt] -= 1
                if colDeg[nxt] == 0:
                    qCol.append(nxt)

        if colCnt != k or rowCnt != k: return []
        res = [[0] * k for _ in range(k)]
        for key, val in mp.items():
            r, c = val
            res[r][c] = key
        return res
