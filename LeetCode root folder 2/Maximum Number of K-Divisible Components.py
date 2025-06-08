# smoothest hard problem tackled. dfs and summing 
# tree value: 33%
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        visited = set()
        res = 0
        def dfs(node):
            nonlocal res
            total = values[node]
            visited.add(node)
            for child in tree[node]:
                if child not in visited:
                    total += dfs(child)

            if total % k == 0:
                res += 1
            # print(node, total)
            return total
        dfs(0)
        return res