# solved, the stupid interactive feature rejecting my code
from collections import defaultdict, deque, Counter
import heapq, math
import sys

def printMsg(msg):
    print(msg)
    sys.stdout.flush()
    tmp = int(input())
    if tmp == -1:
        sys.exit()
    return tmp

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    st = set([i for i in range(1, n+1)])

    for num in nums:
        if num in st:
            st.remove(num)
    if len(st):
        res = printMsg('? ' + str(list(st)[0]) + ' ' + str(nums[0]))
        print('! A') if res == 0 else print('! B')
    else:
        a = printMsg('? 1 ' + str(n))
        b = printMsg('? ' + str(n) + ' 1')
        if (
            min(a, b) >= n-1
        ):
            print('! B')
        else:
            print('! A')

    sys.stdout.flush()
t = int(input())
for i in range(t):
    solve()


