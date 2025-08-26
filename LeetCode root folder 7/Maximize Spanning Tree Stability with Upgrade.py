# small issue to fix
class Solution:
    def checkCycle(self, graph):
        q = deque([(0, -1)])
        vis = set()
        while q:
            node, par = q.popleft()
            for nxt in graph[node]:
                if nxt == par: continue
                if nxt in vis: return True
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
            wei, node = heapq.heappop(maxheap)
            if wei == -inf: wei, node = node
            else: wei = -wei
            if node in vis: continue
            if wei == -inf: ws.append((wei, 1))
            else: ws.append((wei, 0))
            vis.add(node)
            for nxt, w in mgraph[node]:
                heapq.heappush(maxheap, (-inf, (nxt, w)))
            for nxt, w in graph[node]:
                if nxt in vis: continue
                heapq.heappush(maxheap, (-w, nxt))
        ws.pop(0)
        print(ws)
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