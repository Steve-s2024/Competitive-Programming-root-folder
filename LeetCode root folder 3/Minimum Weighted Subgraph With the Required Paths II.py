


# TLE

class Solution:
    @staticmethod
    def getMinTree(tree, s1, s2, dst):
        inf = float('inf')
        visited = set()

        def dfs(node):
            nonlocal inf
            if node is None:
                return -inf

            res = -inf
            for nxt, weight in tree[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    a = dfs(nxt)
                    if a != -inf:
                        res = max(res, 0)
                        res += a + weight
            if res == -inf and node in [s1, s2]:
                return 0
            return res

        visited.add(dst)
        return dfs(dst)

    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        for a, b, w in edges:
            tree[a].append((b, w))
            tree[b].append((a, w))

        ans = []
        q = len(queries)
        for i in range(q):
            s1, s2, dst = queries[i]
            ans.append(Solution.getMinTree(tree, s1, s2, dst))

        return ans