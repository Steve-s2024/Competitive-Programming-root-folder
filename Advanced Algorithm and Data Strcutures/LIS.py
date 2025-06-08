# pretty interesting algorithm, but I don't fully understand
# why it works.

# this implementation only find the length of the LIS, not the actual LIS
def LIS(nums):
    arr = []
    n = len(nums)
    for i in range(n):
        l, r = 0, len(arr)
        while l < r:
            m = (r+l)//2
            if arr[m] >= nums[i]:
                r = m
            elif arr[m] < nums[i]:
                l = m+1
        if l < len(arr):
            arr[l] = nums[i]
        else:
            arr.append(nums[i])
    print(len(arr))

LIS([1,3,2,1,5,3])
LIS([1,3,2,1,5,3,6,4,7,2,2,1,25,4])
LIS([5,3,2,5,6,2,1,3,6,4,3,12,1,23])