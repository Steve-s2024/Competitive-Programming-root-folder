# dfs & hashing solution, this is rated 1808 on zerotrac, not bad👍✌: 89%
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        visited = set()
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        hashMap = defaultdict(int)
        ans = [0] * n

        def dfs(node):
            tmp = hashMap[labels[node]]
            visited.add(node)
            hashMap[labels[node]] += 1
            for nextNode in graph[node]:
                if nextNode not in visited:
                    dfs(nextNode)
            ans[node] = hashMap[labels[node]] - tmp

        dfs(0)
        return ans



# brute-force: TLE
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        visited = set()
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        valMap = defaultdict(int)
        def dfs(node, ancesters):
            for anc in ancesters:
                if labels[anc] == labels[node]:
                    valMap[anc] += 1

            visited.add(node)
            for nextNode in graph[node]:
                if nextNode not in visited:
                    ancesters.append(node)
                    dfs(nextNode, ancesters)
                    ancesters.pop()        
        dfs(0, [])
        # print(valMap)
        ans = [1] * n
        for key, val in valMap.items():
            ans[key] = val+1
        return ans
        
# brute-force: MLE
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        visited = set()
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        valMap = defaultdict(int)
        def dfs(node, ancesters):
            for anc in ancesters:
                if labels[anc] == labels[node]:
                    valMap[anc] += 1

            visited.add(node)
            for nextNode in graph[node]:
                if nextNode not in visited:
                    dfs(nextNode, ancesters + [node])
        
        dfs(0, [])
        # print(valMap)
        ans = [1] * n
        for key, val in valMap.items():
            ans[key] = val+1
        return ans
        