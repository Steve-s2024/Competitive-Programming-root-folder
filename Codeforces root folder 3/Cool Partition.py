# nice, three question under 10 minutes
import sys
sys.setrecursionlimit(100000000)

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    res = 1
    st = set()
    st.add(nums[0])
    tmp = set()
    for i in range(1, n):
        tmp.add(nums[i])
        if nums[i] in st:
            st.remove(nums[i])
            if len(st) == 0:
                res += 1
                st = tmp
                tmp = set()
    print(res)


t = int(input())
for i in range(t):
    solve()

