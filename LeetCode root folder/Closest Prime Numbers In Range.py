# brute force: tle
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr = [i for i in range(2, right + 1)]
        primes = []
        # print(arr)
        while arr and arr[0] ** 2 <= right:

            tmp = []
            ref = arr[0]
            primes.append(ref)
            for num in arr:
                if num % ref:
                    tmp.append(num)
            arr = tmp

        primes += arr
        # print(primes)
        min_ = float('inf')
        res = [-1, -1]
        for i in range(1, len(primes)):
            if primes[i - 1] >= left and primes[i] <= right:
                diff = primes[i] - primes[i - 1]
                if diff < min_:
                    min_ = diff
                    res = [primes[i - 1], primes[i]]
                if diff == 2:
                    return res
        return res

# brute force no.2: tle
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [i for i in range(2, right+1)]
        factor = 2
        while factor ** 2 <= right:
            tmp = []
            for num in primes:
                if num % factor or num == factor:
                    tmp.append(num)
            primes = tmp
            factor += 1
        # print(primes)
        min_ = float('inf')
        res = [-1, -1]
        for i in range(1, len(primes), 2):
            if primes[i-1] >= left and primes[i] <= right:
                diff = primes[i] - primes[i-1]
                if diff < min_:
                    min_ = diff
                    res = [primes[i-1], primes[i]]
        return res
