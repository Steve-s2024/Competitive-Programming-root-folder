# I am really gambling with the submission here
# humbly accept the success.😊: 13%
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        matrix = [[0]*k for i in range(k)]
        visited = set()
        rowMp, colMp = {}, {}
        
        def dfs(node, mp):
            if node in mp:
                return mp[node]+1
            res = 0
            for nextNode in graph[node]:
                if nextNode in visited:
                    return -1
                visited.add(nextNode)
                a = dfs(nextNode, mp)
                visited.remove(nextNode)
                if a == -1:
                    return -1
                res += a
            mp[node] = res
            return res+1


        graph = defaultdict(list)
        for above, below in rowConditions:
            graph[above].append(below)
        for i in range(1, k+1):
            visited.add(i)
            if dfs(i, rowMp) == -1:
                return []
            visited.remove(i)

        graph.clear()
        for left, right in colConditions:
            graph[left].append(right)
        for i in range(1, k+1):
            visited.add(i)
            if dfs(i, colMp) == -1:
                return []
            visited.remove(i)

        # print(rowMp, colMp)
        arr1, arr2 = [(key, val) for key, val in rowMp.items()], [(key, val) for key, val in colMp.items()]
        arr1.sort(reverse = True, key = lambda i : i[1])
        arr2.sort(reverse = True, key = lambda i : i[1])
        n, m = len(arr1), len(arr2)
        
        coors = [[0, 0] for i in range(k)]
        for i in range(n):
            [key, val] = arr1[i]
            coors[key-1][0] = i

        for i in range(m):
            [key, val] = arr2[i]
            coors[key-1][1] = i
        
        for i in range(k):
            [r, c] = coors[i]
            matrix[r][c] = i+1

        return matrix
