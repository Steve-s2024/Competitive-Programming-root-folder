# this is the type of problem here the approach is so naively simple but somehow people just don't think it in
# that direction, I couldn't solve it without the hint: 91%


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        mp = defaultdict(list)
        heimp = {}
        lvlmp = {}
        def dfs(node, dep):
            if not node: return 0
            lvlmp[node.val] = dep
            height = max(
                dfs(node.left, dep+1),
                dfs(node.right, dep+1)
            )
            heimp[node.val] = height
            mp[dep].append(height)
            return height+1
        dfs(root, 0)

        for val in mp.values():
            val.sort()

        ans = []
        for q in queries:
            dep = lvlmp[q]
            if len(mp[dep]) == 1: ans.append(dep-1)
            else:
                if mp[dep][-1] == heimp[q]: ans.append(dep+mp[dep][-2])
                else: ans.append(dep+mp[dep][-1])
        return ans
