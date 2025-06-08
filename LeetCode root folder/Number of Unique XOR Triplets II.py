# passed: 70%, dumb constraint, dumb question. 
# this has the exact complexity as any of the other three
# below, but this is the only one passed. 
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        hashSet = set()
        tmp = []
        for num in nums:
            if num not in hashSet:
                hashSet.add(num)
                tmp.append(num)

        p = 1
        max_ = max(tmp)
        while p <= max_:
            p *= 2
        n = len(tmp)
        mp = [False] * p

        for i in range(n):
            for j in range(n):
                mp[tmp[i]^tmp[j]] = True
        
        res = set()
        for tar in range(p):
            if tar not in hashSet:
                for num in nums:
                    if mp[tar^num]:
                        res.add(tar)
        return len(res) + n            


# solution no.3: WA
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def recursive(remain, cur):
            nonlocal n
            if remain == 0:
                return set([cur])

            hashSet = set()
            for i in range(n):
                hashSet = hashSet.union(recursive(remain-1, cur^nums[i]))
            return hashSet
        hashSet = recursive(2, 0)

        # print(hashSet)
        st = set(nums)
        res = set()
        p = 1
        max_ = max(nums)
        while p <= max_:
            p *= 2
        for i in range(p):
            if i not in st:
                for num in nums:
                    if num ^ i in hashSet:
                        res.add(i)
            
        return len(res) + n

# solution no.2: TLE
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def recursive(remain, cur):
            nonlocal n
            if remain == 0:
                return set([cur])

            hashSet = set()
            for i in range(n):
                hashSet = hashSet.union(recursive(remain-1, cur^nums[i]))
            return hashSet
        hashSet = recursive(2, 0)

        # print(hashSet)
        res = set()
        for val in hashSet:
            for i in range(n):
                res.add(val ^ nums[i])
        return len(res)

        

# dp: TLE
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def recursive(remain, cur):
            nonlocal n
            if remain == 0:
                return set([cur])
            if (remain, cur) in dp:
                return dp[(remain, cur)]
            hashSet = set()
            for i in range(n):
                hashSet = hashSet.union(recursive(remain-1, cur^nums[i]))
            dp[(remain, cur)] = hashSet
            return hashSet
        return len(recursive(3, 0))