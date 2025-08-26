# annoying question, but taught me a lesson that the BFS I am doing, although it will be O(n) for normal graph, but for
# the graph I constructed here, there can be duplicate edges, and now the worst case BFS will cost O(n^2). I will then
# need to do the BFS visited judgement a bit different to reduce it back to n(0):83%
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda i: i[2])
        n = len(meetings)
        cands = set([0, firstPerson])
        i = 0
        while i < n:
            j = i
            q = deque()
            graph = defaultdict(list)
            vis = set()
            while j < n and meetings[j][2] == meetings[i][2]:
                a, b, _ = meetings[j]
                if a in cands: q.append(a)
                if b in cands: q.append(b)
                graph[a].append(b)
                graph[b].append(a)
                j += 1

            while q:
                node = q.popleft()
                if node in vis: continue
                vis.add(node)
                cands.add(node)

                for nxt in graph[node]:
                    if nxt not in vis: q.append(nxt)
            i = j
        return list(cands)

