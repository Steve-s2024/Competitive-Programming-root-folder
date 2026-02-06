# tricky one...
t = int(input())
for tt in range(t):
    [n, k] = [int(e) for e in input().split(' ')]

    left = [int(e) for e in input().split(' ')]
    right = [int(e) for e in input().split(' ')]
    mins = []
    for i in range(n):
        mins.append(min(left[i], right[i]))
    mins.sort()
    res = sum(left) + sum(right) - sum(mins[:n - k + 1]) + 1
    print(res)
