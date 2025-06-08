# neetcode's idea, binary search: 35%
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # binary search solution
        left, right = 1, min(ranks)*pow(cars, 2)
        minTime = right
        while left <= right:
            m = (left+right) // 2 # m is the time i want to test
            cTotal = 0
            for r in ranks:
                # let t be the time for the current guy
                # t shouldn't exceed m, let c be the number of cars this guy fix
                # so, we have m >= r * c^2 --> sqrt(m / r) >= c
                # to maximize c without exceed m, let it be int(sqrt(m/r))
                c = int(math.sqrt(m/r))
                cTotal += c

            # if we can fix all the cars with the time limit 'm', then try left range, otherwise try right range
            if cTotal >= cars:
                right = m-1
                minTime = m
            else:
                left = m+1
        return minTime
            
            

# its similar to the removing mountain question,
# I therefore used the same approach, and it worked
# but apparently it is not close to optimal:5%

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        minHeap = []
        for r in ranks:
            minHeap.append((r*pow(1, 2), r, 1))
        heapq.heapify(minHeap)
        minTime = 0
        while cars:
            [t, r, c] = heapq.heappop(minHeap)
            minTime = t
            c += 1
            heapq.heappush(minHeap, (r*pow(c, 2), r, c))
            cars -= 1
        return minTime


