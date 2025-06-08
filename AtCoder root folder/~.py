# find all subarray that is of shape ~: AC
from collections import defaultdict, deque, Counter
import cmath, heapq



def solve():
    n = int(input())
    p = [int(e) for e in input().split()]

    stack = []
    for i in range(1, n-1):
        if p[i] < min(p[i-1], p[i+1]):
            stack.append((-1, i))
        elif p[i] > max(p[i-1], p[i+1]):
            stack.append((1, i))

    res = 0
    # print(stack)
    if stack:
        l, r = 0, stack[2][1] if len(stack) > 2 else n-1
        for i in range(1, len(stack)):
            a, b = stack[i-1], stack[i]
            if a[0] == 1 and b[0] == -1:
                # print(l, a[1], b[1], r)
                res += (a[1]-l) * (r-b[1])
            l, r = a[1], stack[i+2][1] if i+2 < len(stack) else n-1
    print(res)




solve()

