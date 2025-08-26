from collections import deque

class TreeNode:
    def __init__(self, val=0, children=[]):
        self.val = val
        self.children = children

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def build(self, arr):
        idx = 0
        tree = Node(arr[idx])
        idx += 1
        q = deque([tree])
        n = len(arr)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if idx >= n: break
                if arr[idx]:
                    node.left = Node(arr[idx])
                    q.append(node.left)
                idx += 1
                if idx >= n: break
                if arr[idx]:
                    node.right = Node(arr[idx])
                    q.append(node.right)
                idx += 1
        return tree
