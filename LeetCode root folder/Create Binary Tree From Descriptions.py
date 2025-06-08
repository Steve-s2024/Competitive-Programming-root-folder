# hash map solution:182
# ms
# Beats
# 66.27%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashSet = set()
        hashMap = {}
        for p, c, isL in descriptions:
            hashSet.add(c)
            if p not in hashMap:
                hashMap[p] = TreeNode(p)
            if c not in hashMap:
                hashMap[c] = TreeNode(c)
            if isL:
                hashMap[p].left = hashMap[c]
            else:
                hashMap[p].right = hashMap[c]
        for key, val in hashMap.items():
            if key not in hashSet:
                # print(key)
                return val
