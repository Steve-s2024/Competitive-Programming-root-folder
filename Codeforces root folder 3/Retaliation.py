# wasted so much of my time one this... my expert!! no~~~
from collections import defaultdict, deque, Counter
import heapq, math
import sys

sys.setrecursionlimit(100000000)


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    st = set()
    for i in range(n-1):
        a, b = nums[i], nums[i+1]
        st.add(b-a)
    if len(st) == 1:
        k = st.pop()
        if k >= 0 and nums[0] >= k and (nums[0] - k) % (n+1) == 0:
            print('Yes')
        elif k < 0 and nums[0] >= (-k)*n and (nums[0] - (-k)*n) % (n+1) == 0:
            print('Yes')
        else:
            print('No')

    else:
        print('No')


t = int(input())
for i in range(t):
    solve()


# TLE
from collections import defaultdict, deque, Counter
import heapq, math
import sys
sys.setrecursionlimit(100000000)

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    flag = False
    for i in range(nums[0]+1):
        for j in range(nums[0]//n+1):
            if i + j*n != nums[0]:
                continue
            # print(i, j)
            for k in range(1, n):
                a, b = k+1, n-k
                # print(i, a, j, b)
                if i*a + j*b != nums[k]:
                    break
            else:
                flag = True
            if flag:
                break
        else: continue
        break

    if flag:
        print('Yes')
    else:
        print('No')

t = int(input())
for i in range(t):
    solve()

