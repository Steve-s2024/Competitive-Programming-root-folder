# gambled a bit here, but luckly it did work, and its neat: 6%
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            if nums[i] != 1:
                cnt += 1
        if cnt != n:
            return cnt

        factors = []
        def factorized(num):
            f = 2
            primes = []
            while f*f <= num:
                while num%f == 0:
                    num /= f
                    primes.append(f)
                f+=1
            if num > 1:
                primes.append(num)
            return primes

        for i in range(n):
            factors.append(factorized(nums[i]))
        # print(factors)


        res = float('inf')
        for i in range(n):
            cands = factors[i][:]
            for j in range(i+1, n):
                tmp = []
                i1, i2 = 0, 0
                while i1 < len(cands) and i2 < len(factors[j]):
                    val1, val2 = cands[i1], factors[j][i2]
                    if val1 < val2:
                        i1+=1
                    elif val1 > val2:
                        i2+=1
                    else:
                        tmp.append(val1)
                        i1+=1
                        i2+=1
                cands = tmp
                if len(cands) == 0:
                    res = min(res, j-i)
        # print(factors)
        if res == float('inf'):
            return -1
        return res + n-1
