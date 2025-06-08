# building my own segment tree build, query, update function for querying maximum value inside range

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(root):
    q = deque([root])
    while q:
        l = len(q)
        s = ''
        while l:
            cur = q.popleft()
            s += str(cur.val) + ' '
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            l -= 1
        print(s)


# 1. build
def build(l, r):
    if l >= r:
        return TreeNode(inputArr[l])
    m = (l + r) // 2
    a = build(l, m)
    b = build(m+1, r)
    return TreeNode(
        max(a.val, b.val),
        a,
        b
    )


# 2. update
def update(node, i, val, l, r):
    if l == r == i:
        node.val = val
        return val
    m = (l + r) // 2
    if i in range(l, m+1):
        res = update(node.left, i, val, l, m)
    else:
        res = update(node.right, i, val, m+1, r)
    node.val = max(node.val, res)
    return node.val


# 3. query
def query(node, L, R, l, r):

    if r < L or l > R:
        return -float('inf')
    if l >= L and r <= R:
        return node.val

    m = (l + r) // 2
    return max(
        query(node.left, L, R, l, m),
        query(node.right, L, R, m+1, r),
    )


# 4. test
inputArr = [1, 2, 3, 4, 5, 6, 7]
length = len(inputArr)
maxTree = build(0, length-1)
print('the tree:')
printTree(maxTree)
print()

print('the maximum queries:')
print(
    query(maxTree, 0, 7, 0, length-1),
    query(maxTree, 2, 3, 0, length - 1),
    query(maxTree, 3, 6, 0, length - 1),
    query(maxTree, 5, 5, 0, length - 1)
)
print()

update(maxTree, 2, 10, 0, length-1)
print('tree updated:')
printTree(maxTree)
print()

print('the maximum queries:')
print(
    query(maxTree, 0, 7, 0, length-1),
    query(maxTree, 2, 3, 0, length - 1),
    query(maxTree, 3, 6, 0, length - 1),
    query(maxTree, 5, 5, 0, length - 1)
)





# discarded codes
'''
# Segment Tree is not a LeetCode question, it is instead a useful data structure for range query. i have created
# three different type of segment tree below, they are designed for searching sum, max, min value of an array in a
# range [l, r] with in log(n) time complexity.


inputArr = [1, 3, 4, 5, 2, 3, 1, 2, 5, 4, 2]


# 1. Sum Tree
def buildSumTree(arr):
    nodes = []
    for num in arr:
        nodes.append(TreeNode(num))
    def build(nodes):
        if len(nodes) == 1:
            return nodes[0]
        tmp = []
        for i in range(0, len(nodes)-1, 2):
            a = nodes[i]
            b = nodes[i+1]
            tmp.append(TreeNode(a.val + b.val, a, b))
        if len(nodes) % 2 == 1:
            a = nodes[-1]
            tmp.append(TreeNode(a.val, a))
        return build(tmp)
    return build(nodes)

# sumTree = buildSumTree(inputArr)
# printTree(sumTree)


# 2. Max Tree
def buildMaxTree(arr):
    nodes = []
    for num in arr:
        nodes.append(TreeNode(num))
    def build(nodes):
        if len(nodes) == 1:
            return nodes[0]
        tmp = []
        for i in range(0, len(nodes)-1, 2):
            a = nodes[i]
            b = nodes[i+1]
            tmp.append(TreeNode(max(a.val, b.val), a, b))
        if len(nodes) % 2 == 1:
            a = nodes[-1]
            tmp.append(TreeNode(a.val, a))
        return build(tmp)
    return build(nodes)

# maxTree = buildMaxTree(inputArr)
# printTree(maxTree)

# 3. Min Tree
def buildMinTree(arr):
    nodes = []
    for num in arr:
        nodes.append(TreeNode(num))
    def build(nodes):
        if len(nodes) == 1:
            return nodes[0]
        tmp = []
        for i in range(0, len(nodes)-1, 2):
            a = nodes[i]
            b = nodes[i+1]
            tmp.append(TreeNode(min(a.val, b.val), a, b))
        if len(nodes) % 2 == 1:
            a = nodes[-1]
            tmp.append(TreeNode(a.val, a))
        return build(tmp)
    return build(nodes)

'''