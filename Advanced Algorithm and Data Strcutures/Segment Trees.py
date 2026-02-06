# 2026/01/04 a better, more efficient version of seg-tree. implemented by array in replacement of actual tree
# same complexity for init, update, and query. simpler update/query interface (parameter simplified)
# functional, verified via LeetCode submission
# (motivation for upgrade: need a more concise code for later lazy seg-tree implementation)
class SumTree:
    def __init__(self, ar):
        n = len(ar)
        tre = [0]*((1<<n.bit_length())-1 + n)
        self.tre, self.n = tre, n
        for i in range(n): self.update(i, ar[i])

    def update(self, i, v):
        tre, n = self.tre, self.n
        l, r = 0, (1<<n.bit_length())-1
        j, ar = 0, []
        while l < r:
            ar.append(j)
            m = (l+r)//2
            if i <= m: j, r = 2*j+1, m
            else: j, l = 2*j+2, m+1
        dif = v-tre[j]
        tre[j] = v
        for j in ar: tre[j] += dif

    def query(self, L, R):
        tre, n = self.tre, self.n
        res = 0
        def recursive(j, l, r):
            nonlocal L, R, res
            if r < L or l > R or l > r: return
            if L <= l and r <= R:
                res += tre[j]
                return
            m = (l+r)//2
            recursive(2*j+1, l, m)
            recursive(2*j+2, m+1, r)
        recursive(0, 0, (1<<n.bit_length())-1)
        return res

nums = [1, 2, 3, 4, 5]
st = SumTree(nums)
print(st.tre)
print(st.query(0, 3))
print(st.query(2, 4))
for i in range(0, 3): st.update(i, nums[i]+2)
print(st.query(0, 3))
print(st.query(2, 4))
print(st.query(1, 4))
for i in range(3, 5): st.update(i, nums[i]-2)
print(st.query(0, 3))
print(st.query(2, 4))
print(st.query(1, 4))

'''
st = SumTree([1, 2, 3, 4, 5])
print(st.query(0, 3))
print(st.query(2, 4))
print(st.query(1, 4))
st.update(0, 3)
st.update(4, 3)
print(st.query(0, 3))
print(st.query(2, 4))
print(st.query(1, 4))
'''



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


# an array sum segment tree implementation
'''
# 1. build
def build(l, r, inputArr):
    if l >= r:
        val = [0] * 6
        val[inputArr[l]] = 1
        return TreeNode(val)
    m = (l + r) // 2
    a = build(l, m, inputArr)
    b = build(m + 1, r, inputArr)
    val = [0] * 6
    for i in range(6):
        val[i] += a.val[i]
        val[i] += b.val[i]

    return TreeNode(
        val,
        a,
        b
    )


# 2. update
def update(node, i, val, oldVal, l, r):
    if l == r == i:
        node.val[oldVal] -= 1
        node.val[val] += 1
        return
    m = (l + r) // 2
    if i in range(l, m + 1):
        update(node.left, i, val, oldVal, l, m)
    else:
        update(node.right, i, val, oldVal, m + 1, r)
    node.val[oldVal] -= 1
    node.val[val] += 1


# 3. query
def query(node, L, R, l, r):
    if r < L or l > R:
        return [0] * 6
    if l >= L and r <= R:
        return node.val

    m = (l + r) // 2
    a = query(node.left, L, R, l, m)
    b = query(node.right, L, R, m + 1, r)
    val = [0] * 6
    for i in range(6):
        val[i] += a[i]
        val[i] += b[i]
    return val
'''


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