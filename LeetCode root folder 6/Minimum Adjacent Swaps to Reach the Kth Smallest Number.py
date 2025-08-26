# find next permutation and array inversion solution: 5%

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        arr = list(num)
        n = len(arr)
        for _ in range(k):
            stk = [(int(arr[-1]), n - 1)]
            i = n - 2
            while i >= 0:
                if int(arr[i]) < stk[-1][0]:
                    mxIdx = -1
                    while stk:
                        val, idx = stk.pop()
                        if val > int(arr[i]): mxIdx = idx
                    arr[mxIdx], arr[i] = arr[i], arr[mxIdx]
                    tmp = arr[i + 1:n]
                    tmp.sort()
                    for j in range(i + 1, n): arr[j] = tmp[j - (i + 1)]
                    break
                stk.append((int(arr[i]), i))
                i -= 1

                # array inversion part
        str1, str2 = num, ''.join(arr)
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

