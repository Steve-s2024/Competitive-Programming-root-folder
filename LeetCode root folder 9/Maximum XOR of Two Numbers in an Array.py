# quite unintuitive problem, but once you realize it is trie, the problem becomes developing a simple greedy
# algorithm on the trie

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = len(nums)
        l = len(str(bin(max(nums)))[2:])
        trie = {}
        for i in range(n):
            s = str(bin(nums[i]))[2:].zfill(l)
            cr = trie
            for c in s:
                if c not in cr: cr[c] = {}
                cr = cr[c]
            cr['end'] = 1

        mx = 0
        for v in nums:
            s = str(bin(v))[2:].zfill(l)
            cr = trie
            res = []
            for c in s:
                if c == '1' and '0' in cr:
                    cr = cr['0']
                    res.append('0')
                elif c == '0' and '1' in cr:
                    cr = cr['1']
                    res.append('1')
                else:
                    cr = cr[c]
                    res.append(c)
            x = int(''.join(res), 2)
            mx = max(mx, x ^ v)
        return mx