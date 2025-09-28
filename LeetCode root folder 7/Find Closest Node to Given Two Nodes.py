# unicyclic tree graph, simple path iteration solution: 87%
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dst = [inf] * n
        x = node1
        d = 0
        while x != -1 and dst[x] == inf:
            dst[x] = d
            d += 1
            x = edges[x]

        dst2 = [inf] * n
        x = node2
        d = 0
        res = inf
        midst = inf
        while x != -1 and dst2[x] == inf:
            dst2[x] = d
            if dst[x] != inf:
                mx = max(dst2[x], dst[x])
                if mx == midst: res = min(x, res)
                if mx < midst:
                    midst = mx
                    res = x
            d += 1
            x = edges[x]
        return res if res != inf else -1
