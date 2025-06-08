# amazing algorithm I have invented here (see recursive function)
# this algorithm incorporated the standard recursion and backtracking, but with linear time
# because it has used a combination of [idx, TreeNode] as return data to reduce the unnecessary
# repetition!

class TreeNode:
    def __init__(self, val='', children=None):
        self.val = val
        self.children = children


def solution():
    str = input()
    def recursive(i):
        r = i
        while 'A' <= str[r] <= 'Z':
            r += 1
        name = str[i:r]
        if str[r] == ':':
            curNode = TreeNode(name, [])
            [idx, child] = recursive(r+1)
            curNode.children.append(child)
            while str[idx] == ',':
                [idx, child] = recursive(idx+1)
                curNode.children.append(child)
            return [idx+1, curNode]
        else:
            return [r+1, TreeNode(name)]

    tree = recursive(0)[1]
    def countPair(val, node):
        total = 0
        if node.val == val:
            total += 1
        if node.children:
            for child in node.children:
                total += countPair(val, child)
        return total
    res = 0
    def dfs(node):
        nonlocal res
        pair = countPair(node.val, node)
        # print(node.val, pair)
        res += pair - 1
        if node.children:
            for child in node.children:
                dfs(child)
    dfs(tree)
    print(res)

solution()