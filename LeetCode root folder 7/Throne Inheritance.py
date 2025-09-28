# most tedious description ever!: 20%
class ThroneInheritance:

    def __init__(self, kingName: str):
        tree = defaultdict(list)
        tree[kingName] = []
        dead = set()

        self.tree = tree
        self.dead = dead
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.tree[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []

        def dfs(node):
            if node not in self.dead: order.append(node)
            for nxt in self.tree[node]: dfs(nxt)

        dfs(self.kingName)
        return order
