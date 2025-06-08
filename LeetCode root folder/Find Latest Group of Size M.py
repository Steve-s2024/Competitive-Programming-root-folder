# elegent one demensional union find solution: 11.11%
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        boundMap = defaultdict(int)
        lenMap = defaultdict(int)
        nums = [0] * n
        res = -1
        for i in range(n):
            idx = arr[i]-1
            l, r = idx, idx
            if idx > 0 and nums[idx-1] == 1:
                [L, R] = boundMap[idx-1]
                lenMap[R-L+1] -= 1
                l = L
            if idx < n-1 and nums[idx+1] == 1:
                [L, R] = boundMap[idx+1]
                lenMap[R-L+1] -= 1
                r = R
            
            boundMap[l] = [l, r]
            boundMap[r] = [l, r]
            lenMap[r-l+1] += 1
            nums[idx] = 1
            # print(lenMap)
            if lenMap[m] > 0:
                res = i+1
        return res

# depricated
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        nums = [0] * n
        res = 0
        hashSet = set()
        for i in range(n):
            pos = arr[i]-1
            if (
                (pos == 0 or arr[pos-1] != 1) and
                (pos == n-1 or arr[pos+1] != 1)
            ):
                hashSet.add(arr[i])
            else:
                if arr[i]-1 in hashSet:
                    hashSet.remove(arr[i]-1)
                if arr[i]+1 in hashSet:
                    hashSet.remove(arr[i]+1)
            nums[pos] = 1
            if len(hashSet) > 0:
                res = i+1
        return res