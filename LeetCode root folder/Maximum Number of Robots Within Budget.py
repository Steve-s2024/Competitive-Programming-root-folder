# the solution is not complicated, a sliding window approach
# however, it is very eazy to make mistake the first time
# trying sliding window with so many data to maintain.
#: 17%

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        l, r = 0, 0
        costSum = 0
        res = 0
        maxHeap = []
        hashMap = defaultdict(int)
        heapq.heapify(maxHeap)

        while r < n:
            while r < n:
                t = chargeTimes[r]
                tmp = max(-maxHeap[0] if maxHeap else 0, t) + (r-l+1)*(costSum + runningCosts[r])
                # print(r, tmp, (r-l+1), (costSum + runningCosts[r]))
                if tmp > budget:
                    break

                heapq.heappush(maxHeap, -t)
                hashMap[t]+=1
                costSum += runningCosts[r]
                r+=1
            # print(l, r, costTotal)

            res = max(res, r-l)
            if r > l:
                hashMap[chargeTimes[l]]-=1
                while maxHeap and hashMap[-maxHeap[0]] == 0:
                    heapq.heappop(maxHeap)
                costSum -= runningCosts[l]
                l += 1
            else:
                l += 1
                r += 1

        return res