# insertion sort
def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0:
            a, b = arr[j-1], arr[j]
            if a > b:
                arr[j-1] = b
                arr[j] = a
                j -= 1
            else:
                break
    print(arr)

# bubbleSort([1,4,-23,-2,34,2,-34,5,12,1,23])


# merge sort
def mergeSort(arr):

    n = len(arr)
    def recursive(l, r):
        if l == r:
            return [arr[l]]
        m = (l+r)//2
        a, b = recursive(l, m), recursive(m+1, r)
        tmp = []
        i1, i2 = 0, 0
        while i1 < len(a) and i2 < len(b):
            if a[i1] < b[i2]:
                tmp.append(a[i1])
                i1 += 1
            else:
                tmp.append(b[i2])
                i2 += 1

        while i1 < len(a):
            tmp.append(a[i1])
            i1 += 1
        while i2 < len(b):
            tmp.append(b[i2])
            i2 += 1
        return tmp
    sortedArr = recursive(0, n-1)
    print(sortedArr)

# mergeSort([1,4,-23,-2,34,2,-34,5,12,1,23])



# quick sort
import random
def quickSort(arr):
    n = len(arr)

    def recursive(l, r):
        if l >= r:
            return
        a, b = [], []
        randIdx = random.randint(l, r)
        tar = arr[randIdx]
        mx, mi = arr[l], arr[l]
        for i in range(l, r+1):
            if arr[i] <= tar:
                a.append(arr[i])
            else:
                b.append(arr[i])
            mx = max(mx, arr[i])
            mi = min(mi, arr[i])
        if mi == mx:
            return

        for i in range(len(a)):
            arr[l+i] = a[i]
        for i in range(len(b)):
            arr[l+len(a)+i] = b[i]

        recursive(l, l+len(a)-1)
        recursive(l+len(a), r)
    recursive(0, n-1)
    print(arr)

# quickSort([1,4,-23,-2,34,2,-34,5,12,1,23])
# quickSort([1,4,-23,-2,34,2,-34,5,12,1,23,23,1,2,3,2,23,2,3,43,2,-123,32,-2323])



# radixSort: for sorting numbers lexicographically, so doesn't deal with negative numbers
from collections import defaultdict
def radixSort(arr):
    n = len(arr)

    def recursive(nums, i):
        if len(nums) == 1:
            return nums

        mp = defaultdict(list)
        for num in nums:
            s = str(num)
            if len(s) <= i:
                mp['_'].append(num)
            else:
                mp[s[i]].append(num)
        tmp = mp['_']
        for c in '0123456789':
            if len(mp[c]):
                for num in recursive(mp[c], i+1):
                    tmp.append(num)

        return tmp
    sortedArr = recursive(arr, 0)
    print(sortedArr)

# radixSort([1,4,23,2,34,2,34,5,12,1,23])


# heap sort, I imported my max heap class as the helper
# note that max heap will give elements in descending order
from PriorityQueue import maxHeap
def heapSort(arr):
    maxHeap.heapify(arr)
    res = []
    while arr:
        res.append(maxHeap.pop(arr))
    print(res)

# heapSort([1,4,23,2,34,2,34,5,12,1,23])
