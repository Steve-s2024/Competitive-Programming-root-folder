# generate by ChatGPT based on my sorting functions

import time
import random
from collections import defaultdict
from PriorityQueue import maxHeap

# --- Sorting Functions ---

def heapSort(arr):
    maxHeap.heapify(arr)
    res = []
    while arr:
        res.append(maxHeap.pop(arr))
    return res

def radixSort(arr):
    if not arr:
        return []
    def recursive(nums, i):
        if len(nums) <= 1:
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
            if c in mp:
                tmp.extend(recursive(mp[c], i + 1))
        return tmp
    return recursive(arr, 0)

def quickSort(arr):
    def recursive(l, r):
        if l >= r:
            return
        randIdx = random.randint(l, r)
        tar = arr[randIdx]
        a, b = [], []
        mi, mx = arr[l], arr[l]
        for i in range(l, r + 1):
            if arr[i] <= tar:
                a.append(arr[i])
            else:
                b.append(arr[i])
            mi = min(mi, arr[i])
            mx = max(mx, arr[i])
        if mi == mx:
            return
        for i in range(len(a)):
            arr[l + i] = a[i]
        for i in range(len(b)):
            arr[l + len(a) + i] = b[i]
        recursive(l, l + len(a) - 1)
        recursive(l + len(a), r)
    recursive(0, len(arr) - 1)
    return arr

def mergeSort(arr):
    if not arr:
        return []
    def recursive(l, r):
        if l == r:
            return [arr[l]]
        m = (l + r) // 2
        a, b = recursive(l, m), recursive(m + 1, r)
        tmp, i1, i2 = [], 0, 0
        while i1 < len(a) and i2 < len(b):
            if a[i1] < b[i2]:
                tmp.append(a[i1])
                i1 += 1
            else:
                tmp.append(b[i2])
                i2 += 1
        tmp.extend(a[i1:])
        tmp.extend(b[i2:])
        return tmp
    return recursive(0, len(arr) - 1)

def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

# --- Benchmarking Function ---

def benchmark(sorting_functions, array_sizes):
    for size in array_sizes:
        print(f"\n--- Benchmark for array size: {size} ---")
        original = [random.randint(0, 99999) for _ in range(size)]
        for name, func in sorting_functions.items():
            arr = original.copy()
            start = time.time()
            result = func(arr)
            duration = time.time() - start
            print(f"{name:<15}: {duration:.6f} seconds")

# --- Run Benchmarks ---

sorting_algorithms = {
    "Heap Sort": heapSort,
    "Radix Sort": radixSort,
    "Quick Sort": quickSort,
    "Merge Sort": mergeSort,
    "Insertion Sort": insertionSort
}

benchmark(sorting_algorithms, array_sizes=[100, 1000, 5000])
