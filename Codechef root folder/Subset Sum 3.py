# not hard but interesting

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    arr = []
    for num in nums:
        arr.append(num%3)

    zero, one, two = 0, 0, 0
    for num in arr:
        if num == 0:
            zero += 1
        if num == 1:
            one += 1
        if num == 2:
            two += 1

    if zero or one >= 3 or two >= 3 or (one >= 1 and two >= 1):
        print('Yes')
    else:
        print('No')



t = int(input())
for i in range(t):
    solve()