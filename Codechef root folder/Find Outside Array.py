# it is actually suppose to be like this...
# cook your dish here
t = int(input())
for tt in range(t):
    n = int(input())
    nums = [int(e) for e in input().split(' ')]
    nums.sort()
    if nums[0] < 0:
        print(str(nums[0])+' '+str(nums[0]))
    elif nums[-1] > 0:
        print(str(nums[-1])+' '+str(nums[-1]))
    else:
        print(-1)



# don't know why this didn't work...
# cook your dish here
t = int(input())
for tt in range(t):
    n = int(input())
    nums = [int(e) for e in input().split(' ')]
    nums.sort()
    if n == 1:
        if nums == 0:
            print(-1)
        else:
            print(nums[0], nums[0])
    else:
        if nums[0] < 0 and nums[1] != 0:
            # print(nums[0], nums[1])
            print(str(nums[0])+' '+str(nums[1]))
        elif nums[-1] > 0 and nums[-2] != 0:
            # print(nums[-2], nums[-1])
            print(str(nums[-2])+' '+str(nums[-1]))
        elif nums[0] != 0 and nums[-1] != 0 and nums[0]+nums[-1] != 0:
            # print(nums[0], nums[-1])
            print(str(nums[0])+' '+str(nums[-1]))
        else:
            print(-1)