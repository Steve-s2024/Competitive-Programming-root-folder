n = int(input())
arr = [int(e) for e in input().split(' ')]
wrong = 0
l, r = 0, len(arr)-1
while l < len(arr) and arr[l] == l+1:
    l += 1

if l == len(arr):
    print('0 0')
else:
    while arr[r] == r+1:
        r -= 1
    for i in range(l+1, r+1):
        if arr[i] - arr[i-1] != -1:
            print('0 0')
            break
    else:
        print(str(l+1) + ' ' + str(r+1))