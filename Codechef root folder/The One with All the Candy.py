# don't know what is this, barely 1300.
# cook your dish here
t = int(input())
for tt in range(t):
    n = int(input())
    nums = [int(e) for e in input().split(' ')]
    nums.sort()
    i = 0
    while i < n:
        if nums[i] != nums[0]:
            break
        i += 1

    res = n * nums[0]
    res += n - i
    print(res)