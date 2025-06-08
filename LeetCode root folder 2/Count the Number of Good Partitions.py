# I tried to implement the pow function myself, but 
# I guess the built-in one is already optimized by the 
# same way: 7%

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        idxMp = defaultdict(deque)
        for i in range(n):
            idxMp[nums[i]].append(i)
        MOD = 1000000007
        i = 0
        l, r = 0, 0
        interval = []
        while i < n:
            val = nums[i]            
            if idxMp[val] and idxMp[val][0] == i:
                idxMp[val].popleft()
            if idxMp[val]:
                r = max(r, idxMp[val][0])
            if i == r:
                if l!=r:
                    interval.append((l, r))
                l=r+1
                r+=1
            i += 1
        # print(interval)  
        for l, r in interval:
            n -= r-l
        if n-1:
            res = 1
            tar = str(bin(n-1))[2:]
            m = len(tar)
            # print(tar)
            for i in range(m-1, -1, -1):
                if tar[i] == '1':
                    cap = pow(2, m-i-1)
                    powOfTwo = 2
                    cnt = 1
                    while cnt < cap:
                        powOfTwo *= powOfTwo
                        powOfTwo %= MOD
                        cnt *= 2
                    res *= powOfTwo
                    res %= MOD
            return res

        return 1        
                


        

# excluded the dp part, and linear: 7%

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        idxMp = defaultdict(deque)
        for i in range(n):
            idxMp[nums[i]].append(i)
        MOD = 1000000007
        i = 0
        l, r = 0, 0
        interval = []
        while i < n:
            val = nums[i]            
            if idxMp[val] and idxMp[val][0] == i:
                idxMp[val].popleft()
            if idxMp[val]:
                r = max(r, idxMp[val][0])
            if i == r:
                if l!=r:
                    interval.append((l, r))
                l=r+1
                r+=1
            i += 1
        # print(interval)  
        for l, r in interval:
            n -= r-l
        
        return pow(2, n-1) % MOD
        


# dp solution with interval merging, linear but TLE, why?

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        idxMp = defaultdict(deque)
        for i in range(n):
            idxMp[nums[i]].append(i)
        
        i = 0
        l, r = 0, 0
        interval = []
        while i < n:
            val = nums[i]            
            if idxMp[val] and idxMp[val][0] == i:
                idxMp[val].popleft()
            if idxMp[val]:
                r = max(r, idxMp[val][0])
            if i == r:
                if l!=r:
                    interval.append((l, r))
                l=r+1
                r+=1
            i += 1
        # print(interval)  
        hashMap = {}
        for l, r in interval:
            hashMap[l] = r
        dp = {}
        dp[n] = 1
        def recursive(i):
            nonlocal n
            if i in dp:
                return dp[i]
            res = 0
            j = i
            while j < n:
                if j in hashMap:
                    j = hashMap[j]
                res += recursive(j+1)            
                j+=1
            res %= 1000000007
            dp[i] = res
            return res
        return recursive(0)