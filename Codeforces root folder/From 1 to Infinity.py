# fucking shaking hands pounding hearts I almost failed it holy fuck! its fucking survival time!!🥵
# king of survival right here!!!!
def solve():
    k = int(input())
    size = 1
    pos = 0
    while pos < k:
        inc = 9*pow(10, size-1)*size
        if inc + pos > k: break
        pos += inc
        size += 1
    rem = k - pos
    mul = rem//size # mul --> the number of numbers of length 'size' that belong to the incomplete range i.e. [1000, 9999] not include the incomplete number
    re = rem%size # re --> the length of the incomplete number

    # print(size, mul, re)
    num = pow(10, size-1)-1 + mul
    # print(num)

    def getSum(n, p):
        # p --> the pos of the digit, start with 1
        f = pow(10, p)
        arr = [n // f * f // 10] * 10
        re = (n * 10 // f) % 10
        for i in range(re):
            arr[i] += f // 10
        if p > 1:
            tail = int(str(n)[-p + 1:])
            arr[re] += tail + 1
        else:
            arr[re] += 1
        return arr

    arr = [0]*10
    for i in range(len(str(num))):
        for i, val in enumerate(getSum(num, i + 1)):
            arr[i] += val
    sm = 0
    for i, val in enumerate(arr):
        sm += i*val

    if re != 0:
        incmpNum = str(num+1)[:re]
        for c in str(incmpNum):
            sm += int(c)
    print(sm)





t = int(input())
for i in range(t):
    solve()
