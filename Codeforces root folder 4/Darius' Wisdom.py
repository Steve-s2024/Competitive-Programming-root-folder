# although didn't drive me mad, but definitely gave me a hard time. don't like this question where I have to guess
# with nothing to support it. nonetheless, it worked
# I think this is overcomplicating the question and is not the intended way

from collections import deque, Counter, defaultdict


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    arr = [0]*3
    f = nums[0] != 1
    ans = []
    for i in range(n):
        arr[nums[i]] += 1
        if f and nums[i] == 1:
            nums[0], nums[i] = nums[i], nums[0] # make sure at least one 1 is not in their interval
            ans.append((0, i))
            f = not f
    zero, one, two = [], [], deque()
    for i in range(n):
        if nums[i] == 0: zero.append(i)
        if nums[i] == 1 and i not in range(arr[0], n-arr[2]): one.append(i)
        if nums[i] == 2: two.append(i)

    for idx in one:
        i = idx
        while i not in range(arr[0], n-arr[2]):
            if i < arr[0]: # move a zero to this position
                j = zero.pop()
                ans.append((i, j))
                i = j
            elif i >= n-arr[2]: # move a two to this position
                j = two.popleft()
                ans.append((i, j))
                i = j
    print(len(ans))
    for u, v in ans:
        print(f'{u+1} {v+1}')


t = int(input())
for i in range(t): solve()