# pretty typical BFS question, only need to pay attention to
# leaf nodes, as frog will be trapped there forever: 72%
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(list)
        leafs = []
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        graph[1].append(0)
        q = deque([(1, 1)])
        vis = set()
        vis.add(0)  #pseudo node, as parent node of node1
        vis.add(1)
        cnt = 0
        while q:
            if cnt == t:
                break
            for _ in range(len(q)):
                node, prob = q.popleft()
                size = len(graph[node])-1
                if size == 0 and cnt <= t:
                    leafs.append((node, prob))
                for nxt in graph[node]:
                    if nxt not in vis:
                        vis.add(nxt)
                        q.append((nxt, prob*(1/size)))
            cnt += 1

        if cnt == t:
            for node, prob in q:
                if node == target:
                    return prob
        for node, prob in leafs:
            if node == target:
                return prob
        return 0