# super boring question: 43%
class Solution:
    def checkCycle(self, graph):
        if not graph: return False
        vis = set()
        for src in graph.keys():
            if src in vis: continue
            q = deque([(src, -1)])
            vis.add(src)
            while q:
                node, par = q.popleft()
                for nxt, _ in graph[node]:
                    if nxt == par: continue
                    if nxt in vis: return True
                    vis.add(nxt)
                    q.append((nxt, node))
        return False

    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        mad = set()
        mgraph = defaultdict(list)
        graph = defaultdict(list)
        for u, v, w, f in edges:
            if f:
                mgraph[u].append((v, w))
                mgraph[v].append((u, w))
            else:
                graph[u].append((v, w))
                graph[v].append((u, w))
        if self.checkCycle(mgraph): return -1

        vis = set()
        maxheap = [(0, 0)]
        ws = []
        while maxheap:
            tmp, node = heapq.heappop(maxheap)
            if tmp == -inf: wei, node = node
            else: wei = -tmp
            if node in vis: continue
            if tmp == -inf: ws.append((wei, 1))
            else: ws.append((wei, 0))
            vis.add(node)
            for nxt, w in mgraph[node]:
                heapq.heappush(maxheap, (-inf, (w, nxt)))
            for nxt, w in graph[node]:
                if nxt in vis: continue
                heapq.heappush(maxheap, (-w, nxt))
        ws.pop(0)
        if len(ws) != n-1: return -1
        ws.sort()

        res = inf
        for w, f in ws:
            if f: res = min(res, w)
            else:
                if k:
                    res = min(res, w*2)
                    k -= 1
                else: res = min(res, w)
        return res