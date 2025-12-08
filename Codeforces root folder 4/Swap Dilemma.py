# Array inversion solution, the keen observation is that we can discuss only adjacent swaps, and when do that we
# only need to know if the number of adjacent swaps to sort each array shares the same parity.

def getCnt(arr):
    cnt = 0
    def recursive(l, r):
        nonlocal cnt
        if l == r: return [arr[l]]
        m = (l+r)//2
        arr1, arr2 = recursive(l, m), recursive(m+1, r)
        i, j = 0, 0
        arr3 = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                arr3.append(arr1[i])
                i += 1
            else:
                cnt += len(arr1)-i
                arr3.append(arr2[j])
                j += 1
        while i < len(arr1):
            arr3.append(arr1[i])
            i += 1
        while j < len(arr2):
            arr3.append(arr2[j])
            j += 1
        return arr3

    recursive(0, len(arr)-1)
    return cnt


def solve():
    n = int(input())
    arr = [int(e) for e in input().split()]
    brr = [int(e) for e in input().split()]

    s1, s2 = sorted(arr), sorted(brr)
    for i in range(n):
        if s1[i] != s2[i]:
            print('no')
            return

    if getCnt(arr)%2 == getCnt(brr)%2:
        print('yes')
    else:
        print('no')


t = int(input())
for i in range(t): solve()