# so ridiculous that I submitted this simply hoping to see TLE, but it passed faster than ever! hooray on the first
# 1700 question solved. kinda lucky to come to this solution.

from math import gcd, lcm, inf, sqrt, floor, ceil

def isPrime(num):
    for i in range(2, int(sqrt(num))+1):
        if num%i == 0: return False
    return True

def solve():

    n = int(input())
    arr = [i for i in range(1, n+1)]
    arr[0] = 1
    for i in range(n, 1, -1):
        if not isPrime(i): continue
        tmp = []
        for j in range(i-1, n, i):
            if arr[j] == j+1: tmp.append(arr[j])

        for idx, num in enumerate(tmp):
            arr[num-1] = tmp[(idx+1)%len(tmp)]


    print(' '.join(str(e) for e in arr))

t = int(input())
for i in range(t): solve()