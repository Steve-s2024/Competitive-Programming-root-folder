# very good problem on expanding the general maximum XOR pair algorithm
# we not just construct/accumulate the trie, also need to deconstruct it. basically only maintain the trie of a sliding window
# I just used the node frequency mechanism to handle this, turns out it can be made very easily to implement
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        trie = {}
        res = 0
        j = 0
        for i in range(n):
            # remove from trie
            while 2 * nums[j] < nums[i]:
                cr = trie
                for c in str(bin(nums[j]))[2:].zfill(20):
                    cr = cr[c]
                    cr['x'] -= 1
                j += 1

            # add to trie
            cr = trie
            for c in str(bin(nums[i]))[2:].zfill(20):
                if c not in cr: cr[c] = {'x': 0}
                cr = cr[c]
                cr['x'] += 1

            # max XOR pair searching
            cr = trie
            ar = []
            for c in str(bin(nums[i]))[2:].zfill(20):
                op = '1' if c == '0' else '0'
                if op in cr and cr[op]['x']:
                    cr = cr[op]
                    ar.append(op)
                else:
                    cr = cr[c]
                    ar.append(c)

            a = int(''.join(ar), 2) ^ nums[i]
            res = max(res, a)

        return res


