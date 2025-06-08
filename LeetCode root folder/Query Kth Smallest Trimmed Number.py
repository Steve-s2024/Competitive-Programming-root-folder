# brute force and hash map solution:696
# ms
# Beats
# 11.26%
'''class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        hashMap = defaultdict(list)
        for num in nums:
            cur = ''
            for i in range(len(num)-1, -1, -1):
                cur = num[i] + cur
                curMap = hashMap[len(cur)]
                curMap.append([int(cur), len(curMap)])
        for key, val in hashMap.items():
            hashMap[key] = sorted(val, key = lambda i : i[0])
        # print(hashMap)
        ans = []
        for n1, n2 in queries:
            ans.append(hashMap[n2][n1-1][1])
        return ans'''

# the harder and better way, radix sort, this sorting algorithm is very efficient!:139
# ms
# Beats
# 99.20%
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        wordSize = len(nums[0])
        hashMap = defaultdict(list)
        tmp = []
        for i, n in enumerate(nums):
            tmp.append((i, n))
        nums = tmp

        for pos in range(wordSize - 1, -1, -1):
            curMap = defaultdict(list)
            for num in nums:
                curMap[num[1][pos]].append(num)
            arr = []
            for i in range(10):
                arr += curMap[str(i)]
            # print(arr)
            nums = arr
            hashMap[wordSize - pos] = arr
        # print(hashMap)
        ans = []
        for n1, n2 in queries:
            tar = hashMap[n2][n1 - 1]
            ans.append(tar[0])
        return ans


