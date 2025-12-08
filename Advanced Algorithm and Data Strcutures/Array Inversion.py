# this algorithm use merge sort to quickly find the count of inversions in an array.

# behold, merge sort array inversion counting. though share the same complexity as the one below, this one don't
# require sorted list but also making it practically slower.
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


# this algorithm uses a position array, and the array inversion counting to find the minimum number of adjacent
# element swap needed on str1 to make it equal to str2, given that str1 is a permutation of str2
# more efficient way of doing inversion counting. however, most platform does not support sorted list.
from sortedcontainers import SortedList

def arrayInversion(str1, str2):
    n = len(str1)
    mp = [[] for _ in range(10)]
    imp = [0] * 10
    for i in range(n): mp[int(str1[i])].append(i)

    pos = []
    for i in range(n):
        x = int(str2[i])
        pos.append(mp[x][imp[x]])
        imp[x] += 1

    sl = SortedList()
    inv = 0
    for i in range(n):
        inv += len(sl) - sl.bisect_right(pos[i])
        sl.add(pos[i])
    return inv


print(
    arrayInversion('5489355142', '5489355421'),
    arrayInversion('11112', '21111'),
    arrayInversion('00123', '00132')
)
