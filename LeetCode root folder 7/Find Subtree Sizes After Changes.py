# 49%
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        tree = defaultdict(list)
        for i in range(n):
            tree[parent[i]].append(i)

        np = parent[:]
        stk = defaultdict(list)

        def dfs(node):
            if stk[s[node]]: np[node] = stk[s[node]][-1]
            stk[s[node]].append(node)
            for chd in tree[node]: dfs(chd)
            stk[s[node]].pop()

        dfs(0)

        tree.clear()
        for i in range(n):
            tree[np[i]].append(i)

        ans = [1] * n

        def dfs2(node):
            for chd in tree[node]: ans[node] += dfs2(chd)
            return ans[node]

        dfs2(0)
        return ans