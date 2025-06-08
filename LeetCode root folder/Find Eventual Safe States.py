# turns out I fk up the caching part with visited2, so theres a lot
# of repetitive work in the solutions, but now its fixed: 7%
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        cands = set()
        for i in range(n):
            cands.add(i)

        visited = set()
        visited2 = set()
        cycleNodes = set()
        
        def dfs(node):
            if node in visited2:
                return
            visited2.add(node)

            for nextNode in graph[node]:
                if nextNode in cycleNodes or nextNode in visited:
                    for nde in visited:
                        cycleNodes.add(nde)
                        if nde in cands:
                            cands.remove(nde)
                    continue
                
                visited.add(nextNode)
                dfs(nextNode)
                visited.remove(nextNode)
        for i in range(n):
            if i not in visited2:
                visited.add(i)
                dfs(i)
                visited.remove(i)

        
        return list(cands)
    

# unbelievable, This is the best it can be... : TLE
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        cands = set()
        for i in range(n):
            cands.add(i)
        visited = set()
        cycleNodes = set()
        visited2 = set()
        def dfs(node):
            visited2.add(node)
            for nextNode in graph[node]:
                if nextNode in visited or nextNode in cycleNodes:
                    # cycle detected
                    print(visited)
                    for num in visited:
                        if num in cands:
                            cands.remove(num)
                        cycleNodes.add(num)
                    continue
                        
                visited.add(nextNode)
                dfs(nextNode)
                visited.remove(nextNode)
        for i in range(n):
            if i not in visited2:
                visited.add(i)
                dfs(i)
                visited.remove(i)

        return list(cands)


# further optimized based on solution no.2: TLE
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        cands = set()
        for i in range(n):
            cands.add(i)
        visited = set()
        stack = []
        cycleNodes = set()
        visited2 = set()
        def dfs(node):
            visited2.add(node)
            for nextNode in graph[node]:
                if nextNode in visited or nextNode in cycleNodes:
                    # cycle detected
                    for num in stack:
                        cycleNodes.add(num)
                    continue
                        
                stack.append(nextNode)
                visited.add(nextNode)
                dfs(nextNode)
                visited.remove(nextNode)
                stack.pop()
        for i in range(n):
            if i not in visited2:
                stack.append(i)
                visited.add(i)
                dfs(i)
                visited.remove(i)
                stack.pop()

        ans = []
        for cand in cands:
            if cand not in cycleNodes:
                ans.append(cand)
        return ans

# optimized cycle detection solution: TLE
# this is at least hundrad of times faster then
# the solution no.1...
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        cands = set()
        for i in range(n):
            cands.add(i)
        visited = set()
        stack = []
        cycleNodes = set()
        def dfs(node):
            for nextNode in graph[node]:
                if nextNode in visited or nextNode in cycleNodes:
                    # cycle detected
                    for num in stack:
                        cycleNodes.add(num)
                    continue
                        
                stack.append(nextNode)
                visited.add(nextNode)
                dfs(nextNode)
                visited.remove(nextNode)
                stack.pop()
        for i in range(n):
            stack.append(i)
            visited.add(i)
            dfs(i)
            visited.remove(i)
            stack.pop()

        ans = []
        for cand in cands:
            if cand not in cycleNodes:
                ans.append(cand)
        return ans
    

# brute-force and cycle detection solution: TLE
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        cands = set()
        for i in range(n):
            cands.add(i)
        visited = set()
        stack = []
        def dfs(node):
            for nextNode in graph[node]:
                if nextNode in visited:
                    # cycle detected
                    for num in stack:
                        if num in cands:
                            cands.remove(num)
                    continue
                        
                stack.append(nextNode)
                visited.add(nextNode)
                dfs(nextNode)
                visited.remove(nextNode)
                stack.pop()
        for i in range(n):
            stack.append(i)
            visited.add(i)
            dfs(i)
            visited.remove(i)
            stack.pop()

        return list(cands)