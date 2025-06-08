


# doesn't work
class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        graph = defaultdict(list)
        parents = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            parents[b].append(a)
        visited = set()

        minHeap = []
        heapq.heapify(minHeap)
        res = 0
        order = 1

        def dfs(node):
            nonlocal res, order
            for parent in parents[node]:
                if parent not in visited:
                    dfs(parent)
            while minHeap:
                (score_, ord_) = heapq.heappop(minHeap)
                print(score_, ord_)
                res += score_ * ord_
            heapq.heappush(minHeap, (score[node], order))
            order += 1
            visited.add(node)
            for child in graph[node]:
                visited.add(child)
                dfs(child)

        visited.add(0)
        dfs(0)

        while minHeap:
            (score_, ord_) = heapq.heappop(minHeap)
            print(score_, ord_)
            res += score_ * ord_

        return res