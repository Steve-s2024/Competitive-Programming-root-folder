# pretty proud of myself after see through the BFS solution that start from nodes with degree of 1, call them leaf
# nodes, and peel layer by layer to get the target node where the tree has the shortest depth with it being the root. all
# this will happen in linear time. though at the end get tricked by not checking the diameter of each tree themselves, but
# still feel happy: 74%
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        tree1, tree2 = defaultdict(list), defaultdict(list)
        deg1, deg2 = [0] * (len(edges1) + 1), [0] * (len(edges2) + 1)
        for u, v in edges1:
            deg1[u] += 1
            deg1[v] += 1
            tree1[u].append(v)
            tree1[v].append(u)
        for u, v in edges2:
            deg2[u] += 1
            deg2[v] += 1
            tree2[u].append(v)
            tree2[v].append(u)

        res1 = 0
        di1 = 0
        q = deque()
        for i, d in enumerate(deg1):
            if d == 1: q.append(i)

        while q:
            if len(q) == 1:
                di1 = res1 * 2
                break
            for _ in range(len(q)):
                node = q.popleft()
                for nxt in tree1[node]:
                    deg1[nxt] -= 1
                    if deg1[nxt] == 1: q.append(nxt)
            res1 += 1
            if not len(q):
                di1 = 2 * res1 - 1

        res2 = 0
        di2 = 0
        q = deque()
        for i, d in enumerate(deg2):
            if d == 1: q.append(i)

        while q:
            if len(q) == 1:
                di2 = res2 * 2
                break
            for _ in range(len(q)):
                node = q.popleft()
                for nxt in tree2[node]:
                    deg2[nxt] -= 1
                    if deg2[nxt] == 1: q.append(nxt)
            res2 += 1
            if not len(q): di2 = 2 * res2 - 1
        return max(di1, di2, res1 + res2 + 1)
