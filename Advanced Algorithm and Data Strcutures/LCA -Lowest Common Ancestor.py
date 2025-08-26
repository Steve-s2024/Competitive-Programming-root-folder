from Tree import Tree
from Binary_Lifting import BinaryLifting

class LCA:
    def __init__(self, tree, size):
        up = BinaryLifting.build(tree, size)
        self.up = up
        depth = [0]*size
        def dfs(node, dep):
            if node is None: return
            depth[node.val] = dep
            dfs(node.left, dep+1)
            dfs(node.right, dep+1)
        dfs(tree, 0)
        self.depth = depth

    def search(self, u, v):
        depth = self.depth
        up = self.up
        if depth[u] > depth[v]: u, v = v, u

        dif = depth[v]-depth[u]
        i = 0
        while dif:
            if dif&1: v = up[v][i]
            dif >>= 1
            i += 1

        # incase if LCA is one of them
        if u == v: return v
        i = len(up[0])-1
        while i >= 0:
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
            i -= 1
        return up[u][0]




treeArr = [0,1,2,3,4,5,6,7,8,9,10]
size = len(treeArr)
tree = Tree().build(treeArr)
lca = LCA(tree, size)
print('LCA tests:')
print(lca.search(1, 4))
print(lca.search(2, 4))
print(lca.search(9, 5))
print(lca.search(6, 5))
print(lca.search(8, 10))
