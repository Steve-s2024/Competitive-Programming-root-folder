// daily question, an easy minheap implementation, but when doing with C, nothing is easy. look at this humongous code
//: 45%

#define max(a, b) ((a) > (b) ? (a) : (b))

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

// int test() {
//     int arr[100];
//     int size = 0;

//     push(arr, &size, 5);
//     push(arr, &size, 10);
//     push(arr, &size, 3);

//     printf("%d\n", pop(arr, &size)); // 10
//     printf("%d\n", pop(arr, &size)); // 5
//     printf("%d\n", pop(arr, &size)); // 3

//     return 0;
// }

int cmp(const void *a, const void *b) {
    int *x = *(int **)a;
    int *y = *(int **)b;
    return x[0] - y[0]; // Sort by start day
}

int maxEvents(int** events, int eventsSize, int* eventsColSize) {
    qsort(events, eventsSize, sizeof(int*), cmp);
    // test();
    int *minheap;
    minheap = malloc(sizeof(int)*eventsSize);
    int n = 0;
    int mx = 0;
    for (int i = 0; i < eventsSize; i++) mx = max(mx, events[i][1]);
    int j = 0;
    int cnt = 0;

    for (int day = 1; day <= mx; day++) {
        while(j < eventsSize && events[j][0] == day) {
            push(minheap, &n, events[j][1]);
            j++;
        }
        while(n > 0 && minheap[0] < day) pop(minheap, &n);
        if (n > 0) {
            pop(minheap, &n);
            cnt++;
        }
    }
    free(minheap);
    return cnt;
}