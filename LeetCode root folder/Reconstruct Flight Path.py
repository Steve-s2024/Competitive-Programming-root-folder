# brute-force solution: time-limit exceeded
# I wonder why, cause NeetCode solution is more time-consuming than as mine, but he passed with 94ms

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        hashMap = defaultdict(int)
        graph = defaultdict(list)
        for src, dst in tickets:
            hashMap[(src, dst)] += 1
            graph[src].append(dst)
        for src in graph:
            graph[src].sort()

        path = []
        def dfs(src):
            path.append(src)
            # print(path)
            if len(path) == len(tickets)+1:
                return path
            for dst in graph[src]:
                if hashMap[(src, dst)]:
                    hashMap[(src, dst)] -= 1
                    res = dfs(dst)
                    if res:
                        return res
                    hashMap[(src, dst)] += 1
            path.pop()
        return dfs('JFK')

