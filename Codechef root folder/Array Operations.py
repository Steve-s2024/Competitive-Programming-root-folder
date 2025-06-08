# not an easy one my god...
# cook your dish here
t = int(input())
for q in range(t):
    size = int(input())
    nums = [int(e) for e in input().split(" ")]
    if size == 1:
        print(nums[0])
        continue

    max_ = nums[0]
    maxIs = []
    for idx, num in enumerate(nums):
        if num > max_:
            max_ = num
            maxIs = [idx]
        elif num == max_:
            maxIs.append(idx)
    # print(maxIs)
    for i in maxIs:
        if i % 2 == 0:
            print(int(max_ + (size - 1) / 2))
            break
    else:
        print(int(max_ + (size - 3) / 2))
