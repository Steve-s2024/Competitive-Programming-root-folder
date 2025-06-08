# greedy solution no.2, very close to the right answer:
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        n = mountainHeight
        workerTimes.sort()
        workerTimes.insert(0, float('inf'))
        workerTimes.append(float('inf'))

        size = len(workerTimes)
        workload = [0] * size
        minTime = 0
        # print(workerTimes, workload)
        while n > 0:
            for i in range(1, len(workerTimes)-1):
                # workload[i] --> the height this worker is removing
                w1, w2, w3 = workerTimes[i-1], workerTimes[i], workerTimes[i+1]
                h1, h2, h3 = workload[i-1]+1, workload[i]+1, workload[i+1]+1
                t1, t2, t3 = w1*h1*(h1+1)/2, w2*h2*(h2+1)/2, w3*h3*(h3+1)/2
                if t1 >= t2 and t2 <= t3:
                    n-=1
                    minTime = max(minTime, t2)
                    workload[i]+=1
                    if n <= 0:
                        return int(minTime)



# greedy solution no.1, glitched:
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        n = mountainHeight
        groups = []
        hashMap = defaultdict(int)
        for t in workerTimes:
            if hashMap[t] == 0:
                groups.append(t)
            hashMap[t]+=1
        groups.sort()
        groups.append(float('inf'))
        groups.insert(0, float('inf'))
        # print(groups, hashMap)
        minTime = float('inf')
        groupHeight = defaultdict(int)
        while n > 0:
            for i in range(1, len(groups)-1):
                prevG, curG, nextG = groups[i-1], groups[i], groups[i+1]
                h1, h2, h3 = groupHeight[prevG]+1, groupHeight[curG]+1, groupHeight[nextG]+1
                t1, t2, t3 = prevG*h1*(h1+1)//2, curG*h2*h2+1//2, nextG*h3*(h3+1)//2
                s1 = hashMap[curG]
                while t1 >= t2 and t2 <= t3:
                    minTime = t1
                    h1+=1
                    n-=s1
                    groupHeight[curG]+=1
                    if n <= 0:
                        return minTime
                    t1 = curG*h1*(h1+1)//2
                    




# dp solution, O(10^9): TLE
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        n = mountainHeight
        workerTimes.sort()
        hashMap = defaultdict(int)

        groups = []
        for t in workerTimes:
            if hashMap[t] == 0:
                groups.append(t)
            hashMap[t]+=1

        dp = {}
        def recursive(remain, i):
            if (remain, i) in dp:
                return dp[(remain, i)]

            if remain <= 0:
                return 0
            if i >= len(groups):
                return float('inf')
            
            groupSize = hashMap[groups[i]]
            heightPerWorker = 0
            totalHeight = 0
            minTime = float('inf')
            while True:
                tmp = heightPerWorker*(heightPerWorker+1)//2
                time = groups[i]*tmp
                minTime = min(minTime, max(recursive(remain-totalHeight, i+1), time))
                if totalHeight >= remain:
                    break
                heightPerWorker+=1
                totalHeight+=groupSize
            # print((remain, i), minTime)
            dp[(remain, i)] = minTime
            return minTime
        return recursive(n, 0)


# template for dp solution
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        n = mountainHeight
        workerTimes.sort()
        hashMap = defaultdict(int)

        groups = []
        for t in workerTimes:
            if hashMap[t] == 0:
                groups.append(t)
            hashMap[t]+=1

        def recursive(remain, i, t):
            if remain <= 0:
                # print(t)
                return 
            if i >= len(groups):
                return 
            
            
            groupSize = hashMap[groups[i]]
            heightPerWorker = 0
            totalHeight = 0
            while True:
                tmp = heightPerWorker*(heightPerWorker+1)//2
                time = workerTimes[i]*tmp
                recursive(remain-totalHeight, i+1, max(time, t))
                if totalHeight >= remain:
                    break
                heightPerWorker+=1
                totalHeight+=groupSize

        recursive(n, 0, 0)