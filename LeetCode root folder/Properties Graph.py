# brute force n^3 solution, it should not pass, the worst case could have 10^6!!:

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        hashMap = {}
        nodes = {}
        for idx, row in enumerate(properties):
            hashMap[idx] = set(row)
        # print(hashMap)

        for i in range(len(properties)):
            for j in range(i + 1, len(properties)):
                count = 0
                for val in hashMap[j]:
                    if val in hashMap[i]:
                        count += 1
                # print(i, j, count)
                if count >= k:
                    if i not in nodes:
                        nodes[i] = Node(i, [])
                    if j not in nodes:
                        nodes[j] = Node(j, [])
                    nodes[i].neighbors.append(j)
                    nodes[j].neighbors.append(i)

        # for key, val in nodes.items():
            # print(key, val.neighbors)
        ans = 0
        visited = set()

        def dfs(val):
            # print(val)
            visited.add(val)
            for nextVal in nodes[val].neighbors:
                if nextVal not in visited:
                    dfs(nextVal)

        for i in range(len(properties)):
            if i in visited:
                continue
            if i in nodes:
                dfs(i)
            ans += 1
            # print()
        return ans