# a variation of the problem "finding pair in array that yields the maximum xor value", where we apply trie to do matching
# greedily, turn the problem from n^2 into nlogn.
# here we need that, and also the concept of offline query, this is probably the first time i practice offline query haha.


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums = sorted(set(nums))
        n = len(nums)
        cp = [(e[0], e[1], i) for i, e in enumerate(queries)]
        cp.sort(key = lambda i:i[1])
        trie = {}
        j = 0
        ans = []
        for x, m, _ in cp:
            if nums[0] > m:
                ans.append(-1)
                continue
            while j < n and nums[j] <= m:
                tr = str(bin(nums[j]))[2:].zfill(30)
                cr = trie
                for c in tr:
                    if c not in cr: cr[c] = {}
                    cr = cr[c]
                j += 1
            res = []
            cr = trie
            for c in str(bin(x))[2:].zfill(30):
                op = '1' if c == '0' else '0'
                if op in cr:
                    res.append(op)
                    cr = cr[op]
                else:
                    res.append(c)
                    cr = cr[c]
            ans.append(int(''.join(res), 2)^x)
        # print(cp)
        # print(ans)

        q = len(queries)
        fans = [0]*q
        for i in range(q): fans[cp[i][2]] = ans[i]
        return fans