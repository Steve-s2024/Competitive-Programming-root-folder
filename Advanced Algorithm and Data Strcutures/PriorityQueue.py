# max heap
class maxHeap:
    @staticmethod
    def recursive(i, arr, n):
        l, r = 2 * i + 1, 2 * i + 2
        j = i
        if l < n and arr[l] > arr[j]:
            j = l
        if r < n and arr[r] > arr[j]:
            j = r
        if j != i:
            a, b = arr[i], arr[j]
            arr[i], arr[j] = b, a
            maxHeap.recursive(j, arr, n)

    @staticmethod
    def heapify(arr):
        n = len(arr)
        for i in range(n-1, -1, -1):
            maxHeap.recursive(i, arr, n)

    @staticmethod
    def push(arr, val):
        arr.append(val)
        n = len(arr)
        j = n-1
        i = (j-1) // 2
        while i >= 0 and arr[i] < arr[j]:
            a, b = arr[i], arr[j]
            arr[i], arr[j] = b, a
            j = i
            i = (j-1)//2

    @staticmethod
    def pop(arr):
        n = len(arr)
        a, b = arr[0], arr[n-1]
        arr[0], arr[n - 1] = b, a
        arr.pop()
        n = len(arr)
        maxHeap.recursive(0, arr, n)
        return a


# arr = [1,4,2,3,6,0]
# print(arr)
# maxHeap.heapify(arr)
# maxHeap.push(arr, 1)
# maxHeap.push(arr, 5)
# maxHeap.push(arr, 8)
# maxHeap.push(arr, 3)
# maxHeap.push(arr, 3)
# print(arr)
# maxHeap.pop(arr)
# maxHeap.pop(arr)
# maxHeap.pop(arr)
# print(arr)

