# today's contest is so fking annoying...
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        nodetog = {}
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        group = defaultdict(list)
        gid = 0

        def dfs(node):
            group[gid].append(node)
            nodetog[node] = gid
            for nxt in graph[node]:
                if nxt in vis: continue
                vis.add(nxt)
                dfs(nxt)

        vis = set()
        for i in range(1, c + 1):
            if i in vis: continue
            vis.add(i)
            dfs(i)
            gid += 1

        # print(group)
        mp = {}
        for key, val in group.items():
            heapq.heapify(val)
            mp[key] = set(val)

        # print(mp)
        ans = []
        for t, x in queries:
            gid = nodetog[x]
            if t == 2:
                if x in mp[gid]: mp[gid].remove(x)
            else:
                if x in mp[gid]:
                    ans.append(x)
                else:
                    while group[gid] and group[gid][0] not in mp[gid]: heapq.heappop(group[gid])
                    if group[gid]:
                        ans.append(group[gid][0])
                    else:
                        ans.append(-1)

        return ans

