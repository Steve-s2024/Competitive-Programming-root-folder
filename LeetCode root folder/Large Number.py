# brute force O(n!)

'''class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        maxSeq = '0'

        def dfs(seq, nums):
            nonlocal maxSeq
            if len(nums) == 0:
                maxSeq = seq if int(seq) > int(maxSeq) else maxSeq
            for idx in range(len(nums)):
                dfs(seq + str(nums[idx]), nums[:idx] + nums[idx+1:])
        dfs('', nums)
        return maxSeq'''


# solution no.2: almost worked
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        trie = {}
        for num in nums:
            cur = trie
            for char in str(num):
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            if 'end' not in cur:
                cur['end'] = 0
            cur['end'] += 1

        def dfs(cur, seq, head, arr):
            for i in range(9, head-1, -1):
                if str(i) in cur:
                    dfs(cur[str(i)], seq+str(i), head, arr)
            if 'end' in cur:
                arr.append(seq * cur['end'])
            for i in range(head-1, -1, -1):
                if str(i) in cur:
                    dfs(cur[str(i)], seq+str(i), head, arr)

        arr = []
        for i in range(9, -1, -1):
            if str(i) in trie:
                dfs(trie[str(i)], str(i), i, arr)
        # print(arr)
        res = ''.join(arr)
        if int(res) == 0:
            return '0'
        return res
'''


