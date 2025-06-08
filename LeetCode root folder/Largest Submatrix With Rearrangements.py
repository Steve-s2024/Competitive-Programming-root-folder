# smart way of doing it, hashing 1s count at each position and
# sorting them and greedly pick largest matrix. I did figure this out...: 16%
# 700th question!!🎉
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        hashMap = defaultdict(list)
        row, col = len(matrix), len(matrix[0])
        for c in range(col):
            ones = 0
            for r in range(row-1, -1, -1):
                if matrix[r][c] == 0:
                    ones = 0
                    continue
                ones += 1
                hashMap[r].append(ones)
        # print(hashMap)
        res = 0
        for val in hashMap.values():
            nums = sorted(val, reverse = True)
            for i in range(len(nums)):
                res = max(res, (i+1)*nums[i])
        return res


# brute force:TLE
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        hashMap = defaultdict(int)
        row, col = len(matrix), len(matrix[0])
        res = 0
        for start in range(row):
            # print('start: ', start)
            colIdx = [i for i in range(col)]
            for r in range(start, row):
                tmp = []
                for c in colIdx:
                    if matrix[r][c] == 1:
                        tmp.append(c)
                colIdx = tmp
                # print(r, tmp)
                res = max(res, (r-start+1)*len(tmp))
        return res
    