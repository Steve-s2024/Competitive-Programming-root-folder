# for some reason this is failing submission
t = int(input())
for pos in range(t):
    sign = True
    [n, m] = [int(e) for e in input().split(' ')]
    ans = ['-1'] * n
    for i in range(n):
        arr = sorted([int(e) for e in input().split(' ')])
        begin = arr[0]
        ans[begin] = str(i+1)
        for j in range(1, len(arr)):
            if arr[j] - arr[j-1] != n:
                sign = False
                break
    if sign:
        print(' '.join(ans))
    else:
        print('-1')


