# couldn't solve during contest, and many other did. turns out it only need you to know
# KMP implementation:
class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        row, col = len(grid), len(grid[0])
        rowChar, colChar = [], []
        for r in range(row):
            for c in range(col):
                rowChar.append(grid[r][c])
        for c in range(col):
            for r in range(row):
                colChar.append(grid[r][c])
        rowStr, colStr = ''.join(rowChar), ''.join(colChar)
        # print(rowStr, colStr)

        arr1 = Solution.KMP(rowStr, pattern)
        arr2 = Solution.KMP(colStr, pattern)

        cnt = 0
        for r in range(row):
            for c in range(col):
                while arr1 and cnt > arr1[0][1]:
                    arr1.popleft()
                if not arr1:
                    break
                if cnt in range(arr1[0][0], arr1[0][1] + 1):
                    grid[r][c] = ''
                cnt += 1
            else:
                continue
            break

        res = 0
        cnt = 0
        for c in range(col):
            for r in range(row):
                while arr2 and cnt > arr2[0][1]:
                    arr2.popleft()
                if not arr2:
                    break
                if cnt in range(arr2[0][0], arr2[0][1] + 1) and grid[r][c] == '':
                    res += 1
                cnt += 1
            else:
                continue
            break
        return res

    @staticmethod
    def KMP(s, p):
        n, m = len(s), len(p)
        lps = [0] * m
        length = 0
        for i in range(1, m):
            while length and p[i] != p[length]:
                length = lps[length - 1]
            if p[i] == p[length]:
                length += 1
                lps[i] = length

        intervals = deque([])
        j = 0
        for i in range(n):
            while j and s[i] != p[j]:
                j = lps[j - 1]
            if s[i] == p[j]:
                j += 1
            if j == m:
                if intervals and intervals[-1][1] >= i - m + 1:
                    intervals[-1][1] = i
                else:
                    intervals.append([i - m + 1, i])
                j = lps[j - 1]

        return intervals


# brute force: TLE
class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        row, col = len(grid), len(grid[0])
        n = len(pattern)
        good = set()
        def markCell(R, C, s):
            nonlocal n, row, col
            r, c = R, C
            i = 0
            coors = []
            while True:
                if s[i] != grid[r][c]:
                    break
                else:
                    coors.append((r, c))
                    i += 1
                c += 1
                if c >= col:
                    c = 0
                    r += 1
                if r >= row or i >= n:
                    break
            if i >= n:
                for coor in coors:
                    good.add(coor)
            # print(R, C, i)
        for r in range(row):
            for c in range(col):
                # check the current place as start
                markCell(r, c, pattern)

        res = 0
        for C in range(col):
            for R in range(row):
                # check the vertical one
                r, c = R, C
                i = 0
                coors = []
                while i <= n:
                    if pattern[i] == grid[r][c]:
                        coors.append((r, c))
                        i += 1
                    else:
                        break
                    r += 1
                    if r >= row:
                        r = 0
                        c += 1
                    if c >= col or i >= n:
                        break
                if i >= n:
                    for coor in coors:
                        if coor in good:
                            good.remove(coor)
                            res += 1
        return res