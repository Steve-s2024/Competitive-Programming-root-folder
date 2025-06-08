# recursive solution:91
# ms
# Beats
# 35.35%
# I love this problem, because the solution is so neet. Also, doing recursive is so amazing, it made me feel smart~
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def recursive(inorder, postorder):
            if not inorder:
                return None
            index = inorder.index(postorder[-1])
            # index--> number of left-hand side node current tree
            # len(postorder)-1 - index --> number of right-hand side node of current tree
            newNode = TreeNode(postorder[-1])
            newNode.left = recursive(inorder[:index], postorder[:index])
            newNode.right = recursive(inorder[index + 1:], postorder[index:-1])
            return newNode

        return recursive(inorder, postorder)
