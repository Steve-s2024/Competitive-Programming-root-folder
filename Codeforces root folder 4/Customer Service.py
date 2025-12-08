# not a bad one, but exhausting. this question is the epitome of the idea that a question is easy if your brain is
# capable of being completely meticulous and rational, not fell in for any logical trap, once your brain no longer lazy
# and blindly follow casual intuition, then the solution actually awaits. you have to be completely aware of exactly
# what is going to happen when simulating the process of a queue being served, with this particular set up.

from math import inf
def solve():
    n = int(input())
    grid = []
    for i in range(n):
        row = [int(e) for e in input().split()]
        grid.append(row)

    arr = []
    for r in grid:
        i = n-1
        cnt = 0
        while i >= 0 and r[i] == 1:
            i -= 1
            cnt += 1
        arr.append(cnt)

    res = n
    for i in range(n):
        mi, idx = inf, -1
        for j in range(len(arr)):
            if mi > arr[j] >= i:
                mi = arr[j]
                idx = j
        if idx == -1:
            res = i
            break
        arr[idx] = -inf

    print(res)







t = int(input())
for i in range(t):
    solve()

