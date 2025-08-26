# either is question is stupid, or I am stupid to not think of the right approach to avoid precision lost
# I and too hang-on the decimal precision, and forget it can be solved via the GP property b^2 == a*c for all
# consecutive a, b, c. just sort them my magnitude
from decimal import Decimal, getcontext
getcontext().prec = 100
def helper(nums):
    n = len(nums)
    if n <= 1: return True
    # prev = nums[0]/nums[1]
    prev = Decimal(nums[0]) / Decimal(nums[1])
    for i in range(1, n):
        # cur = nums[i-1]/nums[i]
        cur = Decimal(nums[i-1]) / Decimal(nums[i])
        ep = Decimal('1e-49')
        if abs(cur-prev) > ep: return False
    return True


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    neg = []
    pos = []
    for num in nums:
        if num < 0: neg.append(num)
        else: pos.append(num)

    neg.sort(reverse = True)
    pos.sort()
    s1, s2 = len(neg), len(pos)
    if s1 == 0:
        if helper(pos): print('Yes')
        else: print('No')
        return
    if s2 == 0:
        if helper(neg): print('Yes')
        else: print('No')
        return

    if abs(s1-s2) > 1:
        print('No')
        return

    if s1 > s2:
        i1, i2 = 0, 0
        arr = []
        arr.append(neg[i1])
        i1 += 1
        while i1 < s1:
            arr.append(pos[i2])
            i2 += 1
            arr.append(neg[i1])
            i1 += 1
        print(arr)
        if helper(arr):
            print('Yes')
        else:
            print('No')

    elif s2 > s1:
        i1, i2 = 0, 0
        arr = []
        arr.append(pos[i2])
        i2 += 1
        while i1 < s1:
            arr.append(neg[i1])
            i1 += 1
            arr.append(pos[i2])
            i2 += 1
        if helper(arr):
            print('Yes')
        else:
            print('No')

    else:
        i1, i2 = 0, 0
        arr = []
        while i1 < s1:
            arr.append(neg[i1])
            i1 += 1
            arr.append(pos[i2])
            i2 += 1
        if helper(arr):
            print('Yes')
            return
        i1, i2 = 0, 0
        arr = []
        while i1 < s1:
            arr.append(pos[i2])
            i2 += 1
            arr.append(neg[i1])
            i1 += 1
        if helper(arr):
            print('Yes')
            return
        print('No')

t = int(input())
for i in range(t):
    solve()



