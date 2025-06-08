# my brain is damage by debugging this question...: 5%
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(tasks)
        ans = [-1] * n
        minHeap = []
        hashMap = {}
        heapq.heapify(minHeap)
        for server, weight in enumerate(servers):
            if weight not in hashMap:
                heap = []
                heapq.heapify(heap)
                hashMap[weight] = heap
            heapq.heappush(hashMap[weight], server)
        # print(hashMap)

        for key, val in hashMap.items():
            heapq.heappush(minHeap, (key, val))

        jobQueue = deque()
        serverHeap = []
        heapq.heapify(serverHeap)
        for i, t in enumerate(tasks):
            jobQueue.append((i, t))
            while serverHeap and serverHeap[0][0] <= i:
                [tmp, server] = heapq.heappop(serverHeap)
                weight = servers[server]
                heapq.heappush(hashMap[weight], server)
                if len(hashMap[weight]) == 1:
                    heapq.heappush(minHeap, (weight, hashMap[weight]))

            while minHeap and jobQueue:
                # assign server for task t
                [idx, task] = jobQueue.popleft()
                server = heapq.heappop(minHeap[0][1])
                heapq.heappush(serverHeap, (i + task, server))  # the server will be free at time+t time
                if not minHeap[0][1]:
                    heapq.heappop(minHeap)
                ans[idx] = server

        time = n
        while jobQueue:
            if not minHeap:
                time = max(time, serverHeap[0][0])
            while serverHeap and serverHeap[0][0] <= time:
                [tmp, server] = heapq.heappop(serverHeap)
                weight = servers[server]
                heapq.heappush(hashMap[weight], server)
                if len(hashMap[weight]) == 1:
                    heapq.heappush(minHeap, (weight, hashMap[weight]))

            while minHeap and jobQueue:
                # assign server for task t
                [idx, task] = jobQueue.popleft()
                server = heapq.heappop(minHeap[0][1])
                heapq.heappush(serverHeap, (time + task, server))  # the server will be free at time+t time
                if not minHeap[0][1]:
                    heapq.heappop(minHeap)
                ans[idx] = server
            time += 1
        return ans


# don't know what's wrong with this, and the code is too complicated
# that I wouldn't willing to debug: WA
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(tasks)
        ans = [-1] * n
        minHeap = []
        hashMap = {}
        heapq.heapify(minHeap)
        for server, weight in enumerate(servers):
            if weight not in hashMap:
                heap = []
                heapq.heapify(heap)
                hashMap[weight] = heap
            heapq.heappush(hashMap[weight], server)
        # print(hashMap)

        for key, val in hashMap.items():
            heapq.heappush(minHeap, (key, val))

        serverHeap = []
        heapq.heapify(serverHeap)
        time = 0
        for i, t in enumerate(tasks):
            if not minHeap:
                time = max(time, serverHeap[0][0])

            while serverHeap and serverHeap[0][0] <= time:
                [tmp, server] = heapq.heappop(serverHeap)
                weight = servers[server]
                heapq.heappush(hashMap[weight], server)
                if len(hashMap[weight]) == 1:
                    heapq.heappush(minHeap, (weight, hashMap[weight]))

            # assign server for task t
            server = heapq.heappop(minHeap[0][1])
            heapq.heappush(serverHeap, (time + t, server))  # the server (an index) will be free at i+t time
            if minHeap and not minHeap[0][1]:
                heapq.heappop(minHeap)
            ans[i] = server
            time += 1
        return ans