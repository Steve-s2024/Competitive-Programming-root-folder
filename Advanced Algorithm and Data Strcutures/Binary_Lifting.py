from collections import deque
from Tree import Tree

# the binary lifting implementation: note that it only work on tree with distinct node value between 0 to size-1
# to accommodate other tree type, write code accordingly
class BinaryLifting():
    @staticmethod
    def build(tree, size):
        lim = 16
        up = [[-1]*lim for _ in range(size)]
        stk = []
        def dfs(node):
            if node is None: return
            i = 0
            while i < lim and 1<<i <= len(stk):
                up[node.val][i] = stk[-(1<<i)]
                i += 1
            stk.append(node.val)
            dfs(node.left)
            dfs(node.right)
            stk.pop()
        dfs(tree)
        return up

    @staticmethod
    def search(src, m, up):
        cur = src
        i = 0
        while m:
            if m&(1<<i):
                cur = up[cur][i]
                m -= 1<<i
                if cur == -1: return -1
            i += 1

        return cur

treeArr = [0,1,2,3,4,5,6,7,8,9,10]
size = len(treeArr)
tree = Tree().build(treeArr)
up = BinaryLifting.build(tree, size)
print(BinaryLifting.search(1, 2, up))
print(BinaryLifting.search(1, 5, up))
print(BinaryLifting.search(10, 3, up))
print(BinaryLifting.search(10, 2, up))
print(BinaryLifting.search(6, 1, up))
print(BinaryLifting.search(8, 2, up))


