# dfs finding the longest path, but because the way the graph is
# structured, each node only at most have one outgoing edge, so
# to try out all possible path is a linear solution: 50%
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = set()
        longestCycle = -1
        hashMap = {}
        for i in range(n):
            if i not in visited:
                tmp = [i]
                hashMap[i] = 0
                path = 1
                nextNode = edges[i]
                while nextNode != -1:
                    if nextNode in visited:
                        break
                    if nextNode in hashMap:
                        cycleLen = path - hashMap[nextNode]
                        longestCycle = max(longestCycle, cycleLen)
                        break
                    hashMap[nextNode] = path
                    tmp.append(nextNode)
                    nextNode = edges[nextNode]
                    path += 1
                for node in tmp:
                    visited.add(node)
        return longestCycle




# brute force: TLE
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        longestPath = -1
        n = len(edges)
        for i in range(n):
            start = i
            nextNode = edges[start]
            path = 1
            visited = set()
            while nextNode != -1:
                # print(start, nextNode)
                if nextNode == start:
                    longestPath = max(longestPath, path)
                    break
                if nextNode in visited:
                    break
                visited.add(nextNode)
                nextNode = edges[nextNode]
                path += 1
        return longestPath
