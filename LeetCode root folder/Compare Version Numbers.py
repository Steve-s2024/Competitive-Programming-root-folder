# this should be an easy.
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split('.')
        arr2 = version2.split('.')
        maxLen = max(len(arr1), len(arr2))
        arr1 += ['0'] * (maxLen - len(arr1))
        arr2 += ['0'] * (maxLen - len(arr2))
        i1, i2 = 0, 0
        while i1 < maxLen:
            if int(arr1[i1]) > int(arr2[i2]):
                return 1
            elif int (arr1[i1]) < int(arr2[i2]):
                return -1
            i1 += 1
            i2 += 1
        return 0