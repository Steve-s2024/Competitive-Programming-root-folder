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



'''
here is the C implementation of minheap

void recursive(int i, int *arr, int n) {
    int l = 2*i+1, r = 2*i+2;
    int j = i;
    if (l < n && arr[l] < arr[j]) j = l;
    if (r < n && arr[r] < arr[j]) j = r;
    if (j != i) {
        int a = arr[i], b = arr[j];
        arr[i] = b;
        arr[j] = a;
        recursive(j, arr, n);
    }
}

void heapify(int *arr, int n) {
    for (int i = (n-1)/2; i >= 0; i--) recursive(i, arr, n);
}

void push(int *arr, int *n, int val) {
    arr[*n] = val;
    (*n)++;
    int j = *n-1;
    int i = (int)((j-1)/2);
    while (i >= 0 && arr[i] > arr[j]) {
        int a = arr[i], b = arr[j];
        arr[i] = b;
        arr[j] = a;
        j = i;
        i = (int)((j-1)/2);
    }
}

int pop(int *arr, int *n) {
    if (*n == 0) return INT_MIN;
    int a = arr[0], b = arr[*n-1];
    arr[0] = b;
    (*n)--;
    recursive(0, arr, *n);
    return a;
}

'''

