# union find and anding all the weights in each cluster greedy solution: 12%
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        vis = set()
        mp = {}
        group = 0
        for i in range(n):
            if i not in vis:
                vis.add(i)
                anding = (1<<31)-1
                tmp = []
                q = deque([i])
                while q:
                    src = q.popleft()
                    tmp.append(src)
                    for nxt, wei in graph[src]:
                        anding &= wei
                        if nxt not in vis:
                            vis.add(nxt)
                            q.append(nxt)
                for node in tmp: mp[node] = (group, anding)
                group += 1
        ans = []
        for src, dst in query:
            if src not in mp or dst not in mp or mp[src][0] != mp[dst][0]: ans.append(-1)
            else: ans.append(mp[src][1])
        return ans



# WA

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        vis = set()
        mp = {}
        group = 0
        for u, v, w in edges:
            if (u, v, w) not in vis:
                tmp = set()
                andRes = u
                q = deque([u])
                while q:
                    src = q.popleft()
                    tmp.add(src)
                    for nxt, wei in graph[u]:
                        if (src, nxt, wei) not in vis:
                            vis.add((src, nxt, wei))
                            q.append(nxt)
                            andRes &= wei
                for node in tmp: mp[node] = (group, andRes)
                group += 1
        # print(mp)
        ans = []
        for src, dst in query:
            if src not in mp or dst not in mp:
                ans.append(-1)
            elif mp[src][0] != mp[dst][0]:
                ans.append(-1)
            else:
                ans.append(mp[src][1])

        return ans