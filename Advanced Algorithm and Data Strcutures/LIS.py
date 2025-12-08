# pretty interesting algorithm

# this implementation only find the length of the LIS, not the actual LIS. for the actual LIS, use the algo below "LISSequence"
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


# return not just the length of the LIS, but the entire sequence. I added a restoring the sequence part. doesn't worsen the
# time complexity of the code above
from math import inf
def LISSequence(nums):
    arr = []
    mp = {}
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
            mp[nums[i]] = (arr[l-1] if l else -inf)
            arr[l] = nums[i]
        else:
            mp[nums[i]] = (arr[-1] if arr else -inf)
            arr.append(nums[i])


    ans = []
    cr = arr[-1]
    while cr != -inf:
        ans.append(cr)
        cr = mp[cr]
    print(ans[::-1])


LISSequence([1,3,2,1,5,3])
LISSequence([1,3,2,1,5,3,6,4,7,2,2,1,25,4])
LISSequence([5,3,2,5,6,2,1,3,6,4,3,12,1,23])
