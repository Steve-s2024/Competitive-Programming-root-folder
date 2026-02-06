n = int(input())
for pos in range(n):
    size = input()
    arr = [int(e) for e in input().split(' ')]
    tar = [int(e) for e in input().split(' ')]

    totalReduce = 0
    for i in range(len(arr)):
        reduce = max(tar[i]- arr[i], 0)
        totalReduce += reduce
    # print(totalReduce)
    for i in range(len(arr)):
        reduce = max(tar[i] - arr[i], 0)
        curVal = max(tar[i], arr[i]) - (totalReduce - reduce)
        if curVal < tar[i]:
            print('NO')
            break
    else:
        print('YES')