# single-handedly make Leetcode problem descriptions lower by a notch, plus that the quad tree definition is a bit complicated...


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def recursive(t, l, b, r):
            if t == b:
                x = Node(grid[t][l] == 1, True)
                return x

            mr = (t+b)//2
            mc = (l+r)//2
            x1 = recursive(t, l, mr, mc) # top left
            x2 = recursive(t, mc+1, mr, r) # top right
            x3 = recursive(mr+1, l, b, mc) # bottom left
            x4 = recursive(mr+1, mc+1, b, r) # bottom right

            if (
                x1.val == x2.val == x3.val == x4.val and
                x1.isLeaf == x2.isLeaf == x3.isLeaf == x4.isLeaf == True
            ): # current node should be a leaf node
                x = Node(grid[t][l] == 1, True)
            else: # current node is not a leaf node
                x = Node(0, False, x1, x2, x3, x4)
            return x
        return recursive(0, 0, n-1, n-1)

