# haha, they actually make the first version a Q4 in morning contest, and make a second version the Q3 of evening contest
# So, I have the luck to check for the hints posted in the biweekly discussion section. but the segment tree part is
# original and I actually spend 80% of the time just to adjust my seg tree form max tree to a frequency array sum tree.
class Solution:
    @staticmethod
    def getPopCountDep(num):
        res = 0
        while num != 1:
            num = num.bit_count()
            res += 1
        return res

    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        arr = []
        for num in nums:
            arr.append(Solution.getPopCountDep(num))
        tree = build(0, len(arr) - 1, arr)

        ans = []
        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]
                k = q[3]
                if k > 5:
                    ans.append(0)
                    continue

                res = query(tree, l, r, 0, len(arr) - 1)
                ans.append(res[k])
            else:
                idx = q[1]
                val = Solution.getPopCountDep(q[2])
                oldVal = arr[idx]
                arr[idx] = val
                update(tree, idx, val, oldVal, 0, len(arr) - 1)
        return ans


class TreeNode:
    def __init__(self, val=[0] * 6, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

