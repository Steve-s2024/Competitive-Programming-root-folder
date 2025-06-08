# here I have written an algorithm for radix sorting of numbers of the same length
from collections import defaultdict

def radixSort(nums):
    for pos in range(len(nums[0]) - 1, -1, -1):
        tmp = defaultdict(list)
        for num in nums:
            tmp[num[pos]].append(num)
        arr = []
        for i in range(10):
            arr += tmp[str(i)]
        nums = arr
    return nums

nums = ['123', '231', '545', '522', '121']
print(radixSort(nums))
