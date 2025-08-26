# this algorithm uses a position array, and the array inversion counting to find the minimum number of adjacent
# element swap needed on str1 to make it equal to str2, given that str1 is a permutation of str2

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
