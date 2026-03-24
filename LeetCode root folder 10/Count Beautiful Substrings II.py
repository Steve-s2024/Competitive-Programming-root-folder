# counting subarray with zero sum can be made O(n) -> frequency map
# even if limiting the size of subarray to be multiple of a number, which is what happened here, it can still be O(n)
# this idea can be extended, for finding count of subarray following certain rules, and also limiting the size of subarray to
# be multiple of some number x. the complexity will be x*TC(n/x), where TC(n) is the complexity for finding subarray count on n element

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        ar = []
        for c in s:
            if c in 'aeiou': ar.append(1)
            else: ar.append(-1)
        n = len(ar)
        pre = [0]*n
        for i in range(n): pre[i] = pre[i-1] + ar[i]

        a = -1
        for i in range(1, n//2+1):
            if (i*i) % k == 0:
                a = i
                break
        if a == -1: return 0
        a *= 2
        # print(a)
        # print(ar)
        # print(pre)
        ans = 0
        for i in range(a):
            mp = defaultdict(int)
            if i == a-1: mp[0] = 1
            for j in range(i, n, a):
                ans += mp[pre[j]]
                mp[pre[j]] += 1
            # print(mp)
        return ans


