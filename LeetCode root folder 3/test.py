# ████████╗██╗███╗░░██╗  ██╗░░░░░███████╗
# ╚══██╔══╝██║████╗░██║  ██║░░░░░██╔════╝
# ░░░██║░░░██║██╔██╗██║  ██║░░░░░█████╗░░
# ░░░██║░░░██║██║╚████║  ██║░░░░░██╔══╝░░
# ░░░██║░░░██║██║░╚███║  ███████╗███████╗
# ░░░╚═╝░░░╚═╝╚═╝░░╚══╝  ╚══════╝╚══════╝
#   __________________
#  | ________________ |
#  ||          ____  ||
#  ||   /\    |      ||
#  ||  /__\   |      ||
#  || /    \  |____  ||
#  ||________________||
#  |__________________|
#  \###################\
#   \###################\
#    \        ____       \
#     \_______\___\_______\
# An AC a day keeps the doctor away. (tin_le)

from collections import defaultdict, deque, Counter
import heapq, cmath


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

        print(ift)






