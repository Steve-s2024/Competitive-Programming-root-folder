# brute force: tle
'''class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums1)):
            nums = []
            for j in range(len(nums1)):
                if nums1[j] < nums1[i]:
                    nums.append(nums2[j])

            res.append(sum(sorted(nums, reverse=True)[:k]))
        return res'''

# don't know name type of solution... haha
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        minHeap = []
        heapq.heapify(minHeap)
        arr = [[nums1[i], nums2[i]] for i in range(len(nums1))]
        arr.sort(key = lambda i : i[0])
        # print(arr)
        sum_ = 0
        hashMap = {}
        for i in range(len(arr)):
            if arr[i][0] not in hashMap:
                hashMap[arr[i][0]] = sum_
            sum_ += arr[i][1]
            heapq.heappush(minHeap, arr[i][1])
            if len(minHeap) > k:
                sum_ -= heapq.heappop(minHeap)
        # print(hashMap)
        res = [0] * len(nums1)
        for idx, num in enumerate(nums1):
            res[idx] = hashMap[num]
        return res
