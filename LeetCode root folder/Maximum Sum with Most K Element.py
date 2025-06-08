# brute-force: tle

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        if k == 0:
            return 0
        hashMap = defaultdict(list)
        arr = []
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                hashMap[grid[r][c]].append(r)
                arr.append(grid[r][c])
        # print(hashMap)
        arr.sort(reverse=True)
        rowCount = defaultdict(int)
        res = 0
        for num in arr:
            # print(hashMap[num])
            for row in hashMap[num]:
                if rowCount[row] < limits[row]:
                    rowCount[row] += 1
                    res += num
                    hashMap[num].remove(row)
                    # print(num)
                    k -= 1
                    if k == 0:
                        break
            else:
                continue
            break

        return res