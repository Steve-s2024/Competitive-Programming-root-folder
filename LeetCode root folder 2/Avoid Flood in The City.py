# super un-intuitive solution, I slowly build it from grinding the problem
# but at least I solved it. maybe it is not intended to be solved this way,
# because binary search appeared in the topics: 62%
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        idxMp = defaultdict(deque)
        for i in range(n):
            idxMp[rains[i]].append(i)
        print([idxMp])

        hashSet = set()
        ans = [-1] * n
        minHeap = []
        heapq.heapify(minHeap)
        for i in range(n):
            rain = rains[i]
            if rain != 0:
                if i in hashSet:
                    return []
                idxMp[rain].popleft()
                if idxMp[rain]:
                    hashSet.add(idxMp[rain][0])
                    heapq.heappush(minHeap, idxMp[rain][0])
            else:
                if minHeap:
                    idx = heapq.heappop(minHeap)
                    ans[i] = rains[idx]
                    hashSet.remove(idx)
                else:
                    ans[i] = 1
        return ans


# solution no.1 by a vague idea of greedy in head, and I am very surprise that
# it worked: TLE
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        hashSet = set()
        ans = [-1] * n
        i = 0
        while i < n:
            rain = rains[i]
            if rain == 0:
                j = i + 1
                while j < n and rains[j] not in hashSet:
                    j += 1
                if j < n:
                    hashSet.remove(rains[j])
                    ans[i] = rains[j]
                else:
                    ans[i] = 1
            else:
                if rain in hashSet:
                    return []
                hashSet.add(rain)
            i += 1
        return ans