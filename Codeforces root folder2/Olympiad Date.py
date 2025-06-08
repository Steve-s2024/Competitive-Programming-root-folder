t = int(input())
for pos in range(t):
    input()
    dateRef = {
        0:3,
        1:1,
        2:2,
        3:1,
        5:1
    }
    count = 8
    arr = [int(e) for e in input().split(' ')]
    for i, d in enumerate(arr):
        if d in dateRef and dateRef[d] > 0:
            dateRef[d] -= 1
            count -= 1
        if count <= 0:
            print(i+1)
            break
    else:
        print(0)