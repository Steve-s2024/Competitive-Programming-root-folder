# maxHeap solution:
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxHeap = []
        for p, t in classes:
            prev, next_ = float(p)/t, float(p+1)/(t+1)
            maxHeap.append([-(next_ - prev), p, t])
        heapq.heapify(maxHeap)
        
        while extraStudents:
            [incre, p, t] = heapq.heappop(maxHeap)
            p, t = p+1, t+1
            prev, next_ = float(p)/t, float(p+1)/(t+1)
            heapq.heappush(maxHeap, [-(next_ - prev), p, t])
            extraStudents-=1
        
        res = 0
        for incre, p, t in maxHeap:
            res += float(p)/t
        return res / len(classes)


# depricated
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        classes.sort(key = lambda i : i[1])
        # print(classes)
        res = 0
        for p, t in classes:
            if extraStudents:
                extraPassed = min(extraStudents, t - p)
                extraStudents -= extraPassed
                p += extraPassed
            res += float(p) / t
        return res / len(classes)