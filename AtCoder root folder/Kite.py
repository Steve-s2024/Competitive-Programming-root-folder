# LIS on pairs, russian doll envelope all over again
from bisect import bisect_left, bisect_right


def solve():
    n = int(input())
    ar = []
    for _ in range(n):
        a, b = [int(e) for e in input().split()]
        ar.append((a, b))
    ar.sort(key = lambda i:(i[0], -i[1]))

    arr = []
    for a, b in ar:
        i = bisect_left(arr, b)
        if i == len(arr): arr.append(b)
        else: arr[i] = b

    print(len(arr))


solve()
