# dfs & hashing the size of each island
# try each water cell, time complexity is 
# probably the same with the average: 5%
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        hashMap = defaultdict(int)
        sizeMap = defaultdict(int)
        visited = set()
        def dfs(r, c):
            nonlocal curId
            res = 1
            for R, C in [(r+1, c),(r-1, c),(r, c+1),(r, c-1)]:
                if (
                    R in range(row) and 
                    C in range(col) and
                    grid[R][C] == 1 and
                    (R, C) not in visited 
                ):
                    visited.add((R, C))
                    hashMap[(R, C)] = curId
                    res += dfs(R, C)
            return res
        curId = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    hashMap[(r, c)] = curId
                    size = dfs(r, c)
                    if size == row * col:
                        return row * col
                    sizeMap[curId] = size
                    curId+=1
        # print(hashMap, sizeMap)

        maxSize = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    hashSet = set()
                    curSize = 1
                    for R, C in [(r+1, c),(r-1, c),(r, c+1),(r, c-1)]:
                        if (
                            R in range(row) and 
                            C in range(col) and
                            grid[R][C] == 1 and
                            hashMap[(R, C)] not in hashSet
                        ):
                            hashSet.add(hashMap[(R, C)])
                            curSize += sizeMap[hashMap[(R, C)]]
                    maxSize = max(maxSize, curSize)
        return maxSize