# greedy solution, the thing is to recognize that you can flip any pairs of element regardless whether if they are
# adjacent as long as you are allowed to do unlimited number of the operation to flip
# two adjacent elements:118
# ms
# Beats
# 7.30%
from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        arr = []
        row, col = len(matrix), len(matrix[0])
        for r in range(row):
            for c in range(col):
                arr.append(matrix[r][c])
        arr.sort()
        i = 1
        # print(arr)
        while i < len(arr):
            if arr[i] <= 0 and arr[i-1] <= 0:
                arr[i] = abs(arr[i])
                arr[i-1] = abs(arr[i-1])
            if arr[i] >= 0 and arr[i-1] <= 0:
                if abs(arr[i-1]) > abs(arr[i]):
                    arr[i-1] = -1*arr[i-1]
                    arr[i] = -1*arr[i]
                break
            i += 2
        # print(arr)
        return sum(arr)