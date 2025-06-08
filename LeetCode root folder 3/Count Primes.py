# fastest: 51%
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        arr = [True] * n
        arr[0] = False
        arr[1] = False
        cap = int(math.sqrt(n))
        for i in range(cap+1):
            if arr[i]:
                for j in range(i*i, n, i):
                    arr[j] = False

        res = 0
        for i in range(n):
            if arr[i]:
                res += 1
        return res

# fast prime sieve, but not the fastest: 49%
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        arr = [True] * n
        arr[0] = False
        arr[1] = False
        cap = int(math.sqrt(n))
        for i in range(cap+1):
            if arr[i]:
                for j in range(i+i, n, i):
                    arr[j] = False

        res = 0
        # primes = []
        for i in range(n):
            if arr[i]:
                res += 1
                # primes.append(i)
        # print(primes)
        return res