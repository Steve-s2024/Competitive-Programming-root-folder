# this question is pretty interesting, its implementation
# is very simple for a hard question, but to come up with the
# solution, it involves a new way of thinking in greedy: 25%
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        n = len(rolls)
        hashSet = set()
        res = 0
        i = 0
        while i < n:
            while i < n and len(hashSet) < k:
                hashSet.add(rolls[i])
                i+=1
            if len(hashSet) == k:
                res += 1
            hashSet.clear()
        return res+1
            
