# idk why this question is even here, the constraint clearly
# forbids you to do this approach, but it actually is the approach...
#: 46%
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def checkIfValid(hashMap):
            vals = list(hashMap.values())
            prev = vals[0]
            for val in vals:
                if val != prev:
                    return False
            return True

        n = len(s)
        dp = {}
        def recursive(i):
            nonlocal n
            if i in dp:
                return dp[i]
            if i >= n:
                return 0
            
            hashMap = defaultdict(int)
            res = float('inf')
            for j in range(i, n):
                hashMap[s[j]]+=1
                if checkIfValid(hashMap):
                    res = min(res, recursive(j+1) + 1)
            dp[i] = res
            return res
                
        return recursive(0)