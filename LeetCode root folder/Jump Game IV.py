# bfs solution for minPath: 94%
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        hashMap = defaultdict(list)
        for i in range(n):
            hashMap[arr[i]].append(i)

        q = deque([0])
        visited = set()
        visited.add(0)
        visited2 = set()
        res = 0
        while q:
            l = len(q)
            while l:
                i = q.popleft()
                if i == n-1:
                    return res
                if i-1 not in visited and i > 0:
                    q.append(i-1)    
                    visited.add(i-1)          
                if i+1 not in visited and i < n-1:
                    q.append(i+1)
                    visited.add(i+1)
                if arr[i] not in visited2:
                    visited2.add(arr[i])
                    for nextI in hashMap[arr[i]]:
                        if nextI not in visited and nextI != i:
                            q.append(nextI)
                            visited.add(nextI)
                l-=1
            res+=1



# the dp template with recursion, but dp will not work in this case...
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        hashMap = defaultdict(list)
        for i in range(n):
            hashMap[arr[i]].append(i)

        visited = set()
        def recursive(i):
            if i >= n-1:
                return 0
            if i in visited or i not in range(n):
                return float('inf')

            visited.add(i)
            
            minDst = min(
                recursive(i-1),
                recursive(i+1)
            )
            for nextI in hashMap[arr[i]]:
                if nextI != i:
                    minDst = min(minDst, recursive(nextI))
            visited.remove(i)
            return minDst + 1
        return recursive(0)




