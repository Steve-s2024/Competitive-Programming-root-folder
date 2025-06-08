n = int(input())
for i in range(n):
    length = int(input())
    arr = [int(e) for e in input().split(' ')]
    # print(arr)
    tar = arr[0]
    arr.sort()
    for num in arr:
        if num > tar:
            # print(num, tar)
            tar += (num - tar + 1) // 2
            # print(tar)
    print(tar)


