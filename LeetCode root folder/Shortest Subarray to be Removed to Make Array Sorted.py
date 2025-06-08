# two pointer & binary search solution: 5% 
# based on the performance, is there somehow a greedy solution?
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        arr.insert(0, -float('inf'))
        n = len(arr)
        i = n-2
        while i >= 0 and arr[i] <= arr[i+1]:
            i -= 1
        L, R = i+1, n-1
        def binarySearch(tar):
            nonlocal L, R
            if tar > arr[R]:
                return R+1
            if tar < arr[L]:
                return L
            res = 0
            l, r = L, R
            while l <= r:
                m = (l + r) // 2
                if arr[m] >= tar:
                    res = m
                    r = m-1
                elif arr[m] < tar:
                    l = m+1
            return res

        minLen = float('inf')
        for i in range(n):
            if i != 0 and (arr[i] < arr[i-1]):
                break
            j = binarySearch(arr[i])
            # print(i, j)
            minLen = min(max(j-i-1, 0), minLen)

        return minLen

                

# two pointer solution: TLE
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        minLen = float('inf')
        arr.insert(0, -float('inf'))
        n = len(arr)
        for i in range(n):
            if i != 0 and (arr[i] < arr[i-1]):
                break
            j = n-1
            while j > i:
                if arr[j] < arr[i] or (j != n-1 and arr[j] > arr[j+1]):
                    break
                j -= 1
            # print(i, j)
            minLen = min(j-i, minLen)

        return minLen

                