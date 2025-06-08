# improved upon solution no.1, using bfs: 79%
class CBTInserter:
    
    def __init__(self, root: Optional[TreeNode]):
        self.tree = root
        self.q = deque([root])
        self.nextQ = deque()
        while True:
            self.nextQ = deque()
            flag = False
            for node in self.q:
                if node.left:
                    self.nextQ.append(node.left)
                else:
                    flag = True
                if node.right:
                    self.nextQ.append(node.right)
                else:
                    flag = True
            if flag:
                break
            self.q = self.nextQ  
        # now, q --> first layer to have None children/child. so we add new nodes to this layer        
        tmp = self.q
        self.q = deque()
        for node in tmp:
            if node.right == None:
                self.q.append(node)
        # print(self.nextQ)
        # print(self.q)

    def insert(self, val: int) -> int:
        cur = self.q[0]
        if cur.left == None:
            cur.left = TreeNode(val)
            self.nextQ.append(cur.left)
        else:
            cur.right = TreeNode(val)
            self.nextQ.append(cur.right)
            self.q.popleft()
        
        if not self.q:
            self.q = self.nextQ
            self.nextQ = deque()

        return cur.val

    def get_root(self) -> Optional[TreeNode]:
        return self.tree





# solution no.1: 18%
class CBTInserter:
    
    def __init__(self, root: Optional[TreeNode]):
        self.tree = root
        def dfs(node):
            if node is None:
                return 0
            return (
                dfs(node.left) +
                dfs(node.right) +
                1
            )
        self.size = dfs(root)
        self.level = 1
        while (pow(2, self.level)-1) < self.size:
            self.level+=1

    def insert(self, val: int) -> int:
        self.size += 1
        if self.size > pow(2, self.level)-1:
            self.level+=1
        pos = self.size - (pow(2, self.level-1)-1)

        def dfs(node, l, r):
            nonlocal pos
            subSize = (r-l+1)//2
            a, b, c, d = l, l+subSize-1, r-subSize+1, r
            if pos in range(a, b+1):
                if a == b:
                    node.left = TreeNode(val)
                    return node.val
                return dfs(node.left, a, b)
            if pos in range(c, d+1):
                if c == d:
                    node.right = TreeNode(val)
                    return node.val
                return dfs(node.right, c, d)

        return dfs(self.tree, 1, pow(2, self.level-1))

    def get_root(self) -> Optional[TreeNode]:
            return self.tree


