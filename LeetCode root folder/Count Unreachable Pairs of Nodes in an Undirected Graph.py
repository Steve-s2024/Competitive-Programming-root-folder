# graph traverse solution, similar to that of count number of island:171
# ms
# Beats
# 88.95%


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def countSize(cur):
            count = 0
            visited.add(cur)
            for next_ in graph[cur]:
                if next_ not in visited:
                    count += countSize(next_)
            return count + 1

        hashMap = defaultdict(int)
        res = 0
        for src in graph:
            if src not in visited:
                hashMap[src] = countSize(src)

        # print(hashMap)
        arr = list(hashMap.values())
        total = sum(arr)
        copy = total
        for i in range(len(arr)):
            copy -= arr[i]
            res += arr[i] * copy
        for i in range(1, n - total + 1):
            res += n - i
        return res

