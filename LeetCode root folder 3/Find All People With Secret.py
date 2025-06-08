# not really the BFS's problem, it turns out by BFS worked exactly as expected
# and with the best time complexity, the reason is in when initializing the sources
# : 89%
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda i:i[2])

        ift = set()
        ift.add(0)
        ift.add(firstPerson)
        m = len(meetings)
        i = 0
        while i < m:
            time = meetings[i][2]
            graph = defaultdict(list)
            q = deque()
            vis = set()
            while i < m and meetings[i][2] == time:
                a, b, t = meetings[i]
                graph[a].append(b)
                graph[b].append(a)
                if a in ift:
                    if a not in vis:
                        q.append(a)
                        vis.add(a)
                if b in ift:
                    if b not in vis:
                        q.append(b)
                        vis.add(b)
                i+=1
            while q:
                p = q.popleft()
                for nxt in graph[p]:
                    if nxt in ift:
                        continue
                    ift.add(nxt)
                    q.append(nxt)

        return list(ift)



# Ah, it's because the time complexity doing the BFS below(TLE) can actually
# be unpredictable, it will range from linear to potentially n^2.
# here by pruning before the for loop for nxt nodes, it helps reduce the
# complexity to close linear: 86%
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda i:i[2])

        ift = set()
        ift.add(0)
        ift.add(firstPerson)
        m = len(meetings)
        i = 0
        while i < m:
            time = meetings[i][2]
            graph = defaultdict(list)
            q = deque()
            while i < m and meetings[i][2] == time:
                a, b, t = meetings[i]
                graph[a].append(b)
                graph[b].append(a)
                if a in ift:
                    q.append(a)
                if b in ift:
                    q.append(b)
                i+=1
            vis = set()
            while q:
                p = q.popleft()
                if p in vis:
                    continue
                vis.add(p)
                for nxt in graph[p]:
                    if nxt in ift:
                        continue
                    ift.add(nxt)
                    q.append(nxt)

        return list(ift)



# this is clearly nlogn solution, why it hit TLE?
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda i: i[2])

        ift = set()
        ift.add(0)
        ift.add(firstPerson)
        m = len(meetings)
        i = 0
        while i < m:
            time = meetings[i][2]
            graph = defaultdict(list)
            q = deque([])
            vis = set()
            while i < m and meetings[i][2] == time:
                a, b, t = meetings[i]
                graph[a].append(b)
                graph[b].append(a)
                if a in ift:
                    q.append(a)
                    vis.add(a)
                if b in ift:
                    q.append(b)
                    vis.add(b)
                i += 1

            while q:
                p = q.popleft()
                for nxt in graph[p]:
                    if nxt in vis:
                        continue
                    vis.add(nxt)
                    ift.add(nxt)
                    q.append(nxt)

        # print(ift)
        return list(ift)


