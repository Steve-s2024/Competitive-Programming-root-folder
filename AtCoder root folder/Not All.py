from collections import defaultdict, deque, Counter
import cmath, heapq

def solve():
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    st = set(nums)
    flag = True
    for i in range(1, m+1):
        if i not in st:
            flag = False

    cnt = 0
    if flag:
        mp = Counter(nums)
        for i in range(n-1, -1, -1):
            cnt += 1
            mp[nums[i]] -= 1
            if mp[nums[i]] == 0 and nums[i] in range(1, m+1):
                break
    print(cnt)
solve()

