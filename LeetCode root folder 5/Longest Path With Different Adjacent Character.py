# intuitive DFS solution, cause of the tree, if its graph than that will be a different story: 34%

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for i, x in enumerate(parent): tree[x].append(i)

        mxLen = 1

        def dfs(node):
            nonlocal mxLen
            leb = s[node]
            arr = []
            for nxt in tree[node]:
                l, c = dfs(nxt)
                if c != leb: arr.append((l, c))
            if len(arr) == 0: return 1, leb
            arr.sort(key=lambda i: i[0], reverse=True)
            if len(arr) == 1:
                mxLen = max(mxLen, arr[0][0] + 1)
                return arr[0][0] + 1, leb
            if len(arr) > 1:
                a, b = arr[0][0], arr[1][0]
                mxLen = max(mxLen, a + 1 + b)
                return a + 1, leb

        dfs(0)
        return mxLen
